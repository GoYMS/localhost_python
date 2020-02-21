#sub替换的案例
import re
p=re.compile(r'(\w+) (\w+)')

s="hello 123 wang 345"
#下边的意思是如果在s中有满足正则表达式的字符串，则将其与‘Hello world’替换
rst=p.sub(r'Hello world',s)
print(rst)
