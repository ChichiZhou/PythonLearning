print("hello world")

import re

# 将正则表达式编译成 pattern
# 以下是为了项目中的匹配
# python 中的 regex 和 java 是一样的
# https://www.runoob.com/python/python-reg-expressions.html
aim = re.compile("^(Gateway/OPC/Connections/)(.*)(/Enabled)$")
matchone = "Gateway/OPC/Connections/UDP_MAP/Enabled"


# 判断字符串是否能够匹配
# https://www.runoob.com/python/python-reg-expressions.html
if re.match(aim, matchone):
    print("true")
else:
    print("false")


us_info = re.compile("^(US)-([A-Z]*)-([0-9]*)$")
print(us_info)
test = "US-IAD-1"
usual = "ACY1"

if re.match(us_info, usual):
    print("This is true")
else:
    print("This is false")

re_list = ["(.*)(AIMPublisher/TotalTagsFailed)$"]
test_list = ["Status/TagAgent/AIMPublisher/TotalTagsFailed", "Status/TagAgent/LETO/TotalTagsFailed", "Gateway/Performance/CPU Usage",
             "Gateway/Performance/Memory Utilization"]
result = []
for re_sitename in re_list:
    te = re.compile(re_sitename)
    print(te)
    for test_case in test_list:
        if re.match(te, test_case):
            result.append(test_case)

print(result)



