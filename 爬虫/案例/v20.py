"""
python中正则模块是re
使用大致步骤 ；
    1.compile函数将正则表达式的字符串变为一个Pattern对象
    2.通过Pattern对象的一些列方法对文本进行匹配，匹配结果是一个Match对象
    3.用Match对象的方法，对结果进行模拟
"""
import re


#\d表示数字，后边+表示这个数字可以出现一次或者多次
#r表示后边的是原生字符串，后边不需要转义
s=r"\d+"

#返回Pattern对象
pattern = re.compile(s)
m = pattern.match("one123two13213")

#默认匹配从头部开始，返回一个match的值
print(m)

#后边两个数字表示查找的范围
m = pattern.match("one123two13213",3,8)
print(m)
#group表示直接将match打印出来
print(m.group())
#表示从那个位置开始
print(m.start(0))
#表示从那个位置结束
print(m.end(0))
#表示所取出来的结果在字符串中的范围，(自我理解，包左不包右)
print(m.span(0))


