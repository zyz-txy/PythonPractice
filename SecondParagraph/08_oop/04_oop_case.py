class Student:
    def __init__(self,name,chinese,math,engliah):
        self.name = name
        self.chinese = chinese
        self.math = math
        self.english = engliah

    def __str__(self):
        return f"姓名：{self.name} | 语文： {self.chinese} | 数学：{self.math} | 英语：{self.english} | 总分：{self.chinese+self.math+self.english}"

    #修改学生成绩
    def update_score(self,chinese=None,math=None,english=None):#添加默认值，可以只修改某一个成绩
        if chinese is not None:
            self.chinese = chinese
        if math is not None:
            self.math = math
        if english is not None:
            self.english = english

class EduManagement:
    system_version = "1.0"
    system_name = "教务管理系统"

    def __init__(self):
        self.student_list = []#列表里面记录在校学生成绩信息

    #添加学生成绩
    def add_student(self):
        name = input("请输入学生姓名：")
        #不能重复添加
        if name in self.student_list:
            print("该学生已存在，添加失败！")
            return
        chinese = int(input("请输入学生语文成绩："))
        math = int(input("请输入学生数学成绩："))
        english = int(input("请输入学生英语成绩："))

        #判断分数合理性
        if chinese < 0 or chinese > 100 or math < 0 or math > 100 or english < 0 or english > 100:
            print("输入分数不合理，请重新输入！")
            return

        stu = Student(name,chinese,math,english)
        self.student_list.append(stu)
        print("添加成功！")
    #修改学生成绩
    def update_student(self):
        name = input("请输入学生姓名：")
        for s in self.student_list:
            if s.name == name:
                print(f"当前成绩：{s}")
                chinese = int(input("请输入修改后的语文成绩："))
                math = int(input("请输入修改后的数学成绩："))
                english = int(input("请输入修改后的英语成绩："))

                if 0<= chinese <= 100 and 0<= math <= 100 and 0<= english <= 100:
                    s.update_score(chinese,math,english)
                    print("修改成功！")
                    print(f"当前成绩：{s}")
                else:
                    print("输入分数不合理，请重新输入！")
                    return
            else:
                print("该学生不存在，修改失败！")
            return
    #删除学生成绩
    def delete_student(self):
        name = input("请输入学生姓名：")
        for s in self.student_list:
            if s.name == name:
                self.student_list.remove(s)
                print("删除成功！")
                return
            else:
                print("该学生不存在，删除失败！")
    #查询指定学生成绩
    def query_student(self):
        name = input("请输入学生姓名：")
        for s in self.student_list:
            if s.name == name:
                print(f"当前学生信息：{s}")
                return
        print("该学生不存在，查询失败！")
    #显示全部学生成绩
    def list_student(self):
        for s in self.student_list:
            print(s)

    #运行系统
    def run(self):
        print("欢迎使用",self.system_name,"系统，版本号：",self.system_version)
        while True:
            print("1. 添加学生成绩")
            print("2. 修改学生成绩")
            print("3. 删除学生成绩")
            print("4. 查询学生成绩")
            print("5. 显示全部学生成绩")
            print("6. 退出系统")
            choice = input("请输入你的选择（1-6）：")
            #或者使用match case1
            if choice == "1":
                self.add_student()
            elif choice == "2":
                self.update_student()
            elif choice == "3":
                self.delete_student()
            elif choice == "4":
                self.query_student()
            elif choice == "5":
                self.list_student()
            elif choice == "6":
                print("感谢使用",self.system_name,"系统，再见！")
                break
            else:
                print("输入不合理，请重新输入！")

if __name__ =="__main__":
    edumgr = EduManagement()
    edumgr.run()
