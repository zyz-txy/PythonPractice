#for 轮询遍历机制
"""
for 元素 in 待处理数据集:
    循环体代码(对元素进行处理)
else:
    循环结束时,执行代码
"""

#遍历字符串
# msg = input("请输入需要遍历的字符串：")
#
# for i in msg:
#     print(f"元素：{i}")
# else:
#     print(f"循环结束时打印")

#range
"""
range(end)默认0开始到end不包含end
range(strat,end)取头不取尾
range(strat,end,step) step为步长,取头不取尾
"""

#计算1-100所有奇数之和
total = 0
for i in range(1,101,2):
    if i % 2 != 0:
        total += i

print(f"1-100之间的奇数和为：{total}")

#计算100-500之间所有2的倍数的数字之和
total = 0
for i in range(100,501):
    if i % 3 == 0:
        total += i
print(f"100-500之间所有3的整数和为：{total}")