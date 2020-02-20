import json
with open("./testInput.json", "r") as f:
    template = json.load(f)

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

template["Outputs"]["BDL2EdgetrueStatusAgentsEDGETagValueChangesPerMinuteAlarm"] = {
    "Value": {"Ref": "BDL2EdgetrueStatusAgentsEDGETagValueChangesPerMinuteAlarm"}
}

with open("./testInput2.json", "w") as f:
    json.dump(template, f)