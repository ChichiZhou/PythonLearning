import json
template = {"a": {"b":"1"}}
with open("./fk.json", "w") as f:
    json.dump(template, f)

    
a = {"a" : [{"1": 2}]}

print(a)