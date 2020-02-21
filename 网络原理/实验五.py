import requests
import csv
from lxml import etree


headers = {
    "User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36"
}
url = 'https://tieba.baidu.com/p/6281342588'
html = requests.get(url,headers=headers)
with open('source.text','w',encoding='utf-8') as f:
   f.write(html.text)
html = etree.HTML(html.text)
all = html.xpath('//div[@class="l_post l_post_bright j_l_post clearfix  "]')

rows = []
for html in all:
    #获得用户名
    name = html.xpath('.//div[@class="d_author"]/ul/li/a/text()')[0]

    #获得发帖内容
    text= html.xpath('.//div[@class="d_post_content j_d_post_content "]/text()')[0]
    #获取发帖时间
    time = html.xpath('.//div[@class="post-tail-wrap"]/span[4]/text()')[0]
    content = (name,text,time)

    rows.append(content)

headers = {
    ('name','text','time')
}

with open('result.csv','w',newline='',encoding='utf-8') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(headers)
    f_csv.writerows(rows)

