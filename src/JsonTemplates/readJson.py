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

dataTobeDumped = {
    "AWSTemplateFormatVersion": "2010-09-09",
    "Resources": {
        "ACY1EdgetrueStatusAgentsEDGETagValueChangesPerMinuteAlarm": {
            "Type": "AWS::CloudWatch::Alarm",
            "Properties": {
                "AlarmName": "ACY1EdgetrueStatusAgentsEDGETagValueChangesPerMinuteAlarm",
                "ComparisonOperator": "LessThanThreshold",
                "Dimensions": [
                    {"Name": "System Name", "Value": "ACY1_Edge"},
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
    },
    "Outputs": {
        "StackArn": {
            "Description": "The DNSName of the backup load balancer",
            "Value": {"Ref": "AWS::StackId"}
        },
        "ACY1EdgetrueStatusAgentsEDGETagValueChangesPerMinuteAlarm": {
            "Value": {"Ref": "ACY1EdgetrueStatusAgentsEDGETagValueChangesPerMinuteAlarm"}
        }
    }
}

with open("./test2.json", "w") as f:
    # f.write(json.dumps(dataTobeDumped))
    json.dump(dataTobeDumped, f)

