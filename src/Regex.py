print("hello world")

import re

# 将正则表达式编译成 pattern
# 以下是为了项目中的匹配
aim = re.compile("^(Gateway/OPC/Connections/)(.*)(/Enabled)$")
matchone = "Gateway/OPC/Connections/UDP_MAP/Enabled"


if re.match(aim, matchone):
    print("true")
else:
    print("false")
