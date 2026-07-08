#双引号定义
s1 = ("\tIt's a example\n\tyes")#单引号，双引号定义的字符串不能直接换行
#单引号定义
s2 = 'It\'s \t a \t example'#转义字符\t,\n,\\,\',\"
s3 = "\"example\""
s4 = ("""
官方
      支持换行""")#三引号，会将每一行原封不动输出
#一般都用双引号不用单引号表示字符串

print(s1)
print(s2)
print(s3)
print(s4)

#字符串拼接
name = "txy"
age = 19#拼接时要转换
hobby = "programing"
print(name + "今年" + str(age) + "岁" +"爱好" + str(hobby))