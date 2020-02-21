"""
利用正则来爬取猫眼电影
爬取电影信息
方法三步走：
1.把整个页面爬取出来
2.提取出来每部电影的单元
3.对每个单元进行查找
"""
from urllib import request
import re

url = 'https://maoyan.com/board'
rsp = request.urlopen(url)
html = rsp.read().decode()
#现在需要将关于电影的数据爬取出来，观察源代码，每部电影都在一个<dd>标签中间,利用正则
#    ' .*? ' 表示匹配任意数量的重复，但是在能使整个匹配成功的前提下使用最少的重复
s = r'<dd>.*?</dd>'
pattern = re.compile(s,re.S)
films = pattern.findall(html)
#从每部电影中将需要的信息爬取出来

for film in films:
    #小括号括起来的这部份正则表达式可以被当作一个“组”。
    # 这个组可以作为整体被后面的修饰，
    # 也可在后续处理中单独获得这一部分正则的匹配结果。
    s = r'<a.*?title="(.*?)"'
    pattern = re.compile(s)
    #注意观察源代码中有两个<a>标签中都有title，此处的[0]为只获取第一个就行
    title = pattern.findall(film)[0]
    print(title)