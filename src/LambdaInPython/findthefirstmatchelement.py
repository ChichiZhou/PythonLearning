seq = ['1234455555']

# next(x for x in seq if x == 1)
# find the first match element
# 这里的 next 就相当于 stream
result = next((n for n in range(len(seq)) if seq[n] == '1234455555'), None)

print(result)


a_dict = {"1": ["a"]}

print(a_dict["1"])

for i in range(len(seq)):
    print(seq[i])
