"""
正则match的使用方法
"""

import re
#以下使用了分组，以小括号为每个组
s = r"([a-z]+) ([a-z]+)"
pattern = re.compile(s,re.I) # re.I 表示忽略分大小写

m = pattern.match("Hello world wide web")

#group(0)表示返回匹配到的整个字符串
s = m.group(0)
print(s)
#span(0)表示匹配成功的整个字符串的跨度
len = m.span(0)
print(len)
#group(1)表示的是返回第一个匹配成功的字符串(此处说明分组是从下标为1开始的)
s = m.group(1)
print(s)

len = m.span(1)
print(len)

#将所有的组都打出来
s = m.groups()
print(s)