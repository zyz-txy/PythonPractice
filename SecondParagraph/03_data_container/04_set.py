#set集合:自动去重，无序的（不支持索引访问），可修改
"""
s1 = {"c", "a", "b", "c"}}
s2 = set() : 定义空集合
"""

s1 = {9,5,2,64,3,10,6,8,3,5}
print(s1)
print(type(s1))
# #定义空集合
s2  = {}# ---- X
print(type(s2))
s2 = set()
print(type(s2))

#--------------------------------------------------

"""
常用方法
add()：添加元素到集合中
remove()：移除集合中的指定元素
pop()：随机移除并返回集合中的一个元素
clear()：清空集合
difference()：返回两个集合的差集（包含在第一个集合但不包含在第二个集合的元素）
union()：返回两个集合的并集
intersection()：返回两个集合的交集
"""
s1 = {1,2,3,400,5}
s1.add(8)
print(s1)
s1.remove(3)
print(s1)
s1.pop()
print(s1)
s1.clear()
print(s1)
s1 = {1,2,3,400,5}
s2 = {4,5,6,7,8}
print(s1.difference(s2))
print(s2.difference(s1))
print(s1.union(s2))
print(s2.union(s1))
print(s1.intersection(s2))
print(s2.intersection(s1))

#--------------------------------------------------------

#案例

#选修足球的学生名单
soccer = {"张三", "李四", "赵六", "孙七", "周八", "吴九", "郑十"}
basketball = {"张三", "李四", "王五", "赵六", "孙七", "周八", "吴九", "郑十"}
french = {"张三", "李四", "王五", "赵六", "周八", "吴九", "郑十"}
art = {"张三", "李四", "王五", "赵六", "孙七", "周八", "吴九"}
#1 同时选修法语和艺术的学生
#法一
print(f"同时选修两门课的学生是{french.intersection(art)}")
#法二：&运算符表示交集
print(f"同时选修两门课的学生是{french & art}")
#2 同时选修四门课的学生
print(f"同时选修四门课的学生是{soccer.intersection(basketball).intersection(french).intersection(art)}")
print(f"同时选修四门课的学生是{soccer & basketball & french & art}")
#3 找出选修了足球但没选修篮球的学生
print(f"选修了足球但没选修篮球的学生是{soccer.difference(basketball)}")
#法二：差运算符表示差集
print(f"选修了足球但没选修篮球的学生是{soccer - basketball}")#“-”运算符表示差集
#法三：列表推导式{要添加的元素 for s in set if 条件} ！！！
print(f"选修了足球但没有选修篮球的学生是{[s for s in set(soccer) if s not in basketball]}")
#4 统计每一个学生选修的课程数量
all_set = soccer | basketball | french | art#整个学生列表
all_list = [*soccer,*basketball,*french,*art]
for s in all_set:
    print(f"{s}选修了{all_list.count(s)}课程")







