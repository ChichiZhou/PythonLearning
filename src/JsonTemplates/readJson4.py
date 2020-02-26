import json
with open("./test3.json", "r") as f:
    template = json.load(f)

print(template)

# 删除 dict 中的元素
template['Resources'].pop("BDL2EdgetrueStatusAgentsEDGETagValueChangesPerMinuteAlarm")

print(template)