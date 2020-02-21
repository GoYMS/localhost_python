from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
#driver = webdriver.PhantomJS()
#手动添加路径（chromedriver.exe）
driver = webdriver.Chrome(executable_path=r'C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chromedriver.exe')
url = "http://www.baidu.com"


driver.get(url)

wrapper = driver.find_element_by_id("wrapper").text
print(wrapper)
print(driver.title)

#得到页面的快照
driver.save_screenshot('index.png')

#id="kw" 的是百度的输入框，我们得到输入框的ui元素之后直接输入“大熊猫”
driver.find_element_by_id('kw').send_keys(u"大熊猫")
#id="su"是百度搜索的按钮，click模拟点击
driver.find_element_by_id('su').click()
#中间要停留几秒钟，因为页面在加载，如果不停留，页面还没加载出来，就应经保存快照了
time.sleep(10)
#保存快照
driver.save_screenshot("daxiongmao.png")

#模拟输入两个按钮ctrl+a
driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'a')
#模拟输入两个按钮ctrl+x
driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'x')
driver.find_element_by_id('kw').send_keys(u"航空母舰")
driver.find_element_by_id('su').click()
time.sleep(10)
driver.save_screenshot("hangkongmujian.png")

#清除页面
driver.find_element_by_id('kw').clear()
#用完之后需要退出
driver.quit()
