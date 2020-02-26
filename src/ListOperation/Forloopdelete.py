a = [1,2,3,4,1,1,1,1,4,42,5,6,6,3,6]

print("a[:] is {}".format(a[:]))

for item in a[:]:
    if item == 1:
        a.remove(item)

print(a)