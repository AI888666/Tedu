"""
    正则表达式演示2
"""
import re

s = "1949年10月1日，中国人民共和国成立"

it = re.finditer(r"\d+", s)

for item in it:
    print(item.group())

# 匹配开头位置
obj = re.match(r"\d+", s)
print(obj.group())

# 匹配第一处
obj = re.search(r"\d+", s)
print(obj.group())

# 完全匹配
obj = re.fullmatch(r".+", s)
print(obj.group())