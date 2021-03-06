# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class T13XiaohuaPipeline(object):
    def process_item(self, item, spider):
        return item

import json
class XiaohuaPipeline(object):
    def __init__(self):
        self.file = open('xiaohua.json','w',encoding = 'utf-8')

    def process_item(self,item,spider):
        str = json.dumps(dict(item),ensure_ascii=False)
        str = str + '\n'
        self.file.write(str)

    def close_spider(self,spider):
        self.file.close()
