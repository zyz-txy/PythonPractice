# -*- coding: utf-8 -*-
"""
08_improve_case.py
对原 07_library_sysytem.py 的改进版：使用面向对象设计和更人性化的命令行交互。
功能要点：
- 更友好的菜单与命令（支持命令式输入：list/search/info/borrow/return/my/logout/quit/help）
- 修复原实现中的 bug（借书可用数判断、还书调用、类型拼写等）
- 更好的错误处理与提示
- 中文注释，直接运行即可（依赖 data/books.json 与 data/members.json）

使用：python 08_improve_case.py
"""

from __future__ import annotations
from typing import Dict, List, Optional
import json
import os
import getpass
import textwrap


# ----------------------------- 模型类 ---------------------------------
class Book:
    """表示一本书的类，封装编号 / 标题 / 作者 / 总数 / 可借数量等属性"""

    def __init__(self, book_id: str, title: str, author: str, total_num: int):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.total_num = int(total_num)
        # 可借数量使用私有属性维护
        self._available = int(total_num)

    def borrow(self) -> bool:
        """尝试借阅：若有可借数量则减一并返回 True，否则返回 False"""
        if self._available > 0:
            self._available -= 1
            return True
        return False

    def give_back(self) -> None:
        """归还图书：将可借数量加一（不超过总数）"""
        if self._available < self.total_num:
            self._available += 1

    def available(self) -> int:
        return self._available

    def to_dict(self) -> dict:
        return {
            "编号": self.book_id,
            "标题": self.title,
            "作者": self.author,
            "数量": self.total_num,
            "可用": self._available,
        }

    def __str__(self) -> str:
        return f"[{self.book_id}] {self.title} — {self.author} (总:{self.total_num} 可:{self._available})"


class Member:
    """会员抽象类：保存基础信息并提供借还操作的公共逻辑"""

    def __init__(self, member_id: str, name: str, password: str):
        self.member_id = member_id
        self.name = name
        self._password = password
        # 存储借阅的书籍 id 列表，便于序列化/展示
        self._borrowed: List[str] = []

    def check_password(self, pwd: str) -> bool:
        return pwd == self._password

    def borrow_book(self, book: Book) -> bool:
        """借书：
        - 检查是否已借过同一本（不允许重复借同一本）
        - 检查是否超额
        - 若图书有可借副本则从 Book 中借出并记录借阅
        - 借阅成功后显示当前还可借数量
        """
        # 不允许重复借同一本书（按书编号判断）
        if book.book_id in self._borrowed:
            print(f"借阅失败：您已借阅编号为 {book.book_id} 的图书，无法重复借阅。")
            print(f"当前还可借：{self.remaining_quota()} 本")
            return False
        # 检查是否达到最大借阅数
        if len(self._borrowed) >= self.max_books():
            print("借阅失败：已达到会员最大借阅数量。")
            print(f"当前还可借：{self.remaining_quota()} 本")
            return False
        # 尝试从 Book 对象中借出一份（Book.borrow 会在没有可借副本时返回 False）
        if book.borrow():
            self._borrowed.append(book.book_id)
            print(f"借阅成功：{self.name} 已借阅《{book.title}》")
            print(f"当前还可借：{self.remaining_quota()} 本")
            return True
        else:
            print(f"借阅失败：图书《{book.title}》暂无可借副本")
            print(f"当前还可借：{self.remaining_quota()} 本")
            return False

    def return_book(self, book: Book) -> bool:
        """还书：如果会员借了该书则完成归还并返回 True，归还后显示剩余额度"""
        if book.book_id in self._borrowed:
            book.give_back()
            self._borrowed.remove(book.book_id)
            print(f"归还成功：{self.name} 已归还《{book.title}》")
            print(f"当前还可借：{self.remaining_quota()} 本")
            return True
        print(f"归还失败：{self.name} 未借阅编号为 {book.book_id} 的图书")
        print(f"当前还可借：{self.remaining_quota()} 本")
        return False

    def borrowed_list(self) -> List[str]:
        return list(self._borrowed)

    def remaining_quota(self) -> int:
        """返回当前会员还可以借多少本书（最大借阅数 - 已借数量）"""
        return max(0, self.max_books() - len(self._borrowed))

    def to_dict(self) -> dict:
        # 子类可以在加载时提供额外字段（如 vip 等）
        return {"卡号": self.member_id, "姓名": self.name, "密码": self._password, "借阅": self._borrowed}

    def max_books(self) -> int:
        """子类覆盖：返回会员最大可借数量"""
        return 3

    def __str__(self) -> str:
        return f"{self.member_id} - {self.name} (已借 {len(self._borrowed)} 本)"


