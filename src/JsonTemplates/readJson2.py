import json
import pickle

with open("./test2.json", "r") as f:
    template = json.load(f)
f.close()
print(type(template))

print(template['Hello'])

template['Bye'] = {"EEEE"}

print(template)


# with open("./test3.json", "w") as f:
#     json.dump(template, f)

with open("./test3.json", "wb") as f:
    pickle.dump(template, f)

######## 只能用 pickle 再次写进去 ######
######## pickle 应该是可以用的 #######

with open("./test3.json", "rb") as f:
    result = pickle.load(f)

print(result)

print(type(result))

######### 循环创建 dict #######