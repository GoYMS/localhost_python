"""
任务：通过selenium模拟对页面元素的控制
"""

from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path=r'C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chromedriver.exe')
driver.get('https://www.baidu.com')
"""
通过js来控制网页内容，需要先把js编写出来，然后通过execute_script 执行
"""
js = "var q=document.getElementById(\'kw\'); q.style.border=\'2px solid red\';"
#执行代码
driver.execute_script(js)
time.sleep(3)
driver.save_screenshot('t08_baidu.png')
#js隐藏相应元素，我们这里隐藏logo
img = driver.find_element_by_xpath('//*[@id="lg"]/img')
driver.execute_script('$(arguments[0]).fadeOut()',img)
#滚动滑动条到最下
js = "$('.scroll_top').click(function(){$('html.body').animate({scrollTop:'0px'},800)});"
time.sleep(3)
driver.save_screenshot("t08_baidu2.png")