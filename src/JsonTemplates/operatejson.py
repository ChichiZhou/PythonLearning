import json


# 写入json 文件
# dumps 和 dump, loads 和 load 的区别在哪？
template = {"a": {"b":"1"}}
with open("./fk.json", "w") as f:
    json.dump(template, f)     # 如果要使用 dump ，则需要传入 template 和 f


with open("./fk.json", "r") as f:
    readtemplate = json.load(f)  # 如果要用 load 的话，只需要传入 f 即可
                                 # 这样读取的 readtemplate 仍然是 dict，而不会变成 string

print("The output of read file is {}".format(readtemplate['a']))


a = {"a" : [{"1": 2}]}


