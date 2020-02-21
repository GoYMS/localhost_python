
'''
#习题1
#匹配一行文字中所有的开头字母
import re
s='I love you yang ming shuai'
p=re.compile(r'\b\w')
m=p.findall(s)
print(m)
'''


"""
#习题2
#匹配一行文字中所有数字开头的内容
import re
s1='i love 200 100time'
rst=re.findall(r'\b\d',s1)
print(rst)
"""


"""
#习题三
#匹配只包含数字和字母的行
import re
s = 'i love you200 89ui 89nijio  kjin'
rst = re.findall(r'\w+',s)
print(rst)
"""
"""
#习题四
#写一个正则表达式，使其能匹配以下字符 'bit','hut','nut','hat','hit'
import re
s = "'bit','hut','nut','hat','hit'"
#比较't'前边点数不同所得到的结果不同
rst = re.findall(r'.t',s)
rst1 = re.findall(r'..t',s)
rst2 = re.findall(r'...t',s)
print(rst)
print(rst1)
print(rst2)
"""

"""
#习题五

#提取 每行中 完整的年月日和时间段
import re

s = 'hfiuvhsiuf  1997-07-22 22:23:54  jiajis  2009-03-27 22:23:54 '
#{}里边显示的是位数
rst = re.findall(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}',s)
print(rst)
"""
"""
#习题六
#提取邮箱
import re
s = 'xxx@qq.com jij  13456  xxxx@wangiyun.com'

rst = re.findall(r'\w+@\w+.com',s)
print(rst)
"""

"""
#习题七

#将字符串中的电子邮件替换成其他的邮件
import re
s = 'xxx@qq.com jij  13456  xxxx@wangiyun.com'

rst = re.sub(r'\w+@\w+.com','1789353033@qq.com',s)
print(rst)
"""


#习题八
#使用正则表达式提取字符串中的单词
import re
s = 'i love you 89u jko0i8078 jis'
rst = re.findall(r'\b[a-zA-Z]+\b',s)
print(rst)