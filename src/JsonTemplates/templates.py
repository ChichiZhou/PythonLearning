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

template = {"AWSTemplateFormatVersion": "2010-09-09", "Resources": {}, "Outputs": {"StackArn": {
    "Description": "The DNSName of the backup load balancer",
    "Value": {"Ref": "AWS::StackId"}
}}}

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
