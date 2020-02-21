"""
要求导入scrapy
所有类一般是XXXSpider命名
所有爬虫类是scrapy.Spider的子类
"""
"""
创建scrapy方法   在相应项目的路径中打开cmd  输入命令   scrapy startproject  项目名
运行方法：在cmd中运行  scrapy crawl  爬虫的名字（name=‘’）
"""
import scrapy

class BaiduSpider(scrapy.Spider):
    #name是爬虫的名字
    name = "baidu"
    #起始的url列表
    start_url = ['https://www.baidu.com']

    #负责分析downloader下载得到的结果
    def parse(self,response):

        with open("baidu.html","w",encoding='utf-8') as f :
          f.write(response.body.decode('utf-8'))


