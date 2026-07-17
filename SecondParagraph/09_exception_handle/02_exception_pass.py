#异常传递
#只需从程序入口捕获异常即可

def fun1():
    print("fun1,run")
    fun2()

def fun2():
    print("fun2,run")
    fun3()
def fun3():
    print("fun3,run")
    print(myfun)

if __name__ == "__main__":
    try:
        fun1()
    except Exception as e:
        print("程序运行出错，请联系管理员~，异常信息：",e)
    finally:
        print("程序结束")

