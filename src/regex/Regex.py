print("hello world")

import re

# 将正则表达式编译成 pattern
# 以下是为了项目中的匹配
# python 中的 regex 和 java 是一样的
aim = re.compile("^(Gateway/OPC/Connections/)(.*)(/Enabled)$")
matchone = "Gateway/OPC/Connections/UDP_MAP/Enabled"


# 判断字符串是否能够匹配
# https://www.runoob.com/python/python-reg-expressions.html
if re.match(aim, matchone):
    print("true")
else:
    print("false")

