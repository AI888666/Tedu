"""
    macth对象
"""

import re

regex = re.compile(r"(ab)cd(?P<pig>ef)")

# macth对象
obj = regex.search("abcdefghijkldegcsfsa")

print(obj)

# 属性变量
# print("正则表达式：", obj.re)
# print("目标字符串：", obj.string)
# print("起始位置：", obj.pos)
# print("结束位置：", obj.endpos)
# print("最后一组名称：", obj.lastgroup)
# print("最后一组序号：", obj.lastindex)

# 属性方法
print("匹配内容的位置：", obj.span(), obj.start(), obj.end())
print("子组内容：", obj.groups())
print("捕获组内容：", obj.groupdict())
print("对应内容：", obj.group())
print("对应内容：", obj.group(1))
print("对应内容：", obj.group(2))

