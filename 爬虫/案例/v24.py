"""
中文unicode案例
"""

import re

s = r"[\u4e00-\u9fa5]+"
pattern = re.compile(s)
m = pattern.findall(u"你好，世界")
print(m)

