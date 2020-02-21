from bs4 import BeautifulSoup
from urllib import request

url = 'http://www.baidu.com'

rsp = request.urlopen(url)
html = rsp.read()

soup = BeautifulSoup(html,'lxml')

print("="*10)
titles = soup.select("title")
print(titles[0])
print("="*10)

metas = soup.select("meta[content='always']")
print(metas[0])
