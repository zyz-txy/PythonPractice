#爬虫：网络机器人
#开始---发送HTTP请求--解析结果提取数据--数据处理（清洗）--数据存储--结束
#合规性：查看目标网站的robots.txt
#User-agent：用户代理
#Disallow：不允许访问的资源
#Allow：允许访问的资源
#Sitemap：网站地图
#Crawl-delay：5（爬取间隔，避免频繁访问造成网站压力过大）
"""
搜索引擎（百度，Google）
舆情监控
商业分析（电商比价系统）
AI大模型训练语料
"""

import requests

#定义url
target_url = "https://www.tiobe.com/tiobe-index/"

#发送请求，获取数据
response = requests.get(target_url)

#输出数据到控制台
print(response.text)
