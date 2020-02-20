'''
testfile1 is in different directory
testfile2 is in the same directory
'''
import os
import testfile2
import sys
######### This can work ###########
# sys.path.append(os.getcwd() + '/TestDirectory')
# import testfile1
########## This can also work ############
from src.TestDirectory import testfile1
# At first, there is still redline. But the red line disappear after I set the src as source



print(testfile2.b)
# os.getcwd() and os.path.abspath(os.getcwd()) 有相同的输出结果

print("The os.getcwd() is {}".format(os.getcwd())) # /Users/hezho/PythonLearning/PythonLearning/src
print("The os.path.abspath.getpath() is {}".format(os.path.abspath(os.getcwd()))) # /Users/hezho/PythonLearning/PythonLearning/src

print(os.getcwd() + '/TestDirectory')
print(testfile1.a)