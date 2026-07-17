#元组 - 记录的信息只能查询，元素可重复，不可修改
"""
元组名称 = (元素1,元素2，元素3....)
定义空元组：元组名称 = ()或元组名称 = tuple()
方法
count()：统计某个元素在元组中的次数
index()：查找某个元素在元组中的索引位置（第一次出现）
"""
t1 = (5,7,9,3,1,2,3)
print(type(t1))
print(t1[0],t1[-1])
#t1[0] = 8 --- X
t2 = ()
t3 = tuple()
#切片
print(t1)
print(t1[0:5:1]," ",t1[-1:2:-1])
#count
print(t1.count(3))
#index
print(t1.index(3))

# #注意点定义单个元素的元组在元素之后加逗号：(100,),不然会被认为是int
t4 = (100,)
print(type(t4))
print(t4)
t5 = (100)
print(type(t5))
print(t5)

#---------------------------------------------------------

#组包：将多个值合到一个容器（元组，列表中）
#解包：将容器（元组，列表）解开成独立的元素，分别赋值给多个变量
#组包
t6 =  5,7,9,1  #可以不写括号
t7 = (5,7,9,1)
#基础解包：一个元素一个变量
a ,b , c , d = t6
print(a,b,c,d)
#(*)扩展解包:收集剩余的所有元素，多个元素生成的是列表，以便于对其进行进一步处理
x , *y , z = t7
print(x,y,z)
s, *o  = t7
print(s,o)
*o, e = t7
print(o,e)

#----------------------------------------------------------

# 交换三个变量的值

a = 100
b = 200
c = 300
#组包
t = a , b , c
#解包
c , a , b = t
print(a,b,c)

#-----------------------------------------------------

#案例-----成绩分析：学号，姓名，语文，数学，英语

students = (
    ("S001","封尊",85,92,78),
    ("S002","婉儿",92,88,95),
    ("S003","小许子",75,69,82),
    ("S004","遁天",66,59,72)
)

#计算每个学生总分，平均分并输出 ---->{avg:.1f}-->保留一位小数
#法一：
for s in students:
    total = 0
    avg = 0
    for o in s[2:]:#切片从第三个开始遍历
        total += o
    avg = total / 3

    print(f"{s[1]}的总分为{total}\t,平均分为{avg:.1f}\t")
    if avg > 90:
        print(f"{s[1]}的成绩优异！")
print("=====================================================")
#法二：
print(f"学号\t\t姓名\t\t 语文\t数学\t\t英语\t\t总分\t\t平均分")
for Id,name,chinese,math,english in students:
    total = chinese + math + english
    avg = total / 3
    print(f"{Id}\t{name} \t {chinese}\t\t{math}\t\t{english}\t\t{total}\t\t{avg:.1f}")
#统计各科最高分，最低分，平均分
chinese_total = [s[2] for s in students]
math_total = [s[3] for s in students]
english_total = [s[4] for s in students]
print(f"语文最低分：{min(chinese_total)},最高分：{max(chinese_total)}")
print(f"数学最低分：{min(math_total)},最高分：{max(math_total)}")
print(f"英语最低分：{min(english_total)},最高分：{max(english_total)}")