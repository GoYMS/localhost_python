from bs4 import BeautifulSoup
from urllib import request

url = 'http://www.baidu.com'

rsp = request.urlopen(url)
html = rsp.read()

soup = BeautifulSoup(html,'lxml')
#bs自动转码
html = soup.prettify()
#打印出标签为link的代码
print(soup.link)

print(soup.link.name)
print(soup.link.attrs)



print(soup.title)
#NavigableString
print(soup.title.string)
