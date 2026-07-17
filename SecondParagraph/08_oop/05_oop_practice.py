class Goods:
    def __init__(self,name,price,num):
        self.name = name
        self.price = price
        self.num = num

    def update_goods(self,price=None,num=None):
        if price is not None:
            self.price = price
        if num is not None:
            self.num = num

    def __str__(self):
        return f"{self.name}的价格为：{self.price}，数量为： {self.num}。"

class ShoppingCart:
    system_name = "购物车"
    system_version = "1.0"
    def __init__(self):
        self.good_lists = []

    def add_goods(self):
        name = input("请输入商品名称：")
        if name in self.good_lists:
            print("商品已存在")
            return
        else:
            price = float(input("请输入商品价格："))
            num = int(input("请输入商品数量："))
            goods = Goods(name,price,num)
            self.good_lists.append(goods)

    def update_shopping_cart(self):
        print(f"当前购物车中的商品有：{[goods.name for goods in self.good_lists]}")
        name = input("请输入商品名称：")
        for goods in self.good_lists:
            if goods.name == name:
                print(f"当前商品信息：{goods}")
                new_price = float(input("请输入新的商品价格："))
                new_num = int(input("请输入新的商品数量："))
                goods.update_goods(new_price,new_num)
                print(f"修改后的商品信息：{goods}")
                break
        else:
            print("商品不存在")

    def delete_goods(self):
        name = input("请输入商品名称：")
        for goods in self.good_lists:
            if goods.name == name:
                self.good_lists.remove(goods)
                print(f"已删除商品：{goods}")
                break
        else:
            print("商品不存在")

    def list_goods(self):
        for goods in self.good_lists:
            print(goods)

    def run(self):
        print(
            f"欢迎使用{self.system_name}系统，版本号：{self.system_version}"
            "\n1. 添加商品\n2. 修改商品\n3. 删除商品\n4. 列出商品\n5. 退出系统"
        )
        while True:
            print("1. 添加商品\t2. 修改商品\t3. 删除商品\t4. 列出商品\t5. 退出系统")
            choice = int(input("请输入你的选择（1-5）："))
            match choice:
                case 1:
                    self.add_goods()
                case 2:
                    self.update_shopping_cart()
                case 3:
                    self.delete_goods()
                case 4:
                    self.list_goods()
                case 5:
                    print("退出系统")
                    break
                case _:
                    print("输入错误")

if __name__ == "__main__":
    cart = ShoppingCart()
    cart.run()