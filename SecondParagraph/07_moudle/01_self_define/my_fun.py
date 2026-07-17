#常量:名称全大写（规范）
from unittest import main

PI = 3.1415926
NAME = "txy"

def log_separator1():
    print("- " * 30)

def log_separator2():
    print("+ " * 30)

def log_separator3():
    print("# " * 30)

def log_separator4():
    print("* " * 30)

#__name__   :python中的内置变量（直接运行这个模块，__name__的值为__main__）
#当该模块被导入时，__name__的值就是该模块名称
#执行当前文件则会执行如下代码；如果被当做模块导入则不执行
if __name__ == '__main__':#快捷方式main
    log_separator1()

#__all__,如果定义了all，则用*导入时则导入的是all的列表功能
__all__ = ["log_separator1","log_separator3","PI"]

