
seq = [1,2,3,4,5]

# next(x for x in seq if x == 1)
# find the first match element
result = next((x for x in seq if x == 1), None)

print(result)