class NormalMember(Member):
    def max_books(self) -> int:
        return 3


class VIPMember(Member):
    def __init__(self, member_id: str, name: str, password: str, vip_level: int = 0):
        super().__init__(member_id, name, password)
        self.vip_level = int(vip_level)

    def max_books(self) -> int:
        # VIP 享有更高的借阅上限
        return 6 + self.vip_level

    def to_dict(self) -> dict:
        d = super().to_dict()
        d.update({"会员等级": self.vip_level})
        return d


# --------------------------- 系统类与交互 --------------------------------
class LibrarySystem:
    """图书馆管理系统：负责数据加载、用户登录与交互命令处理"""

    BOOKS_PATH = os.path.join("data", "books.json")
    MEMBERS_PATH = os.path.join("data", "members.json")

    def __init__(self):
        self.books: Dict[str, Book] = {}
        self.members: Dict[str, Member] = {}
        self.current: Optional[Member] = None
        # 尝试加载数据，若文件缺失会给出友好提示
        self._load_books()
        self._load_members()

    # ---------------- 数据加载/保存 ----------------
    def _load_books(self) -> None:
        if not os.path.exists(self.BOOKS_PATH):
            print(f"警告：未找到书籍数据 {self.BOOKS_PATH}，请确认数据文件存在。")
            return
        with open(self.BOOKS_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
        for item in data:
            # 兼容不同字段名
            bid = item.get("编号") or item.get("book_id")
            title = item.get("标题") or item.get("title")
            author = item.get("作者") or item.get("author") or "未知"
            num = item.get("数量") or item.get("total") or 1
            b = Book(str(bid), str(title), str(author), int(num))
            # 如果 data 中有可用字段则尝试设置
            if "可用" in item:
                try:
                    b._available = int(item.get("可用"))
                except Exception:
                    pass
            self.books[b.book_id] = b
        print(f"已加载 {len(self.books)} 本书。")

    def _load_members(self) -> None:
        if not os.path.exists(self.MEMBERS_PATH):
            print(f"警告：未找到会员数据 {self.MEMBERS_PATH}，请确认数据文件存在。")
            return
        with open(self.MEMBERS_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
        for item in data:
            cid = item.get("卡号") or item.get("card_id")
            name = item.get("姓名") or item.get("name")
            pwd = item.get("密码") or item.get("password")
            if cid is None or name is None or pwd is None:
                continue
            cid = str(cid)
            if cid.startswith("N"):
                member = NormalMember(cid, name, pwd)
            else:
                vip_level = int(item.get("会员等级") or item.get("vip_level") or 0)
                member = VIPMember(cid, name, pwd, vip_level)
            # 恢复借阅记录（若存在）
            borrowed = item.get("借阅") or item.get("borrowed") or []
            member._borrowed = [str(x) for x in borrowed]
            self.members[cid] = member
        print(f"已加载 {len(self.members)} 个会员。")

    def _save_books(self) -> None:
        # 可选：将当前可用数写回 books.json（覆盖原文件）
        try:
            data = [b.to_dict() for b in self.books.values()]
            with open(self.BOOKS_PATH, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print("无法保存书籍数据：", e)

    def _save_members(self) -> None:
        try:
            data = []
            for m in self.members.values():
                data.append(m.to_dict())
            with open(self.MEMBERS_PATH, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print("无法保存会员数据：", e)

    # ---------------- 用户认证 ----------------
    def login(self) -> bool:
        """使用与 07 版本相同的登录流程：无限循环直到登录成功。
        - 直接用 input 获取密码（兼容不支持 getpass 的运行环境）
        - 输入会员卡号后回车即可，无需输入 "q"
        """
        print('\n【登录】')
        while True:
            member_id = input("请输入会员卡号：").strip()
            # 判断会员是否存在
            if member_id not in self.members:
                print("登录失败，会员不存在")
                continue
            password = input("请输入会员密码：")
            member = self.members[member_id]
            if member.check_password(password):
                self.current = member
                print(f"登录成功！欢迎您，{member.name}")
                return True
            else:
                print("登录失败，密码错误")
                continue

    def logout(self) -> None:
        if self.current:
            print(f"{self.current.name} 已登出。")
        self.current = None

    # ----------------- 辅助查询/展示 -----------------
    def list_books(self, top: Optional[int] = None) -> None:
        """列出馆内所有图书（或前 top 本）"""
        books = list(self.books.values())
        if top:
            books = books[:top]
        for b in books:
            print(b)

    def search_books(self, keyword: str) -> List[Book]:
        keyword = keyword.lower().strip()
        res = [b for b in self.books.values() if keyword in b.title.lower() or keyword in b.author.lower() or keyword in b.book_id.lower()]
        return res

    def show_book_info(self, book_id: str) -> None:
        b = self.books.get(book_id)
        if not b:
            print("未找到该图书，请检查编号。")
            return
        print(textwrap.dedent(f"""
        编号: {b.book_id}
        标题: {b.title}
        作者: {b.author}
        馆藏: {b.total_num}
        可借: {b.available()}
        """))

    # ----------------- 借还操作 -----------------
    def borrow_flow(self, book_id: str) -> None:
        if not self.current:
            print("请先登录。")
            return
        b = self.books.get(book_id)
        if not b:
            print("图书编号不存在。")
            return
        self.current.borrow_book(b)

    def return_flow(self, book_id: str) -> None:
        if not self.current:
            print("请先登录。")
            return
        b = self.books.get(book_id)
        if not b:
            print("图书编号不存在。")
            return
        self.current.return_book(b)

    def show_my_borrows(self) -> None:
        if not self.current:
            print("请先登录。")
            return
        ids = self.current.borrowed_list()
        if not ids:
            print("当前没有借阅记录。")
            return
        print(f"{self.current.name} 的借阅列表：")
        for bid in ids:
            b = self.books.get(bid)
            if b:
                print(f" - {b}")
            else:
                print(f" - 编号 {bid} （已下架或无法找到）")

    # ----------------- 主交互循环 -----------------
    def help(self) -> None:
        print(textwrap.dedent("""
        可用命令：
        list                    列出全部图书
        search <关键词>          按标题/作者/编号搜索
        info <book_id>          查看图书详细信息
        borrow <book_id>        借书
        return <book_id>        还书
        my                      查看我的借阅
        logout                  登出当前账号
        save                    保存当前数据到 data/*.json
        quit                    退出程序
        help                    显示本帮助
        """))

    def run(self) -> None:
        """仿造 07 的菜单式交互：登录后直接显示数字菜单供选择。"""
        print("欢迎使用改进版图书管理系统")
        # 先登录（与 07 保持一致，循环直到登录成功）
        if not self.login():
            print("未登录，程序退出。")
            return
        # 菜单循环
        while True:
            print("\n【图书管理系统】")
            print("1. 借阅图书")
            print("2. 归还图书")
            print("3. 查询借阅")
            print("4. 列出图书")
            print("5. 保存并退出")
            choice = input("请选择操作（1-5）：").strip()
            if choice == "1":
                # 显示图书并提示输入编号
                print("\n【图书列表】")
                for b in self.books.values():
                    print(f"编号：{b.book_id}，标题：{b.title}，作者：{b.author}，总数：{b.total_num}，可用数量：{b.available()}")
                book_id = input("请输入要借阅的图书编号：").strip()
                if not book_id:
                    print("未输入编号，返回菜单。")
                    continue
                self.borrow_flow(book_id)
            elif choice == "2":
                # 展示当前会员借阅并还书
                print("\n【当前会员所借的图书】")
                self.show_my_borrows()
                book_id = input("请输入要归还的图书编号：").strip()
                if not book_id:
                    print("未输入编号，返回菜单。")
                    continue
                self.return_flow(book_id)
            elif choice == "3":
                # 查询借阅
                self.show_my_borrows()
            elif choice == "4":
                # 列出全部图书
                print("\n【全部图书】")
                self.list_books()
            elif choice == "5":
                # 保存并退出
                print("正在保存数据并退出...")
                self._save_books()
                self._save_members()
                break
            else:
                print("无效的选项，请输入 1-5 的数字。")


if __name__ == '__main__':
    system = LibrarySystem()
    system.run()