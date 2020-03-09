import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), "../")))
from AlarmClass import AlarmClass
from unittest import mock
from util.NoMetricsMath import NoMetricsMath
import os
import json
import shutil

class TestAlarmClass:
    alarmTypes = ["TagValueChangesPerMinute"]
    parameterMap = {"TagValueChangesPerMinute": [{"Source": "AIMPublisher", "Compare": "LessThanThreshold", "Active": "true", "Statistic":"Average", "Threshold":60, "Period":60, "Counts": 59, "Datapoints":60, "Missingdata":"breaching"}]}
    alarmTypesNameAndAggregatedTemplateFiles = {"TagValueChangesPerMinute": "aimpublisherTagChanges"}
    metricsSiteDict = {"TagValueChangesPerMinute":{"Status/Agents/EDGE/TagValueChangesPerMinute":["ACY1_Edge"]}, "ActiveTagsCount":{"Status/Agents/EDGE/ActiveTagsCount":["ACY1_Edge"]}}
    testdirectory = os.path.abspath(os.path.join(os.getcwd(), "testresultfolder"))

    class mockAlarm(AlarmClass):
        def __init__(self, alarmTypes, parameterMap, alarmTypesNameAndAggregatedTemplateFiles, uplimit, outputpath, returnlist):
            AlarmClass.__init__(self, alarmTypes, parameterMap, alarmTypesNameAndAggregatedTemplateFiles, uplimit, outputpath)
            self.returnlist = returnlist

        def createMetricSiteDict(self, alarmTypeInput):
            return self.returnlist[alarmTypeInput]

    testobject = mockAlarm(alarmTypes, parameterMap, alarmTypesNameAndAggregatedTemplateFiles, 2, testdirectory, metricsSiteDict)

    def test_createInputMap(self):
        """
        Test the method to generate CloudWatch parameter
        """
        parameterMap = {"TagValueChangesPerMinute": [{"Source": "AIMPublisher", "Compare": "LessThanThreshold", "Active": "true", "Statistic":"Average", "Threshold":60, "Period":60, "Counts": 59, "Datapoints":60, "Missingdata":"breaching"}]}
        parameterlist = self.testobject.createInputMap("ACY1_Edge", "Status/Agents/EDGE/TagValueChangesPerMinute", parameterMap["TagValueChangesPerMinute"])

        assert parameterlist == [{'Source': 'AIMPublisher', 'Compare': 'LessThanThreshold', 'Active': 'true', 'Statistic': 'Average', 'Threshold': 60, 'Period': 60, 'Counts': 59, 'Datapoints': 60, 'Missingdata': 'breaching', 'AlarmName': 'ACY1EdgetrueStatusAgentsEDGETagValueChangesPerMinuteAlarm', 'SystemName': 'ACY1_Edge', 'Metrics': 'Status/Agents/EDGE/TagValueChangesPerMinute'}]

    def test_createTemplate(self):
        """
        Test the method to create aggregated CloudWatch template
        :return:
        """
        template = NoMetricsMath.originalTemplates()

        assert template == {"AWSTemplateFormatVersion": "2010-09-09", "Resources": {}, "Outputs": {"StackArn": {
            "Description": "The DNSName of the backup load balancer",
            "Value": {"Ref": "AWS::StackId"}
        }}}

        template = NoMetricsMath(template)

        newadded = {'Source': 'AIMPublisher', 'Compare': 'LessThanThreshold', 'Active': 'true', 'Statistic': 'Average', 'Threshold': 60, 'Period': 60, 'Counts': 59, 'Datapoints': 60, 'Missingdata': 'breaching', 'AlarmName': 'ACY1EdgetrueStatusAgentsEDGETagValueChangesPerMinuteAlarm', 'SystemName': 'ACY1_Edge', 'Metrics': 'Status/Agents/EDGE/TagValueChangesPerMinute'}
        template.addOneItem(newadded)

        assert template.template == {"AWSTemplateFormatVersion": "2010-09-09", "Resources": {"ACY1EdgetrueStatusAgentsEDGETagValueChangesPerMinuteAlarm": {"Type": "AWS::CloudWatch::Alarm", "Properties": {"AlarmName": "ACY1EdgetrueStatusAgentsEDGETagValueChangesPerMinuteAlarm", "ComparisonOperator": "LessThanThreshold", "Dimensions": [{"Name": "System Name", "Value": "ACY1_Edge"}, {"Name": "Source", "Value": "AIMPublisher"}, {"Name": "Active Node", "Value": "true"}], "MetricName": "Status/Agents/EDGE/TagValueChangesPerMinute", "Namespace": "AFTMI/Ignition Monitoring", "Statistic": "Average", "Period": 60, "EvaluationPeriods": 59, "Threshold": 60, "DatapointsToAlarm": 60, "TreatMissingData": "breaching"}}}, "Outputs": {"StackArn": {"Description": "The DNSName of the backup load balancer", "Value": {"Ref": "AWS::StackId"}}, "ACY1EdgetrueStatusAgentsEDGETagValueChangesPerMinuteAlarm": {"Value": {"Ref": "ACY1EdgetrueStatusAgentsEDGETagValueChangesPerMinuteAlarm"}}}}

    def test_allAggreagatedFiles(self):
        """
        Test the method to create all aggregated cloudwatch alarm files according to the uplimit
        """
        alarmTypeInput = "TagValueChangesPerMinute"

        formatDict = [{'Source': 'AIMPublisher', 'Compare': 'LessThanThreshold', 'Active': 'true', 'Statistic': 'Average', 'Threshold': 60, 'Period': 60, 'Counts': 59, 'Datapoints': 60, 'Missingdata': 'breaching', 'AlarmName': 'ACY1EdgetrueStatusAgentsEDGETagValueChangesPerMinuteAlarm', 'SystemName': 'ACY1_Edge', 'Metrics': 'Status/Agents/EDGE/TagValueChangesPerMinute'}, {"Source": "AIMPublisher", "Compare": "LessThanThreshold", "Active": "true", "Statistic":"Average", "Threshold":0, "Period":60, "Counts": 30, "Datapoints":30, "Missingdata":"ignore"}]

        self.testobject.cutIntoSection = mock.Mock(return_value = [[{'Source': 'AIMPublisher', 'Compare': 'LessThanThreshold', 'Active': 'true', 'Statistic': 'Average', 'Threshold': 60, 'Period': 60, 'Counts': 59, 'Datapoints': 60, 'Missingdata': 'breaching', 'AlarmName': 'ACY1EdgetrueStatusAgentsEDGETagValueChangesPerMinuteAlarm', 'SystemName': 'ACY1_Edge', 'Metrics': 'Status/Agents/EDGE/TagValueChangesPerMinute'}], [{'Source': 'AIMPublisher', 'Compare': 'LessThanThreshold', 'Active': 'true', 'Statistic': 'Average', 'Threshold': 60, 'Period': 60, 'Counts': 59, 'Datapoints': 60, 'Missingdata': 'breaching', 'AlarmName': 'BDL2EdgetrueStatusAgentsEDGETagValueChangesPerMinuteAlarm', 'SystemName': 'BDL2_Edge', 'Metrics': 'Status/Agents/EDGE/TagValueChangesPerMinute'}]])

        self.testobject.createAggregatedCloudWatchTemplates(formatDict, alarmTypeInput, NoMetricsMath)

        filelist = os.listdir(self.testdirectory + "/cloudwatchtemplates")

        assert len(filelist) == 2

        shutil.rmtree(self.testdirectory)

    def test_findAggregatedTemplateFile(self):
        """
        Test the method to find the file in which is used to add CloudWatch alarm
        """
        addedmetrics = "Status/Agents/EDGE/TagValueChangesPerMinute"

        # self.testobject.createMetricSiteDict = mock.Mock(return_value = {"Status/Agents/EDGE/TagValueChangesPerMinute":["ACY1_Edge"]})
        self.testobject.createAllAggragatedCloudWatchTemplateFiles(NoMetricsMath)
        assert self.testobject.findAggregatedTemplateFile(addedmetrics) == "aimpublisherTagChangesAlarms0.json"

    def test_addCloudWatch(self):
        """
        Test the method to add one CloudWatch alarm into file
        :return:
        """
        addedmetricInputType = "TagValueChangesPerMinute"
        addedmetrics = "Status/Agents/EDGE/TagValueChangesPerMinute"
        addedmetricsparameter = {'Source': 'AIMPublisher', 'Compare': 'LessThanThreshold', 'Active': 'true', 'Statistic': 'Average', 'Threshold': 60, 'Period': 60, 'Counts': 59,
                                 'Datapoints': 60, 'Missingdata': 'breaching', 'AlarmName': 'XXX1EdgetrueStatusAgentsEDGETagValueChangesPerMinuteAlarm', 'SystemName': 'XXX1_Edge',
                                 'Metrics': 'Status/Agents/EDGE/TagValueChangesPerMinute'}

        self.testobject.createAllAggragatedCloudWatchTemplateFiles(NoMetricsMath)

        filename = self.testobject.addCloudWatchAlarm(addedmetricInputType, addedmetrics, addedmetricsparameter, NoMetricsMath)

        with open(self.testdirectory + "/cloudwatchtemplates/{}".format(filename), "r") as f:
            template = json.load(f)

        assert "XXX1EdgetrueStatusAgentsEDGETagValueChangesPerMinuteAlarm" in template["Resources"]

    def test_deleteCloudWatchAlarm(self):
        self.testobject.createAllAggragatedCloudWatchTemplateFiles(NoMetricsMath)

        deletealarmType = "TagValueChangesPerMinute"
        deletealarmmetrics = "Status/Agents/EDGE/TagValueChangesPerMinute"
        deletealarmname = "ACY1EdgetrueStatusAgentsEDGETagValueChangesPerMinuteAlarm"

        self.testobject.deleteMetrics(deletealarmType, deletealarmmetrics, deletealarmname)


if __name__ == '__main__':
    pytest.main(["test_alarmClass.py"])
