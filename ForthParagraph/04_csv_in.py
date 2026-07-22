#csv格式文件操作
#方法一：文件操作原始方式
#写
with open("csv_data/01.csv","w",encoding = "utf-8") as f:
    f.write("姓名,年龄,性别,爱好\n")#写入表头
    f.write("小王,18,男,football\n")#写入数据,一一对应
    f.write("小刘,19,女,Python\n")#写入数据
    f.write("小明,19,男,C++\n")#写入数据
    f.write("小李,18,男,Go\n")#写入数据
#读
with open("csv_data/01.csv","r",encoding = "utf-8") as f:
    for line in f:
        print(line.strip())

#csv操作 - 方式二：csv
import csv
#写
#newline：如何处理换行，""表示不处理换行，"\n"表示处理换行
with open("csv_data/02.csv","w",encoding = "utf-8", newline = "") as f:
    writer = csv.DictWriter(f,fieldnames=["姓名","年龄","性别","爱好"])
    writer.writeheader()#写入表头
    #写入数据：字典格式
    writer.writerow({"姓名":"小王","年龄":18,"性别":"男","爱好":"java"})
    writer.writerow({"姓名":"小刘","年龄":19,"性别":"女","爱好":"Python"})
    writer.writerow({"姓名":"小明","年龄":19,"性别":"男","爱好":"C++"})
    writer.writerow({"姓名":"小李","年龄":18,"性别":"男","爱好":"Go"})
#读
with open("csv_data/02.csv","r",encoding = "utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["姓名"])#字典可以键名访问值


