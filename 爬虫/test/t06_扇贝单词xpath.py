"""
扇贝单词
把单词列表爬取下来
利用xpath

"""
from  urllib import request
from lxml import etree

#用于存储单词


def shanbei():
    for page in range(1,11):
        url = 'https://www.shanbay.com/wordlist/187711/540709/?page={0}'.format(page)
        print(url)

        rsp = request.urlopen(url)
        html = rsp.read().decode()
        #解析成html形式
        html = etree.HTML(html)
        #因为tr标签下边是单词和释义，先将tr标签提取出来
        tr_list = html.xpath(".//tr")

        for tr in tr_list:
            word = []
            #查找相应的单词和释义
            strong = tr.xpath('.//strong')
            #判断是否爬取到
            if len(strong):

                #strip把找到的内容自动去掉空格
                name =  strong[0].text
                word.append(name)

            td_content = tr.xpath('./td[@class="span10"]')
            if len(td_content):
                content = td_content[0].text
                word.append(content)
            print(word)

if __name__ == '__main__':
    shanbei()