import json
import copy
with open("./test2.json", "r") as f:
    template = json.loads(f.read())

print(type(template))

print(template['Hello'])

template['Bye'] = {"Seeya"}

print(template)


with open("./test3.json", "w") as f:
    json.dump(template, f)

