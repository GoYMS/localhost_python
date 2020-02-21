"""
search
"""

import re

s = r"\d+"

pattern = re.compile(s)
m = pattern.search("one12two34three56")
print(m.group(0))

m = pattern.search("one12two34three56",10,30)
print(m.group(0))

