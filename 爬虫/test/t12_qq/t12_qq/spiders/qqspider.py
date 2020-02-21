"""
    1.创建项目
    2.编写item
    3.编写spider
    4.编写pipeline
    5.设置pipeline
"""
import scrapy
import re
from t12_qq.items import QQItem

class QQspider(scrapy.Spider):
    name = 'qq'
    #设置智能爬取腾讯域名的信息
    allowed_domain = ['hr.tencent.com']
    start_url = ['https://hr.tencent.com/position.php?&start=0#a']

    def parse(self, response):

        #下载的页面自动存入response中
        for each in response.xpath('//*[@class="even"]'):
            #对于得到的每一个工作信息，把数据封装入相应的item中
            item = QQItem()
            name = each.xpath('./td[1]/a/text()').extract()[0]
            detaiLink = each.xpath('./td[1]/a/@href').extract()[0]
            positionInfo = each.xpath('./td[2]/a/text()').extract()[0]
            workLocation = each.xpath('./td[4]/a/text()').extract()[0]

            item['name'] = name.encode('utf-8')
            item['detaiLink'] = detaiLink.encode('utf-8')
            item['positionInfo'] = positionInfo.encode('utf-8')
            item['workLocation'] = workLocation.encode('utf-8')
            #处理继续爬取的链接
            #通过的到当前页，提取数字把数字加十，替换原来的数字，就是下一个页面地址
            curpage = re.search('(\d+)',response.url).group(1)
            page = int(curpage)+10
            url = re.sub('\d+',str(page),response.url)
            #把地址通过yield返回
            yield scrapy.Request(url,callback=self.parse)
            yield item



