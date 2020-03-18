###全部用绝对路径就可以避免 import error #######
# from src.InputDirectory import dependency
# 利用相对路径导入文件。这里python只会以当前路径向下搜索，而不会向上搜索
import os
# import sys
# sys.
from src.InputDirectory2 import Another     # 这种写法是对的
from src.InputDirectory import dependency   # 这种写法也是对的
from InputDirectory2.Another import dd      # 这种写法也是正确的

print(os.getcwd())
print(os.path.abspath('.'))  # 当前绝对路径
# print("sys.path is {}".format(sys.path))
print(dependency.cc)
print(Another.dd)
print(Another.dd2)

