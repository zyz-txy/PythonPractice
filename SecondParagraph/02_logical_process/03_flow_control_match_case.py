#结构模式匹配match...case 适用于等值匹配，多匹配
"""
match exp:
    case "1":
        pass
    case "2":
        pass
    case "3":
    ......
    case _:(中间有空格)
        pass
"""

day = input("请输入今天星期几（1-7）：")
#match能够匹配字符串，所以不用类型转换！！

match day:#调试！
    case "1":
        print(f"吃草！")
    case "2":
        pass
    case "3":
        pass
    case "4":
        pass
    case "5":
        pass
    case "6" | "7":
        print("周末,睡觉")
    case _:
        print("输入有误！不要逃避！")

#练习：简易计算器
num1 = float(input("请输入第一个数："))
num2 = float(input("请输入第二个数："))
operator = input("请输入运算符（+ - * / ）：")

match operator:
    case "+":
        print(f"{num1} + {num2} = { num1 +num2 }")
    case "-":
        print(f"{num1} - {num2} = {num1 - num2}")
    case "*":
        print(f"{num1} * {num2} = {num1 * num2}")
    case "/":
        if num2 != 0:
            print(f"{num1} / {num2}")
        else:
            print(f"分母不能为0！想啥呢！")
    case _ :
        print(f"输入有误！操作不支持！")

#简单游戏指令系统
motion = input("请输入移动指令：")

match motion:
    case "上" | "w" | "W":
        print(f"角色已向上移动！")
    case "下":
        pass
    case "左" | "a" | "A":
        print(f"角色已向左移动！")
    case "右":
        pass
    case "跳" | "/" | " ":
        print(f"角色跳跃！")
    case "攻击" | "j" | "J":
        print(f"角色发动攻击！")
    case "esc" | "ESC":
        print(f"退出游戏！！")
    case _ :
        print(f"指令错误")