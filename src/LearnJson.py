import json

with open("testjson.json", "w") as f:
    f.write(json.dumps("{a:12}"))

with open("testjson.json", "r") as f:
    result = json.load(f)


print(result)

print(type(result))