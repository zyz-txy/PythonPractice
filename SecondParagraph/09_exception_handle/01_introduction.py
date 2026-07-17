#异常处理
# try:
#     print("-------------------")
#     print(my_name)
#     print("-------------------")
# except NameError as e:
#     #捕获name error类型异常
#     print("程序运行出错，请联系管理员~，异常信息：",e)
# finally:
#     print("程序结束")
from logging import exception

try:
    print("-------------------")
    #print(myname)
    #print(1/0)
    print("abc"[10])
    print("abc".hello)
    print("-------------------")

#逐项匹配except
except NameError as e:
    #捕获name error类型异常
    print("变量未定义，异常信息：",e)
except ZeroDivisionError as e:
    #捕获zero division error类型异常
    print("零不能做被除数",e)
except IndexError as e:
    #捕获index error类型异常
    print("索引越界",e)
except Exception as e:
    #捕获其他类型异常
    print("程序运行出错，请联系管理员~，异常信息：",e)
finally:
    #无论程序是否正常运行，finally里面的代码都会运行
    print("程序结束，释放资源~")
