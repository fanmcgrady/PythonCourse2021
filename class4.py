# 匿名函数
# lambda_fun = lambda x, y, z : x * y * z
#
# print(type(lambda_fun))
# print(lambda_fun(2, 3, 4))
#
# # filter
# ll = [1, 2, 3, 4]
# def filter_fun(i):
# if i > 3:
#     return i
# else:
#     return None
# return i if i > 3 else None

# print(list(filter(filter_fun, ll)))

# 另一种等价的filter方法
# ll2 = [i for i in ll if i > 3]
# print(ll2)

# map
# list3 = [1, 2, 3, 4]

# def map_fun(i):
#     return "{}.txt".format(i)

# result = map(map_fun, list3)
# print(list(result))


# def fun(x, y):
#     return x * y, x + y, x / y
#
# m, a, s = fun(1, 2)

# 教务处新闻爬虫程序
## 1、分析网页结构
# <div class="list-llb-box">.....
#     <ul class="list-llb-s">....
#         <li class="list-llb-list">....
#             <a href=".."....

## 2、Python获取网页源代码
import requests
from bs4 import BeautifulSoup

url = "http://jwc.scu.edu.cn"
html = requests.get(url)
html.encoding = 'utf-8'
# print(html.text)
web_source = BeautifulSoup(html.text, 'html.parser')
news_list = web_source.select('.list-llb-list')

## 3、处理数据，获取新闻列表
for li in news_list:
    a = li.find('a')
    title = a['title']
    url = a['href']
    date = a.select('.list-date-a')[0].get_text()

    print("新闻：标题：{}，日期：{}，地址：{}"
          .format(title, date, url))