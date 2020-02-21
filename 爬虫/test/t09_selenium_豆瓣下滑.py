"""
利用selenium自动下拉页面
"""
from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path=r'C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chromedriver.exe')
url = 'https://movie.douban.com/typerank?type_name=%E5%89%A7%E6%83%85&type=11&interval_id=100:90&action='
driver.get(url)
#向下滑动5000像素
js = 'document.body.scrollTop=10000'
time.sleep(3)

driver.execute_script(js)

time.sleep(3)

driver.quit()