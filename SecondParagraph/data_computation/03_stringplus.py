#字符串格式化1->%s占位符

name = "txy"
age = 19
hobby = "programming"
print("大家好，我是%s,我今年%s岁，爱好是%s"%(name,age,hobby))
#会将%后转化为string

#字符串格式化2->f"内容{变量/表达式}"-->推荐

print(f"大家好，我是{name},我今年{age}岁，爱好是{hobby}")
#拼接,推荐
print(f"{name},{age}{hobby}")