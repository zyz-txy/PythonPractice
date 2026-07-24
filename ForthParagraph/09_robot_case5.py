#获取高分电影榜单（Top100）数据，并保存在csv文件中
"""
步骤
1.明确网站()的robots.txt中的抓取规则，并遵守
2.查看页面的结构，拆解具体的操作步骤，按步骤开发
    a.获取高分电影数据列表
    b.遍历电影列表，获取每一部电影的详细信息，并提取电影数据信息
    c.将电影详细信息保存到csv文件中
"""

import requests
import csv
from lxml import html


#常量
MOVIE_LIST_FILE = "csv_data/movie_list.csv"
TMDB_BASE_URL = "https://www.themoviedb.org/"
TMDB_TOP_URL_1 = "https://www.themoviedb.org/movie/top-rated"#高分电影榜单首页20条数据
TMDB_TOP_URL_2 = "https://www.themoviedb.org/discover/movie/items"#高分电影榜单第二页之后




#alt + enter，快捷创建函数

#获取电影详情信息(电影名，年份，上映时间，类型，时长，评分，语言，导演，作者，主演，Slogan,简介)
def get_movie_info(movie_info_url):

    #1发送请求，获取电影详情数据
    movie_response = requests.get(movie_info_url,timeout = 60)
    print(f"发送请求{movie_info_url}，获取电影详情")


    #2解析数据，获取电影详情
    movie_document = html.fromstring(movie_response.text)
    #电影名称
    movie_names = movie_document.xpath("//*[@id='original_header']/div[2]/section/div[1]/h2/a/text()")
    #电影年份
    movie_years = movie_document.xpath("//*[@id='original_header']/div[2]/section/div[1]/h2/span/text()")
    #电影上映时间
    movie_dates = movie_document.xpath("//*[@id='original_header']/div[2]/section/div[1]/div/span[@class='release']/text()")
    #电影标签
    movie_tags = movie_document.xpath("//*[@id='original_header']/div[2]/section/div[1]/div/span[@class='genres']/a/text()")
    #电影时长
    movie_cost_times = movie_document.xpath("//*[@id='original_header']/div[2]/section/div[1]/div/span[@class='runtime']/text()")
    #电影评分
    movie_rating = movie_document.xpath("//*[@id='consensus_pill']/div/div[1]/div/div/@data-percent")
    #电影语言
    movie_languages = movie_document.xpath("//*[@id='media_v4']/div/div/div[2]/div/section/div[1]/div/section[1]/p[3]/text()")
    #电影导演
    movie_directors = movie_document.xpath("//*[@id='original_header']/div[2]/section/div[3]/ol/li[1]/p[1]/a/text()")
    #电影作者
    movie_novels = movie_document.xpath("//*[@id='original_header']/div[2]/section/div[3]/ol/li[2]/p[1]/a/text()")
    #电影标语
    movie_slogans = movie_document.xpath("//*[@id='original_header']/div[2]/section/div[3]/h3[1]/text()")
    #电影简介
    movie_descriptions = movie_document.xpath("//*[@id='original_header']/div[2]/section/div[3]/div/p/text()")

    #3返回电影详情
    #使用字典进行封装，方便后期维护与查找
    movie_info =  {
        "电影名": movie_names[0].strip() if movie_names else '',
        "年份": movie_years[0].strip() if movie_years else '',
        "上映时间": movie_dates[0].strip() if movie_dates else '',
        "类型": ",".join(movie_tags) if movie_tags else '',
        "时长": movie_cost_times[0].strip() if movie_cost_times else '',
        "评分": movie_rating[0].strip() if movie_rating else '',
        "语言": movie_languages[0].strip() if movie_languages else '',
        "导演": ",".join(movie_directors) if movie_directors else '',
        "作者": ",".join(movie_novels) if movie_novels else '',
        "宣传语": movie_slogans[0].strip() if movie_slogans else '',
        "简介": movie_descriptions[0].strip() if movie_descriptions else ''
    }
    # print(movie_info)
    return movie_info

#保存电影数据到csv文件中
def save_all_movies(all_movies):
    with open(MOVIE_LIST_FILE, mode='w', newline='', encoding='utf-8') as csvfile:
        #创建csv写入对象
        csv_writer = csv.DictWriter(csvfile, fieldnames=['电影名', '年份', '上映时间', '类型', '时长', '评分', '语言', '导演', '作者', '宣传语', '简介'])
        #写入表头
        csv_writer.writeheader()
        #写入数据
        csv_writer.writerows(all_movies)

# 主函数，定义核心逻辑
def main():
    # 定义一个空列表，保存所有电影数据
    all_movies = []
    #循环获取电影列表，从第一页到第五页
    for page_num in range(1, 6):
        # 1发送请求，获取高分电影榜单数据
        if page_num == 1:
            response = requests.get(TMDB_TOP_URL_1, timeout=60)
        else:
            response = requests.post(TMDB_TOP_URL_2,
                                     f"air_date.gte=&air_date.lte=&certification=&certification_country=AU&debug=&first_air_date.gte=&first_air_date.lte=&include_adult=false&include_softcore=false&latest_ceremony.gte=&latest_ceremony.lte=&page={page_num}&primary_release_date.gte=&primary_release_date.lte=&region=&release_date.gte=&release_date.lte=2027-01-24&show_me=everything&sort_by=vote_average.desc&vote_average.gte=0&vote_average.lte=10&vote_count.gte=300&watch_region=AU&with_genres=&with_keywords=&with_networks=&with_origin_country=&with_original_language=&with_watch_monetization_types=&with_watch_providers=&with_release_type=&with_runtime.gte=0&with_runtime.lte=400",
                                     timeout=60)
        print(f"获取第{page_num}页高分电影榜单数据：")
        # 2解析数据，获取电影列表
        # 先通过固定IDmedia-list精准锁定整个电影列表的父容器，这个ID是TMDB写死的页面结构标识，刷新页面也不会变，比之前用动态随机ID稳定得多
        # 用//在这个父容器内部全局搜索所有class里包含poster-card的div元素，也就是每一个独立的电影海报卡片；用contains()做模糊匹配，就算网站后续给卡片追加新的样式类名，这段定位逻辑也不会失效。
        document = html.fromstring(response.text)
        movie_list = document.xpath("//div[@id='media-list']//div[contains(@class, 'poster-card')]")

        # 3遍历电影列表，获取电影的详情

        for movie in movie_list:
            # 修正相对路径，直接在当前卡片下找a标签的href
            movie_urls = movie.xpath(".//a/@href")
            if movie_urls:
                # 注意TMDB返回的是相对路径，要做拼接处理
                movie_info_url = "https://www.themoviedb.org" + movie_urls[0]
                # 发送请求，获取电影详情数据
                movie_info = get_movie_info(movie_info_url)
                all_movies.append(movie_info)
    #4保存数据到csv文件中
    print("获取到所有电影数据，保存到csv文件中...")
    save_all_movies(all_movies)
if __name__ == "__main__":
     main()