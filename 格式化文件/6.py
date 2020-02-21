import re


#不是仅仅是针对中文, 可以针对任何的字符串，代表是对字符串进行unicode编码。
#一般英文字符在使用各种编码下, 基本都可以正常解析, 所以一般不带u；但是中文,
# 必须表明所需编码, 否则一旦编码转换就会出现乱码。
title=u'世界 你好 I love you'
p=re.compile(r'[\u4e00-\u9fa5]+')
rst=p.findall(title)
print(rst)