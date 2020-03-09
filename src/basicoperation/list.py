# 在 list 后面 append
a = [1]
print("before append is {}".format(a))
a.append(2)
print("after append is {}".format(a))

# 下面这种写法是错误的
a = [1,2,3,4,1,1,1,1,4,42,5,6,6,3,6]

print("a[:] is {}".format(a[:]))

for item in a[:]:
    if item == 1:
        a.remove(item)

print(a)

# merge two list
a = [1,2]
b = [3,4]

c = a + b
print(c)

