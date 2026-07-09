#if 要判断的条件：（判断语句结果必须为bool：True执行，False不执行）
#     条件成立时，要执行的操作

score = 695
if score > 680:
    print("欢迎你，来清华读书")
    print("你将开启精彩的大学生活")#Python依靠缩进描述层级 /t
print("---------------")

#正确账号密码
r_account = "1888"
r_pwd = "8888"
#上面int下面输入就要转化，上面str输入就不转，一般还是str，用户名会有字母
account = input("输入用户名：")
pwd = input("输入密码：")

#if语句不写括号()，注意末尾冒号:
if account == r_account and pwd == r_pwd:
    print("登录成功")
    print("进入到b站首页")

if account != r_account or pwd != r_pwd:
    print("登录失败！")
    print("账号或密码错误！")