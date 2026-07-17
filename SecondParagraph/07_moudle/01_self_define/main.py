# #导入自定义模块
# import my_fun
# #模块中的代码也会被执行
# #使用模块中的功能
# print(my_fun.PI)
# print(my_fun.NAME)
#
# my_fun.log_separator1()
# my_fun.log_separator2()

# from my_fun import log_separator1,log_separator3,PI,NAME
# print(PI)
# print(NAME)
# log_separator1()
# log_separator3()

from my_fun import *#__all__ = ["log_separator1","log_separator3","PI"]
print(PI)
log_separator1()
log_separator3()

