#使用模块需要import导入
import random
names = ["wanglin","limuwan"
         ,"xuliguo"]
print(random.choice(names))

#提高代码复用性，降低开发门槛，避免命名冲突
#模块是Python代码的组织形式，可以将代码组织成模块，然后在其他代码中导入和使用
#模块可以包含函数，类，变量等
#模块的命名空间是模块名加点加函数名或变量名，例如：random.choice
