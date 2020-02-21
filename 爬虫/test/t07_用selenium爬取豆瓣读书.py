"""
使用selenium爬取页面
保存后用xpath进行分析
"""

from selenium import webdriver
import time
from lxml import etree


def getweb():
    url = 'https://book.douban.com/subject_search?search_text=python&cat=1001&start=%s0'
    driver = webdriver.Chrome(executable_path=r'C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chromedriver.exe')
    driver.get(url)
    time.sleep(10)
    driver.save_screenshot('t07(豆瓣).png')

    fn = 't07(豆瓣).html'
    with open(fn,'w',encoding='utf-8') as f:
    #   page_source得到页面的源码
        f.write(driver.page_source)

    content_parse(fn)
    driver.quit()
def content_parse(fn):

    with open(fn,'r',encoding='utf-8') as f:
       html = f.read()

    #生成xml树
    tree = etree.HTML(html)
    #查找book
    books = tree.xpath('//div[@class="item-root"]')
    for book in books:
        book_name = book.xpath(".//div[@class='title']/a")
        print(book_name)


if __name__ == '__main__':
    getweb()
