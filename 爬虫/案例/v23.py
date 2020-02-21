"""
findall
"""
import re

s = r"\d+"
pattern = re.compile(s)
m = pattern.findall("one123toe7890")
print(m)


m = pattern.finditer("uidh7908oinjuu109j900kl")
for item in m:
    print(item.group())