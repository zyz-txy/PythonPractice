import re

s1 = "17378962680是我的一个手机号，我的另一个手机号是17742496963，QQ号是1876195621和1736483618374"
s2 = "我的一个手机号是17378962680，我的另一个手机号是17742496963，QQ号是1876195621和1736483618374"

#match - 从字符串开头匹配（匹配第一个匹配项），返回match对象
result = re.match(r"1[3-9]\d{9}",s1)#如果是s2对象匹配不到，会返回None
print(result.group())
print(result.span())
print(result.start())
print(result.end())

#search - 从字符串任意位置开始，搜索所有匹配项，返回match对象
result = re.search(r"1[3-9]\d{9}",s2)#r是raw string，表示原始字符串，不进行转义
print(result.group())
print(result.span())
print(result.start())
print(result.end())

#findall - 从任意位置开始，搜索所有匹配项，返回列表
result = re.findall(r"1[3-9]\d{9}",s2)
print(result)


