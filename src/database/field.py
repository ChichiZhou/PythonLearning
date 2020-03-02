class Field:
    def __int__(self, metric, siteName, alarmType, alarmName, alarmParameter):
        self.metric = metric
        self.siteName = siteName
        self.alarmType = alarmType
        self.alarmName = alarmName
        self.alarmParameter = alarmParameter


    def modify(self, field, value):
        self.field = value


