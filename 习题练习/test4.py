""""
#写一个6位随机验证码程序（使用random模块），要求验证码中必须包含一个数字，一个小写字母，一个大写字母

import random
import string
password=[]
password.append(random.choice(string.ascii_uppercase))
password.append(random.choice(string.ascii_lowercase))
password.append(random.choice(string.digits))
while len(password)<6:
    password.append(random.choice(string.ascii_uppercase+string.ascii_lowercase+string.digits))
#join()：    连接字符串数组。将字符串、元组、列表
# 中的元素以指定的字符(分隔符)连接生成一个新的字符串
#在这里是用 空 作为连接符
password1="".join(password)
print(password)
"""
