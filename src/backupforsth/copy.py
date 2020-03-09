import abc
import os
import json


class AlarmClass(metaclass=abc.ABCMeta):

    def __init__(self, alarmTypes, parameterMap, alarmTypesNameAndAggregatedTemplateFiles, uplimit, outputpath):
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

        self.alarmTypeAndAggregatedTemplateFilesRelation = {}       # This is used to store the relation between alarm type and aggregated cloudwatch alarm file in which they are stored
        self.metricsAndAggregatedTemplateFilesRelation = {}         # This is used to store the relation between metrics and aggregated cloudwatch alarm file in which they are stored
        self.aggregatedTemplateFilesAndCloudWatchAlarm = {}          # This is used to store the relation between aggregated cloudwatch alarm file and the cloudwatch alarms stored in this file
        # need to the metrics and cloudwatch alarm relaitons
        self.metricsAndCloudWatchAlarmNames = {}
        # need to know the aggregated file and metrics
        self.aggregatedTemplateFilesAndMetrics = {}
        # need to know the cloudwatchalarm and type
        self.cloudwatchalarmAndAlarmType = {}
        self.cloudwatchalarmsAndNestedFiles = {}
        self.cloudwatchalarmsAndMetrics = {}
        self.outputpath = outputpath


    @abc.abstractmethod
    def createMetricSiteDict(self, metricInput): pass

    def createAllAggragatedCloudWatchTemplateFiles(self, fillTemplate):
        """ Create all aggregated cloudwatch alarm files for all cloudwatch alarm types.

        Args:
            fillTemplate: The template which used to descript cloudwatch paramters.
        """

        for alarmTypeInput in self.alarmTypesNameAndAggregatedTemplateFiles:
            metricsAndSites = self.createMetricSiteDict(alarmTypeInput)
            oneMetricsInputAndNestedFileRelation = self.createTemplatesForOneAlarmType(alarmTypeInput, metricsAndSites, fillTemplate)
            for key in oneMetricsInputAndNestedFileRelation.keys():
                self.metricsAndAggregatedTemplateFilesRelation[key] = copy.deepcopy(oneMetricsInputAndNestedFileRelation[key])
                for aggregatedFile in oneMetricsInputAndNestedFileRelation[key]:
                    if aggregatedFile not in self.aggregatedTemplateFilesAndMetrics:
                        self.aggregatedTemplateFilesAndMetrics[aggregatedFile] = [key]
                    else:
                        self.aggregatedTemplateFilesAndMetrics[aggregatedFile].append(key)
            temp = []
            for metrics in oneMetricsInputAndNestedFileRelation.keys():
                temp += oneMetricsInputAndNestedFileRelation[metrics]
            self.alarmTypeAndAggregatedTemplateFilesRelation[alarmTypeInput] = list(set(temp))

    def createTemplatesForOneAlarmType(self, alarmTypeInput, metricsAndSites, fillTemplate):
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

        cloudwatchalarmsAndNestedFiles = self.createAggregatedCloudWatchTemplates(formatDict, alarmTypeInput, fillTemplate)

        for key in cloudwatchalarmsAndNestedFiles.keys():
            aggregatedTemplateFiles = cloudwatchalarmsAndNestedFiles[key]
            if aggregatedTemplateFiles in self.aggregatedTemplateFilesAndCloudWatchAlarm:
                self.aggregatedTemplateFilesAndCloudWatchAlarm[aggregatedTemplateFiles].append(key)
            else:
                self.aggregatedTemplateFilesAndCloudWatchAlarm[aggregatedTemplateFiles] = [key]

        for metrics in metricsAndCloudWatchAlarmNames.keys():

            for cloudwatchalarm in metricsAndCloudWatchAlarmNames[metrics]:

                aggregatedTemplateFiles = cloudwatchalarmsAndNestedFiles[cloudwatchalarm]
                if metrics not in metricsAndAggregatedTemplateFilesRelation:
                    metricsAndAggregatedTemplateFilesRelation[metrics] = [aggregatedTemplateFiles]
                elif aggregatedTemplateFiles not in metricsAndAggregatedTemplateFilesRelation[metrics]:
                    metricsAndAggregatedTemplateFilesRelation[metrics].append(aggregatedTemplateFiles)

        for metrics in metricsAndCloudWatchAlarmNames.keys():
            self.metricsAndCloudWatchAlarmNames[metrics] = metricsAndCloudWatchAlarmNames[metrics]
            for cloudwatchalarm in metricsAndCloudWatchAlarmNames[metrics]:
                self.cloudwatchalarmsAndMetrics[cloudwatchalarm] = metrics
        return metricsAndAggregatedTemplateFilesRelation

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

    def createAggregatedCloudWatchTemplates(self, formatDict, alarmTypeInput, fillTemplate):
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
        fileName = self.alarmTypesNameAndAggregatedTemplateFiles[alarmTypeInput]

        folder = self.outputpath + '/cloudwatchtemplates'

        if not os.path.exists(folder):
            os.makedirs(folder)

        createList = self.cutIntoSection(formatDict)

        for sectionNumber in range(len(createList)):
            template = fillTemplate.originalTemplates()

            with open(folder + "/{}Alarms{}.json".format(fileName.replace('/', ''), sectionNumber), 'w') as f:
                nestedfilename = "{}Alarms{}.json".format(fileName.replace('/', ''), sectionNumber)
                for parameterInput in createList[sectionNumber]:
                    nometricsmath = fillTemplate(template)
                    cloudwatchalarmname, template = nometricsmath.addOneItem(parameterInput)
                    cloudwatchalarmsAndAggregatedTemplageFiles[cloudwatchalarmname] = nestedfilename
                    self.cloudwatchalarmAndAlarmType[cloudwatchalarmname] = alarmTypeInput
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


    def addCloudWatchAlarm(self, addedalarmType, addedmetrics, addedmetricsparameter, fillTemplate):
        """ Add one CloudWatch alarm into the aggregated cloudwatch alarm template files
        Args:
            :param addedmetrics: The metric of the new CloudWatch alarm.
            :param addedmetricsparameter: The parameter of addedmetrics.
            :param fillTemplate: templates which used to descript the CloudWatch alarm parameter for each metric.

        """

        availablefile = next((file for file in self.alarmTypeAndAggregatedTemplateFilesRelation[addedalarmType] if len(self.aggregatedTemplateFilesAndCloudWatchAlarm[file]) < 50), None)
        if availablefile is None:
            operationfile = "{}Alarms{}.json".format(self.alarmTypesNameAndAggregatedTemplateFiles[addedalarmType], len(self.metricsAndAggregatedTemplateFilesRelation[addedmetrics]))
            self.aggregatedTemplateFilesAndCloudWatchAlarm[operationfile] = [addedmetricsparameter["AlarmName"]]

        else:
            self.aggregatedTemplateFilesAndCloudWatchAlarm[availablefile].append(addedmetricsparameter["AlarmName"])

            operationfile = self.findAggregatedTemplateFile(addedmetrics)
            if operationfile is None:
                operationfile = availablefile

        if addedmetrics in self.metricsAndCloudWatchAlarmNames:
            self.metricsAndCloudWatchAlarmNames[addedmetrics].append(addedmetricsparameter["AlarmName"])
        else:
            self.metricsAndCloudWatchAlarmNames[addedmetrics] = [addedmetricsparameter["AlarmName"]]

        if addedmetrics in self.metricsAndAggregatedTemplateFilesRelation:
            self.metricsAndAggregatedTemplateFilesRelation[addedmetrics].append(operationfile)
        else:
            self.metricsAndAggregatedTemplateFilesRelation[addedmetrics] = operationfile

        self.alarmTypeAndAggregatedTemplateFilesRelation[addedalarmType].append(operationfile)

        with open(self.outputpath + "/cloudwatchtemplates/{}".format(operationfile), "r") as f:
            templateneededtobemodified = json.load(f)

        new_template = fillTemplate(templateneededtobemodified)
        new_template.addOneItem(addedmetricsparameter)

        with open(self.outputpath + "/cloudwatchtemplates/{}".format(operationfile), "w") as f:
            json.dump(templateneededtobemodified, f)

        # add cloudwatch
        self.cloudwatchalarmsAndMetrics[addedmetricsparameter["AlarmName"]] = addedmetrics
        self.cloudwatchalarmAndAlarmType[addedmetricsparameter["AlarmName"]] = addedalarmType

        return operationfile


    def findAggregatedTemplateFile(self, addedmetrics):
        """ Find the aggregated CloudWatch alarm file.

        :param addedmetrics: The metric of the new CloudWatch alarm.

        :return: The aggregated cloudwatch alarm file which contains the new metric
        """

        if addedmetrics in self.metricsAndAggregatedTemplateFilesRelation:
            candidatenestedfiles = self.metricsAndAggregatedTemplateFilesRelation[addedmetrics]
            availablefile = next((file for file in candidatenestedfiles if len(self.aggregatedTemplateFilesAndCloudWatchAlarm[file]) < 50), None)
            return availablefile

    def deleteMetrics(self, deletealarmType, deletealarmmetrics, deletealarmname):

        operationfile = self.findAggregatedTemplateFile(deletealarmmetrics)
        try:
            operationfile is not None
        except ValueError:
            print("The metric you want to delete does not exist")

        with open(self.outputpath + "/cloudwatchtemplates/{}".format(operationfile), "r") as f:
            templateneededtobemodified = json.load(f)

        templateneededtobemodified["Resources"].pop(deletealarmname)

        with open(self.outputpath + "/cloudwatchtemplates/{}".format(operationfile), "w") as f:
            json.dump(templateneededtobemodified, f)

        self.aggregatedTemplateFilesAndCloudWatchAlarm[operationfile].remove(deletealarmname)

        self.metricsAndCloudWatchAlarmNames[deletealarmmetrics].remove(deletealarmname)

        count = 0
        for cloudwatchalarm in self.aggregatedTemplateFilesAndCloudWatchAlarm[operationfile]:
            if self.cloudwatchalarmsAndMetrics[cloudwatchalarm] == deletealarmmetrics:
                return
            else:
                count += 1

        if count == 0:
            self.metricsAndAggregatedTemplateFilesRelation[deletealarmmetrics].remove(operationfile)

        count = 0
        for cloudwatchalarm in self.aggregatedTemplateFilesAndCloudWatchAlarm[operationfile]:
            if self.cloudwatchalarmAndAlarmType[cloudwatchalarm] == deletealarmType:
                return
            else:
                count += 1

        if count == 0:
            self.alarmTypeAndAggregatedTemplateFilesRelation[deletealarmType].remove(operationfile)

        self.cloudwatchalarmsAndMetrics.pop(deletealarmname)
        self.cloudwatchalarmAndAlarmType.pop(deletealarmname)
