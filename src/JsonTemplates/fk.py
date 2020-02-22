import json
template = {"a": {"b":"1"}}
with open("./fk.json", "w") as f:
    json.dump(template, f)