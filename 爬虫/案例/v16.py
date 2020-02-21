"""
爬取豆瓣电影数据
了解ajax的基本爬取方式
因为豆瓣中排行榜电影往下拉是一直都有新的东西出现，所以判定是ajax

"""
from urllib import request
import json
#url是选取其中的一段的地址
url = 'https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=40&limit=20'

rsp = request.urlopen(url)
data = rsp.read().decode()

#一般情况下ajax所得到的页面是json格式，所以需要解码
#json.loads 用于解码 JSON 数据
data = json.loads(data)

print(data)
