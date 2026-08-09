#图书管理系统

from abc import ABC, abstractmethod
import json

#图书类
class Book:

    def __init__(self,book_id,title,author,total_num):
        self.book_id = book_id      # 图书编号
        self.title = title          # 图书名称
        self.author = author        # 作者
        self.total_num = total_num  # 馆藏数量
        self.__available_num = total_num # 可借数量

    def borrow_book(self):  #借书
        if self.__available_num >= 0:
            self.__available_num -= 1
            return True
        else:
            return False

    def return_book(self): #还书
        self.__available_num += 1

    def get_available_num(self): #获取书籍可用数量
        return self.__available_num

#抽象类：智能被继承，不能被直接实例化的类，作用：规定子类必须实现某些方法，遵循统一的代码规范
#python中的抽象类，需要继承abc模块中的ABC类 --> ABC:Abstract Base Class 抽象基类
#会员类
class Member( ABC):

    def __init__(self,member_id,name,password):
        self.member_id = member_id # 会员编号
        self.name = name           # 会员名称
        self.__password = password # 密码
        self.__borrowed_books = [] # 借阅的图书

    def borrow_book(self,book: Book): #借阅书籍
        #判断当前会员借阅数量是否到达最大限制
        if len(self.__borrowed_books) >= self.get_max_books():
            print("借阅失败，当前借阅数量已达到最大限制")
            return False

        #判断书记是否可以借阅
        if book.borrow_book():
            self.__borrowed_books.append(book)
            print(f"{self.name}已成功借阅《{book.title}》")
            return True
        else:
            print(f"借阅失败，图书《{book.title}》已被借完")
            return False

    def return_book(self,book: Book): #还书
        if book in self.__borrowed_books:
            book.return_book
            self.__borrowed_books.remove(book)
            print(f"{self.name}已成功归还《{book.title}》")
        else:
            print(f"还书失败，您没有借阅《{book.title}》")

    #获取会员密码
    def get_password(self):
        return self.__password

    #获取会员所借书籍
    def get_borrowed_books(self):
        return self.__borrowed_books

    # 获取会员最大借阅数量（在子类中实现）
    @abstractmethod #装饰器，用于检查抽象方法是否被实现
    def get_max_books(self) -> int:
        pass

#普通会员类
class NormalMemeber(Member):
    def get_max_books(self) -> int:
        return 3

#VIP会员类
class VIPMember(Member):

    def __init__(self,member_id,name,password,vip_level):
        super().__init__(member_id,name,password)
        self.vip_level = vip_level #会员等级

    def get_max_books(self) -> int:
        return 6 + self.vip_level

#图书管理系统
class LibrarySystem:
    def __init__(self):
        self.books = {} #书籍列表 --> {"AI001":Book对象,...}
        self.members = {} #会员列表 --> {"V001":Member对象,...}
        self.current_member: Menber|None = None
        #加载数据（书籍，会员）
        self.load_books_data()
        self.load_members_data()

    #初始化图书数据
    def load_books_data(self):
        #加载data/books.json
        with open("data/books.json","r",encoding="utf-8") as f:
            books_data = json.load(f)
            for book in books_data:
                self.books[book['编号']] = Book(book['编号'],book['标题'],book['作者'],book['数量'])
            print("加载书籍数据成功")

    #初始化会员数据
    def load_members_data(self):
        # 加载data/members.json
        with open("data/members.json", "r", encoding="utf-8") as f:
            members_data = json.load(f)
            for member in members_data:
                if member['卡号'].startswith('N'):
                    self.members[member['卡号']] = NormalMemeber(member['卡号'],member['姓名'],member['密码'])
                elif member['卡号'].startswith('V'):
                    self.members[member['卡号']] = VIPMember(member['卡号'],member['姓名'],member['密码'],member['会员等级'])
            print("加载会员数据成功")

    #登录
    def login(self):
        while True:
            print("\n【登录】")

            member_id = input("请输入会员卡号：")
            # 判断会员是否存在
            if member_id not in self.members:
                print("登录失败，会员不存在")
                continue

            password = input("请输入会员密码：")
            # 判断密码是否正确
            member = self.members[member_id]
            if member.get_password() != password:
                print("登录失败，密码错误")
                continue

            self.current_member = member
            print(f"登录成功！欢迎您，{member.name}")
            return True

    #借阅图书方法
    def borrow_book(self):
        #展示当前图书馆的图书列表
        for book in self.books.values():
            print(f"编号：{book.book_id}，标题：{book.title}，作者：{book.author}，总数：{book.total_num}，可用数量：{book.get_available_num()}")

        #获取用户输入的图书编号，执行借阅图书
        book_id = input("请输入要借阅的图书编号：")
        if book_id not in self.books:
            print("借阅失败，图书不存在")
            return

        self.current_member.borrow_book(self.books[book_id])

    #归还图书方法
    def return_book(self):
        #展示当前会员所借的图书列表
        print("【当前会员所借的图书】")
        borrowed_books = self.current_member.get_borrowed_books()
        for book in borrowed_books:
            print(f"编号：{book.book_id}，标题：{book.title}")

        #获取用户输入的图书编号，执行归还图书
        book_id = input("请输入要归还的图书编号：")
        if book_id not in self.books:
            print("归还失败，图书不存在")
            return

        self.current_member.return_book(self.books[book_id])

    #查询借阅
    def show_borrowed_books(self):
        borrowed_books = self.current_member.get_borrowed_books()
        if len(borrowed_books) > 0:
            print("【当前会员所借的图书】")
            for book in borrowed_books:
                print(f"编号：{book.book_id}，标题：{book.title}")
        else:
            print("当前会员没有借阅图书")\


    def run(self):
        if self.login():
            while True:
                print("\n【图书管理系统】")
                print("1.借阅图书")
                print("2.归还图书")
                print("3.查询借阅")
                print("4.退出系统")
                choice = input("请选择操作（1-4）：")
                match choice:
                    case "1":
                        self.borrow_book()
                    case "2":
                        self.return_book()
                    case "3":
                        self.show_borrowed_books()
                    case "4":
                        print("退出系统,Bye~")
                        break
                    case _:
                        print("无效的选项，请重新选择！")

if __name__ == '__main__':
    ls = LibrarySystem()
    ls.run()