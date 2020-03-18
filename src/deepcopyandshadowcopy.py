a = {1:1, 2:2}

b = a

for key in b.keys():
    b[key] += 1


print("b dict is {}".format(b))
print("a dict is {}".format(a))

import copy
a = {1:1, 2:2}

b = copy.deepcopy(a)

for key in b.keys():
    b[key] += 1

print("b dict is {}".format(b))
print("a dict is {}".format(a))

a = {1:[1,1], 2:[2,2]}
b = copy.deepcopy(a)

for key in b.keys():
    temp = []
    for item in b[key]:
        temp.append(item + 1)
    b[key] = temp

print("b is {}".format(b))
