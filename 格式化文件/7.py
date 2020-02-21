import re

title=u'<div>nihao<div>jjj<div>age<div>'

# .*表示在字符串中，<div>和<div>中内容，所有的尽可能多的都打印出来（贪婪）
#  .*?表示在字符串中，<div>和<div>中内容，尽可能少的打印出来   （非贪婪）

p1=re.compile(r'<div>.*<div>')
p2=re.compile(r'<div>.*?<div>')

m1=p1.search(title)
print(m1.group())
m2=p2.search(title)
print(m2.group())