"""
爬取糗事百科

需要用到requests爬取页面，用xpath来提取数据

大致步骤
1.爬取整个页面
2.利用xpath爬取信息
3.保存文件落地
"""
import  requests
from lxml import etree

url = 'https://www.qiushibaike.com/hot/'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9"
}
rsp = requests.get(url,headers=headers)
html = rsp.text
#把页面解析成html
html = etree.HTML(html)
#contains 匹配一个属性值中包含的字符串
#//表示任意一个标签
rst = html.xpath('//div[contains(@id , "qiushi_tag")]')
for r in rst:
    content  = r.xpath('//div[@class="content"]/span')[0].text
    print(content)



