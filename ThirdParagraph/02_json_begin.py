import json

#写入json数据文件
user = {
    "name" : "txy",
    "age" : 19,
    "gender" : "男",
    "hobbies" : ["coding","gaming"]
}

with open("resources/user.json","w",encoding = "utf-8") as f1:
    json.dump(user,f1,ensure_ascii = False,indent=2)
    #对象和要写入的文件，参数解决输入有中文的情况和缩进
    #ensure_ascii默认为True，非ascll码会转义，False即保留原样输出

#读取json文件
with open("resources/user.json","r",encoding = "utf-8") as f2:
    user = json.load(f2)
    print(user)
    print(type(user))
    print(user["name"])
    print(user["age"])
    print(user["gender"])
    print(user["hobbies"])
