"""
 案例1

#导入相关的包、
import re

#查找相关的数字
#r表示字符串不转义
pattern=re.compile(r'\d+')

#在字符串"123one789two"中按照pattern指定的正则进行查找

match=pattern.match("123one789two")

print(match)
"""


"""
#案例2
#导入相关的包、
import re

#查找相关的数字
#r表示字符串不转义
pattern=re.compile(r'\d+')
#在字符串"123one789two"中按照pattern指定的正则进行查找
#后边的参数0,10表示查找的范围
match=pattern.match("123one789two",0,10)

print(match)
#start
print(match.start(0))
#end
print(match.end(0))

#上述代码说明的问题
#1.match可以输入参数表示想要查找的起始位置
#2.查找到的结果只包含一个，表示第一次进行匹配成功的内容
"""


#案例三
import re
# I表示忽略掉大小写
#下边的相当于分两个组，两组之间必须空开,([a-z]+) ([a-z]+)是一个整体，满足这两个的话打印出来，
# 例如”I am yang ming“，会打印出来“I am”

p=re.compile(r'([a-z]+) ([a-z]+)',re.I)
m=p.match("I aam EROMAN niiu")
print(m)

#下边三个表示整个匹配到的字符串

print(m.group(0))
print(m.start(0))
print(m.end(0))

#下边三个表示第一组的内容和起始的位置
print(m.group(1))
print(m.start(1))
print(m.end(1))


#下边表示将所有的组表示出来

print(m.groups())



