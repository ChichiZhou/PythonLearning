import json
import pickle

with open("./test2.json", "r") as f:
    template = json.load(f)

print(type(template))


template['Resources']["BDL2EdgetrueStatusAgentsEDGETagValueChangesPerMinuteAlarm"] = {
    "Type": "AWS::CloudWatch::Alarm",
    "Properties": {
        "AlarmName": "BDL2EdgetrueStatusAgentsEDGETagValueChangesPerMinuteAlarm",
        "ComparisonOperator": "LessThanThreshold",
        "Dimensions": [
            {"Name": "System Name", "Value": "BDL2_Edge"},
            {"Name": "Source", "Value": "AIMPublisher"},
            {"Name": "Active Nodee", "Value": "true"}
        ],
        "MetricName": "Status/Agents/EDGE/TagValueChangesPerMinute",
        "Namespace": "AFTMI/Ignition Monitoring",
        "Statistic": "Average",
        "Period": "60",
        "EvaluationPeriods": "60",
        "Threshold": "60",
        "DatapointsToAlarm": "59"
    }
}

print(template)

with open("./test3.json", "w") as f:
    json.dump(template, f)

with open("./test2.json", "r") as f:
    template = json.load(f)

print(template)
# class SetEncoder(json.JSONEncoder):
#     def default(self, obj):
#         if isinstance(obj, set):
#             return obj.__dict__
#         return json.JSONEncoder.default(self, obj)
#
# with open("./test2.json", "w") as f:
#     json.dump(template, f, cls = SetEncoder)
#
# with open("./test3.json", "wb") as f:
#     pickle.dump(template, f)
#
# ######## 只能用 pickle 再次写进去 ######
# ######## pickle 应该是可以用的 #######
#
# with open("./test3.json", "rb") as f:
#     result = pickle.load(f)
#
# print(result)
#
# print(type(result))
#
# ######### 使用模版创建 json template #######
# # 循环创建 dict #######
#
# with open("./test4.json", "w", encoding='utf-8') as f:
#     json.dump(result, f, ensure_ascii=False)