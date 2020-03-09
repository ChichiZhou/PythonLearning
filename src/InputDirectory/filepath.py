import os

# os.path.abspath(os.path.join(os.getcwd(), "testresultfolder"))
# os.path.abspath() 的作用是什么？

print(os.getcwd())

print(os.path.abspath(os.path.join(os.getcwd(), "testresultfolder")))
