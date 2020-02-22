'''
This is used to create the map which is finally used to create templates

For one:
metrics : [all parameters]
source: AIMPublisher
compare: LessThanThreshold
active: true
statistic: Average
threshold:
period:(in seconds)
counts: EvaluationPeriods
datapoints: DatapointsToAlarm
'''
def createInputMap(a, *parameterList):
    b, c = parameterList

    d = {"A": a, "B":b, "C":c}
    return d

if __name__ == '__main__':
    createInputMap([1])