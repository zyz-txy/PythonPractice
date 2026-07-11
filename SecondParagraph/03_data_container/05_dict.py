#dict字典介绍：
"""
dict字典：无序的，可修改的，键值对存储，键唯一(若重复，后面的值会覆盖前面的值)
(key:value),可根据key查找对应的value
value可以为任何类型，包括列表，元组，字典等
key不能为可变类型，如列表，字典等
"""
#定义字典
dict1 = {"王林":679,"韩立":556,"婉儿":700}
dict2 = {}
dict3 = dict()
"""
字典增删改查操作
1.dict[key] = value:添加键值对到字典中（无就添加，有就修改）
2.dict[key] | dict.get("key"):访问字典中的值
3.dict[key] = value:修改字典中的值
4.dict.pop(key):删除字典中的值，并返回
5.dict.clear():清空字典中的值
6.dict.items():遍历字典中的键值对
7.dict.keys():获取字典中的键
8.dict.values():获取字典中的值
9.dict2 = dict1.copy() #字典的复制
10.dict5 = {**dict3,**dict4} #字典的合并
"""
# print(dict1)
# print(type(dict1))
# #添加键值对到字典中（无就添加，有就修改）
# dict1["许立国"] = 555
# print(f"许立国分数：{dict1['许立国']}")
# #访问字典中的值
# print(dict1["王林"])
# print(dict1.get("韩立"))
# #修改字典中的值
# dict1["王林"] = 670
# print(dict1["王林"])
# dict1["韩立"] = 558
# print(dict1["韩立"])
#
# print(dict1)
# #添加键值对到字典中（无就添加，有就修改）
# dict1["婉儿"] = 700
# print(dict1)
# #删除字典中的值，并返回
# dict1.pop("王林")
# print(dict1)
# del dict1["韩立"]
# print(dict1)
# #字典的遍历
# for key in dict1:
#     print(key,dict1[key])
# for key,value in dict1.items():
#     print(key,value)
# #字典的长度
# print(len(dict1))
# #字典的键
# print(dict1.keys())
# #字典的值
# print(dict1.values())
# #字典的键值对
# print(dict1.items())
# #字典的复制
# dict2 = dict1.copy()
# print(dict2)
# #清空字典中的值
# dict1.clear()
# print(dict1)
# #字典的合并
# dict3 = {"name":"张三","age":18,"sex":"男"}
# dict4 = {"name":"李四","age":20,"sex":"女"}
# dict5 = {**dict3,**dict4}#合并机制:如果键存在则修改，不存在则添加
# print(dict5)
# #字典的键存在则修改，不存在则添加
# dict5.update({"name":"张三","age":19,"sex":"男"})
# print(dict5)
# #字典的键存在则修改，不存在则添加
# dict5.update({"name":"李四","age":19,"sex":"女"})
# print(dict5)

#--------------------------------------------------------------------------------------------------------------
"""
案例:
开发一个购物车管理系统,实现商品信息的添加、修改、删除、查询和统计功能。系统使用嵌套字典结构存储商品数据,通过控制台菜单与用户交互。
具体功能如下:
1. 添加购物车: 用户根据提示录入商品名称、以及该商品的价格、数量,保存该商品信息到购物车。
2. 修改购物车: 要求用户输入要修改的购物车商品名称,然后再提示输入该商品的价格、数量,输入完成后修改该商品信息。
3. 删除购物车: 要求用户输入要删除的购物车商品名称,根据名称删除购物车中的商品。
4. 查询购物车: 将购物车中的商品信息展示出来,格式为: "商品名称: xxx, 商品价格: xxx, 商品数量: xxx"。
5. 退出购物车
结构: shopping_cart = {"Meta80": {"price": 6999, "num": 2}, "鼠标": {...}}
"""

shopping_cart = {}
menu = """
########## 购物车管理系统 ##########
#         1.  添加购物车          #
#         2.  修改购物车          #
#         3.  删除购物车          #
#         4.  查询购物车          #
#         5.  退出购物车          #
##################################
"""
print("欢迎使用购物车管理系统")

#主程序
while True:
    print(menu)
    choice = input("请输入你的选择(1-5)：")
    match choice:
        case "1":
            name = input("请输入商品名称：")
            price = float(input("请输入商品价格："))
            num = int(input("请输入商品数量："))
            if name in shopping_cart:
                print("商品已存在，请重新输入!")
            else:
                shopping_cart[name] = {"price":price,"num":num}
                print("商品添加成功！")
        case "2":
            name = input("请输入要修改的购物车商品名称：")
            if name in shopping_cart:
                price = float(input("请输入商品价格："))
                num = int(input("请输入商品数量："))
                shopping_cart[name] = {"price":price,"num":num}
                print("商品修改成功！")
            else:
                print("商品不存在，请重新输入!")
            pass
        case "3":
            name = input("请输入要删除的购物车商品名称：")
            if name not in shopping_cart:
                print("商品不存在，请重新输入!")
            else:
                del shopping_cart[name]
                print("商品删除成功！")
        case "4":
            for name in shopping_cart.keys():
                info = shopping_cart[name]
                print(f"商品名称: {name}, 商品价格: {info["price"]}, 商品数量: {info['num']}")
                #单引号双引号都可以引用字符串，单引号更好区分
        case "5":
            print("Bye ~")
            break
        case _:
            print("输入有误，请重新输入!")

















