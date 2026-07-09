"""
while 条件表达式:
    循环体语句1
    循环体语句2
    ...
"""
#打印十遍“人生苦短，我用Python”
#调试跟踪
i = 1
while i <= 10:
    print(f"第{i}遍：人生苦短，我用Python")
    i += 1
else:
    print(f"循环正常结束，执行完毕")

#1-100之间所有偶数之和
total = 0
i = 1
while i<=100:
    if i % 2 == 0 :
        total += i
    i += 1
else:
    print(f"1-100所有偶数和已累加完毕，和为{total}")

"""
等价于sum()函数
total = sum(range(1,101,2))
参数分别代表：起始，终止，步长
范围取首不取尾
"""