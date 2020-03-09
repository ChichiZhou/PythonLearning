a = {1: "1", 2: "2"}

# 将元素从map中去除
print("origin a is {}".format(a))
a.pop(1)
print("after pop is {}".format(a))

a = {"1": 1, "2": 2}

print("print out this whole dict {}".format(a.items()))

print("print out the first item in the dict {}".format(list(a.items())[0]))

print("print the value of the first item in the dict {}".format(list(a.items())[0][1]))

print("only get the value {}".format(a.values()))

print("convert the value to list {}".format(list(a.values())))
