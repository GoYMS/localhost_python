from bs4 import BeautifulSoup
from urllib import request

url = 'http://www.baidu.com'

rsp = request.urlopen(url)
html = rsp.read()

soup = BeautifulSoup(html,'lxml')
#bs自动转码
html = soup.prettify()
for node in soup.head.contents:
    if node.name == "meta":
        print(node)
    if node.name == "title":
        print(node.string)
print("==" * 12)

