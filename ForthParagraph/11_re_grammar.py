import re

s1 = "18809090000是我的手机号，188开头的，以00结尾的；我的另一个手机号是15500008888，两个QQ号分别是1259989092和13809091293821，邮箱为python666@163.com，请给我发邮件。"

# 正则表达式
# print(re.findall(r"188.*", s1))  # * 匹配任何个
# print(re.findall(r"188.?", s1))  # ? 匹配0个或者1个（最多出现一次）
# print(re.findall(r"188.+", s1))  # + 匹配1个或者多个（最少出现一次）

# print(re.findall(r"188\d\d{8}", s1))  # {8} 匹配8个
# print(re.findall(r"155\d\d{6,10}", s1))  # {6,10} 匹配6到10个
# print(re.findall(r"155\d{6,}", s1))  # {6,} 匹配6个或者更多

# print(re.findall(r"1[38]\d{8}", s1))  # [38] 匹配3或者8
# print(re.findall(r"1[^38]\d{8}", s1))  # [^38] 匹配非3或者8
# print(re.findall(r"1[3-9]\d{8}", s1))  # [3-9] 匹配3到9（范围）
# print(re.findall(r"^1[3-9]\d{9}", s1))  # ^ 匹配开头
# print(re.findall(r"^1[3-9]\d{9}$", s1))  # $ 匹配结尾

print(re.findall(r"\w+@\w+\.\w+", s1))  # \w 匹配任何单词字符(a-z、A-Z、0-9、_、其它语言字符)
# print(re.findall(r"\w+@\w+\.\w+", s1, re.ASCII))  # \w 匹配任何单词字符(a-z、A-Z、0-9、_)

# 注意
s2 = "现在的时间是2026-07-25 13:58:25，今天的天气还可以，气温是28度 "
print(re.findall(r"\d{4}-\d{2}-\d{2}", s2))
print(re.findall(r"(\d{4})-(\d{2})-(\d{2})", s2))
