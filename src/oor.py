import abc
import os
import json
import copy


class AlarmClass(metaclass=abc.ABCMeta):

    def __init__(self, alarmTypes, parameterMap, alarmTypesNameAndAggregatedTemplateFiles, uplimit):
        """ Initialize the object

        Args:
            alarmTypes: The alarm types
            parameterMap: The parameters for each alarm
            alarmTypesNameAndAggregatedTemplateFiles: The file name for each alarm
            uplimit: The limit for each aggregated cloudwatch alarm file
        """
        self.alarmTypes = alarmTypes
        self.parameterMap = parameterMap
        self.alarmTypesNameAndAggregatedTemplateFiles = alarmTypesNameAndAggregatedTemplateFiles
        self.uplimit = uplimit


    @abc.abstractmethod
    def createMetricSiteDict(self, metricInput): pass

    def createAllNestedFiles(self, fillTemplate):
        """ Create all aggregated cloudwatch alarm files for all cloudwatch alarm types.

        Args:
            fillTemplate: The template which used to descript cloudwatch paramters.
        """

        for alarmTypeInput in self.alarmTypesNameAndAggregatedTemplateFiles:
            metricsSitesDict = self.createMetricSiteDict(alarmTypeInput)
            self.createAllTemplates(alarmTypeInput, metricsSitesDict, fillTemplate)


    def createAllTemplates(self, alarmTypeInput, metricsAndSites,  fillTemplate):
        """ Create all aggregated cloudwatch alarm template files for one cloudwatch alarm type.

        Args:
            alarmTypeInput: The input alarm type (i.e systemCPUUsage).
            metricsAndSites: The dict with key: metrics, value: site names in this metircs (i.e  System/CPU/Usage : [ACY1, ACY4, EWR4 ...]).
            fillTemplate: The templates which used to descript the cloudwatch alarm parameter for each metric.

        Returns:
            metricsAndAggregatedTemplateFilesRelation: The metricsAndAggregatedTemplateFilesRelation for one alarm type
        """
        metricsAndAggregatedTemplateFilesRelation = {}
        metricsAndCloudWatchAlarmNames = {}
        fileName = self.alarmTypesNameAndAggregatedTemplateFiles[alarmTypeInput]

        formatDict = []
        for metrics in metricsAndSites.keys():
            for name in metricsAndSites[metrics]:
                parametersForOneCloudWatch = self.createInputMap(name, metrics, self.parameterMap[alarmTypeInput])

                for parameters in parametersForOneCloudWatch:
                    if metrics not in metricsAndCloudWatchAlarmNames:
                        metricsAndCloudWatchAlarmNames[metrics] = [parameters['AlarmName']]
                    else:
                        metricsAndCloudWatchAlarmNames[metrics].append(parameters['AlarmName'])

                formatDict += copy.deepcopy(parametersForOneCloudWatch)
        self.createNestedStackFiles(formatDict, fileName, fillTemplate)


    def createInputMap(self, sitename, metrics, parameterDict):
        ''' Create input parameter for each metrics

        Args:
            sitenmae: i.e ACY1
            metrics:  i.e System/CPU/Usage
            parameterDict: i.e Threshold, Statics, ...

        Returns:
            parameterlist: {Systemname: ACY1, Metrics: System/CPU/Usage, Threshold:60, ....}
        '''

        parameterlist = []
        for parameter in parameterDict:
            active = parameter['Active']
            finalSystemName = ''.join(list(filter(str.isalnum, sitename)))

            finalname = finalSystemName +'{}'.format(active) + ''.join(list(filter(str.isalnum, ''.join(metrics.split('/'))))) + "Alarm"

            parameter['AlarmName'] = finalname
            parameter['SystemName'] = sitename
            parameter['Metrics'] = metrics

            parameterlist.append(parameter)

        return parameterlist

    def createNestedStackFiles(self,formatDict, fileName, fillTemplate):
        ''' Create all nested files for one metric

        Args:
            formatDict: The input parameter for one alarm type (i.e System/CPU/Usage).
            fileName: The fileName corresponds to the alarm type (i.e systemCPUUsage).
               This file will be part of the finall aggregated cloudwatch alarm template files (i.e "systemCPUUsageAlamr1.json").
            fillTemplate: The templates which used to descript the cloudwatch alarm parameter for each metric.

        Return:
            cloudwatchalarmsAndAggregatedTemplageFiles: The cloudwatchalarms and aggregated templage files for one alarm type
        '''

        cloudwatchalarmsAndAggregatedTemplageFiles = {}

        folder = os.path.abspath(os.path.join(os.getcwd())) + '/cloudwatchtemplates'
        if not os.path.exists(folder):
            os.makedirs(folder)


        createList = self.cutIntoSection(formatDict)

        for sectionNumber in range(len(createList)):
            template = {"AWSTemplateFormatVersion": "2010-09-09", "Resources": {}, "Outputs": {"StackArn": {
                "Description": "The DNSName of the backup load balancer",
                "Value": {"Ref": "AWS::StackId"}
            }}}

            with open(folder + "/{}Alarms{}.json".format(fileName.replace('/', ''), sectionNumber), 'w') as f:
                nestedfilename = "{}Alarms{}.json".format(fileName.replace('/', ''), sectionNumber)
                for parameterInput in createList[sectionNumber]:
                    nometricsmath = fillTemplate(template)
                    cloudwatchalarmname = nometricsmath.addOneItem(parameterInput)
                    cloudwatchalarmsAndAggregatedTemplageFiles[cloudwatchalarmname] = nestedfilename

                json.dump(template, f)

        return cloudwatchalarmsAndAggregatedTemplageFiles

    def cutIntoSection(self, formatDict):
        """ Cut the input parameter into different slices. Those slices are used to generate aggregated cloudwatch alarm
            template files.

        Args:
            formatDict: The input parameter for one alarm type (i.e System/CPU/Usage).

        Returns:
            sectionList: The list of slice which is used to generate aggregated cloudwatch alarm template files.
        """
        sectionList = []
        start = 0
        while start < len(formatDict):
            tempstart = start
            tempcount = 0
            sublist = []
            while tempstart < len(formatDict) and tempcount < self.uplimit:
                sublist.append(formatDict[tempstart])
                tempstart += 1
                tempcount += 1

            start = tempstart
            sectionList.append(sublist)

        return sectionList
