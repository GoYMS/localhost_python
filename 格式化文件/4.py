import  re
p=re.compile(r'\d+')
#查找所有
res=p.findall("one123two345")
print(res)