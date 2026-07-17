def triangle_area(b,h):
    """
        根据传入的底和高计算三角形面积
    :param b: 底
    :param h: 高
    :return: 面积
    """
    return b * h / 2
print("底为30，高为20的三角形的面积为：",triangle_area(30,20))

def count_aeiou(s):
    """
    统计字符串中元音字母个数
    :param s:
    :return:
    """
    num = 0
    for w in s:
        if w in "aeiouAEIOU":
            num += 1
    return num
print("字符串中元音字母个数为：",count_aeiou("Hello World"))

def calc_score(score_list):
    """
    计算最高分、最低分、总分和平均分
    :param score_list: 分数列表
    :return: 最高分、最低分、总分和平均分
    """
    max_s = max(score_list)
    min_s = min(score_list)
    total_score = sum(score_list)
    avg_score = total_score / len(score_list)
    return max_s, min_s,  avg_score
max_ ,min_,avg_ = calc_score([580,590,575,595,586])
print(f"最高分：{max_}，最低分：{min_}，平均分：{avg_:.2f}")

#练习，判断回文字符串
def pal(s):
    """
    判断字符串是否为回文字符串
    :param s: 字符串
    :return: 布尔值
    """
    return  s == s[::-1]
print(pal("level"))