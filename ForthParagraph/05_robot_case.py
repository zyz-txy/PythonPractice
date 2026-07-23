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

#定义url常量
TMDB_BASE_URL = "https://www.themoviedb.org/"
TMDB_TOP_URL = "https://www.themoviedb.org/movie/top-rated"

#alt + enter，快捷创建函数

#获取电影详情信息
def get_movie_info(movie_info_url):
    pass

#保存电影数据到csv文件中
def save_all_movies(all_movies):
    pass

# 主函数，定义核心逻辑
def main():
#1发送请求，获取高分电影榜单数据
    response = requests.get(TMDB_TOP_URL,timeout = 60)
#2解析数据，获取电影列表
#先通过固定IDmedia-list精准锁定整个电影列表的父容器，这个ID是TMDB写死的页面结构标识，刷新页面也不会变，比之前用动态随机ID稳定得多
#用//在这个父容器内部全局搜索所有class里包含poster-card的div元素，也就是每一个独立的电影海报卡片；用contains()做模糊匹配，就算网站后续给卡片追加新的样式类名，这段定位逻辑也不会失效。
    document = html.fromstring(response.text)
    movie_list = document.xpath("//div[@id='media-list']//div[contains(@class, 'poster-card')]")

#3遍历电影列表，获取电影的详情
    all_movies = []
    for movie in movie_list:
    # 修正相对路径，直接在当前卡片下找a标签的href
        movie_urls = movie.xpath(".//a/@href")
        if movie_urls:
        # 注意TMDB返回的是相对路径，要做拼接处理
            movie_info_url = "https://www.themoviedb.org" + movie_urls[0]
        #发送请求，获取电影详情数据
            get_movie_info(movie_info_url)
            all_movies.append(movie_info_url)
#4保存数据到csv文件中
    save_all_movies(all_movies)
if __name__ == "__main__":
     main()