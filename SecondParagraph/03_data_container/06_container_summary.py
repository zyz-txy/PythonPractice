# # 各容器特性
#
# print(f"特性\t\t\t字符串\t\t\t\t列表\t\t\t\t\t元组\t\t\t\t\t集合\t\t\t\t\t字典")
# containers = (("有序性","有序","有序","有序","无序","有序(3.7+)"),
#               ("重复元素","允许","不允许","不可变","不允许","key不允许"),
#               ("可变性","不可变","可变","不可变","可变","可变"),
#               ("索引访问","支持","支持","支持","不支持","不支持"),
#               ("切片操作","支持","支持","支持","不支持","不支持"),
#               ("使用场景","文本处理","有序可重复数据集合","固定数据记录","去重数据记录","键值对存储")
#               )
# for unique,str_,list_,tuple_,set_,dict_ in containers:
#     print(f"{unique}\t\t{str_}\t\t\t\t{list_}\t\t\t\t{tuple_}\t\t\t\t\t{set_}\t\t\t\t{dict_}")

table = """
###########################################菜单################################################
# 1.添加学生信息  2.修改学生信信息 3.删除学生信息 4.查询学生信息 5，列出所有学生 6.统计班级成绩 7.退出系统 #
##############################################################################################
"""
#students = {name:{chinese:100,math:80,english:78},.....}
students = {}
while True:
    print(table)
    option = input("请输入你想进行的操作(1-7)：")
    match option:
        case "1":#添加学生信息
            name = input("请输入学生姓名：")
            if name in students:
                print("学生已存在，请勿重复添加！")
                continue
            else:
                chinese = int(input("请输入学生语文成绩："))
                math = int(input("请输入学生数学成绩："))
                english = int(input("请输入学生英语成绩："))
                students[name] = {"chinese":chinese,"math":math,"english":english}
                print(f"成功添加{name}信息")
        case "2":#修改学生信息
            name = input("请输入学生姓名：")
            if name not in students:
                print("学生不存在，请重新操作！")
                continue

            chinese = int(input("请输入学生语文成绩："))
            math = int(input("请输入学生数学成绩："))
            english = int(input("请输入学生英语成绩："))
            students[name] = {"chinese":chinese,"math":math,"english":english}
            print(f"成功修改{name}信息")
        case "3":#删除学生信息
            name = input("请输入学生姓名：")
            if name not in students:
                print("学生不存在，请重新操作！")
                continue

            del students[name]
            print(f"成功删除{name}信息")
        case "4":#查询学生信息
            name = input("请输入学生姓名：")
            if name not in students:
                print("学生不存在，请重新操作！")
                continue
            info = students[name]
            total = info["chinese"] + info["math"] + info["english"]
            avg = total / 3
            print(f"{name}的成绩单：语文{info['chinese']}，数学{info['math']}，英语{info['english']}")
            print(f"总分：{total}，平均分：{avg:.2f}")
        case "5":#列出所有学生
            for s in students:
                print(s)
        case "6":#统计班级成绩
            if not students:
                print("暂无学生信息！")
                continue
            best_score = max(s["chinese"] + s["math"] + s["english"] for s in students.values())
            names = [n for n, s in students.items() if s["chinese"] + s["math"] + s["english"] == best_score]
            print(f"最高分：{best_score}（{names}）")
        case "7":
            print("成功退出！")
            break
        case _:
            print("操作错误，请重新输入！")