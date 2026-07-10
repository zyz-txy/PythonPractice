#列表定义
"""
列表名称  = [元素1.元素2.....]
可存储不同类型，一般相同
有序，元素可重复，可修改
正反向索引：正从0，反从-1，通过[index]取出元素
"""
#---------------------------------------------

s = [56,True,None,"hello"]#中括号
#print(type(s))  -- str

print(s[0])#正向索引
print(s[-4])#反向索引
s[0] = 50
print(s[0])
print(s)

#print(s[10])#索引越界报错

del s[0]#删除元素
print(s,s[0])#s[0]会自动被替换

#遍历
for i in s:
    print(i)

#----------------------------------------------

#列表-切片
"""
序列数据[开始索引:结束索引:步长]取头不取尾，步长默认1
       [0:5:2]
       取出s[0],s[2],s[4] 
"""
s = ["A","B","C","D","E","F","G","H","I","J"]
print(s)
print(s[0:5:1])
print(s[:5])#第一个冒号不能省略
print(type(s[0:5:1]))#无意义
print(s[0:5:2])
print(s[0:-2:])#逆向

#--------------------------------------------------------

#列表常见方法
"""  调用方式：对象.(参数)
append() 在列表尾部追加元素
insert() 在指定索引之前插入元素
remove() 移除列表中第一个匹配到的值
pop() 删除列表中第一个元素,会返回删除的元素 a = s.pop(2)
sort() 对列表进行排序（类型一致）
reverse() 反转列表元素

"""
s = [56,90,88,65,90,100,209,72,145]
print(s)
#追加
s.append(188)
print(s)
#插入
s.insert(2,80)
print(s)
#移除
s.remove(90)
print(s)
#取出
e = s.pop(1)
print(e)
print(s)
#排序
s.sort()
print(s)
#反转
s.reverse()
print(s)
#清空
s.clear()
print(s)

#----------------------------------------

#案例1

s = []
total = 0
print("输入十个数字")
for i in range(1,11):#取头不取尾
    num = float(input(f"第{i}个数字："))
    total += num
    s.append(num)
s.sort()
print(f"最大值为：{s[0]}")
print(f"最小值为：{s[-1]}")
print(f"平均值为：{total/10}")
#sum求和   len求列表长度
print(f"平均值为：{sum(s)/len(s)}")

#--------------------------------------

#案例2

# list1 = [19,23,54,64,875,20,109,232,123,54]
# list2 = [55,80,72,35,60,123,54,29,91]
# #合并列表
# for i in list2:
#     list1.append(i)
# list1.sort()#排序方便对比观察
# print(list1)
# # #去重
# new_list = []
# for i in list1:
#     #使用 in 判断元素是否存在于列表中
#     if i not in new_list:#取反
#         new_list.append(i)
# new_list.sort()
# print(new_list)

#简化案例2---------------------------------------------

list1 = [19,23,54,64,875,20,109,232,123,54]
list2 = [55,80,72,35,60,123,54,29,91]
#合并列表
# num_list = [*list1,*list2]  #解包,组包操作 等价于+

num_list = list1 + list2
num_list.sort()#排序方便对比观察
print(f"合并后的初始列表：{num_list}")
#去重
new_list = []
for i in num_list:
    #使用 in 判断元素是否存在于列表中
    if i not in new_list:#取反
        new_list.append(i)
new_list.sort()
print(f"去重后的列表{new_list}")

#---------------------------------------------

#案例3
#列表推导式：快速生成列表
"""
[要插入的值 for i in 序列/列表 if 条件]
"""
num_list2 = [i**2 for i in range(1,21)]
print(num_list2)

num_list1 = [12,20,45,77,80,92,33,57,32,54,78,52]
#提取出列表中所有偶数并将其平方插入到列表中
new_list1 = [i**2 for i in num_list1 if i%2==0]
print(new_list1)

