"""
    演示正则表达式
"""

import re

s = "skks:1009,ronsf:2900"
# pattern = r"\w+:\d+"
# pattern = r"(\w+):\d+"
pattern = r"(\w+):(\d+)"

# 使用re调用
l = re.findall(pattern, s)
print(l)

# compile对象
regex = re.compile(pattern)
l2 = regex.findall(s, 0, 13)
print(l2)

# 使用正则表达式匹配到的内容切割字符串
l = re.split("[^\w]", s)
print(l)

# 使用指定的字符串替换匹配到的内容
s1 = re.sub(r":", "$", s)
s2 = re.subn(r":", "$", s)
print(s1,s2)
