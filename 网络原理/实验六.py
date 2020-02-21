#coding=utf-8

import requests
from lxml import etree


headers = {
    "User-Agent" :'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}
url = 'http://www.kanunu8.com/book3/6879/'
html = requests.get(url,headers=headers)
html = etree.HTML(html.text)
#获得所有章节的短链接
list = html.xpath('//tr[@bgcolor="#ffffff"]/td/a/@href')
#通过观察每章网址，得出正确的网址为以下内容

for i in list:
    #每章地址
    url1 = url+i
    html = requests.get(url1, headers=headers)
    html = etree.HTML(html.text)
    zhang = html.xpath('//td[@width="820"]/p/text()')
    print(zhang)

