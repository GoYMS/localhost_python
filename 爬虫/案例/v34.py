"""
通过webdriver操作百度进行查找
"""

from selenium import webdriver
import time
#通过Keys模拟键盘
from selenium.webdriver.common.keys import Keys

#操作哪个浏览器就对那个浏览器建一个实例
#自动按照环境变量查找相应的浏览器
#如果浏览器没有在相应的环境变量中，需要指定浏览器的位置,例如下边一行
#driver = webdriver.PhantomJS(executable_path=r'E:\Anaconda3\phantomjs-2.1.1-windows\bin\phantomjs.exe')
driver = webdriver.PhantomJS()


driver.get("http://www.baidu.com")
#通过函数查找title标签

print("Title:{0}".format(driver.title))