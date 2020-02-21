"""
构建代理集群/队列
每次访问服务器，随机抽取一个代理
抽取可以访问  random.choice

分析步骤
1.构建代理群
2.每次访问，随机选取代理并行执行
"""
from urllib import request,error
import random
url = "http://www.baidu.com"
#1设置代理地址
proxy_list = [
    #列表中存放的是dict类型的元素
    #如果运行中出现无法访问的情况，说明代理服务器死了
    {"http":"181.114.224.38:8080"},
    {"http":"95.38.14.3:8080"},
    {"http":"196.251.19.113:53281"},
    {"http":"103.194.232.131:8123"}
]
#2创建ProxyHandler
proxy_handler_list = []
for proxy in proxy_list:
    proxy_handler = request.ProxyHandler(proxy)
    proxy_handler_list.append(proxy_handler)
#3创建Opener
opener_list = []
for proxy_handler in proxy_handler_list:
    opener = request.build_opener(proxy_handler)
    opener_list.append(opener)
#安装opener
opener = random.choice(opener_list)
request.install_opener(opener)

try:
    rsp = request.urlopen(url)
    html = rsp.read().decode()
    print(html)
except error.URLError as e:
    print(e)
except Exception as e:
    print(e)
