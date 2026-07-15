#导入模块语法
"""
import module_name   调用方式 module_name.function_name()
import module_name as new_name  调用方式 new_name.function_name()
from module_name import function_name  调用方式 function_name()
from module_name import function_name as new_name  调用方式 new_name()
from module_name import *  调用方式 function_name()
"""

# import random as rd
# for i in range(100):
#     print(rd.randint(1,100))

from random import randint as rint
for i in range(100):
    print(rint(1,100))
print("-------------------------")
from random import *
print(randint(1,100))


