import json

with open("./test.json", "r") as f:
    template = json.loads(f.read())

print(template)

print(template['Resources'])

print(template['Resources'].values())
# print(template['Resources']['MetricName'])

print(list(template['Resources'].values()))

# 这个可以用来访问到准确的值
print(list(template['Resources'].values())[0]['Properties']['MetricName'])

dataTobeDumped = {"Hello": {"Hi": "Hi"}}
with open("./test2.json", "w") as f:
    # f.write(json.dumps(dataTobeDumped))
    json.dump(dataTobeDumped, f)
