# #导入模块
# import utils.my_fun
# utils.my_fun.log_separator1()
# utils.my_fun.log_separator2()

#导入包下部分模块
# from utils import my_fun
# my_fun.log_separator3()
# my_fun.log_separator4()

#如果要通过*导入所有模块，需要init里面添加all
#导入包下所有模块
from utils import *
my_fun.log_separator1()
my_fun.log_separator2()
print(my_var.NAME)
print(my_var.PI)

#导入模块中具体功能
# from utils.my_fun import log_separator1, log_separator2
# log_separator1()
# log_separator2()

#导入指定模块下所有功能
from utils.my_fun import *
log_separator3()
log_separator4()


#相对路径：从当前文件所在目录开始查找
#也可通过绝对路径查找，从项目的根目录开始查找
