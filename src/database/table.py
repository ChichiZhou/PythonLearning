from src.syldb.core.field import Field
# 结构：
# 这里不设置主键，而是设置一些 field （字段）
# 每条 item 考一个自增的key值来区分
# 将 alarmName 当做主键

class Table:

    def __init__(self):
        self.table = {}
        self.fieldName = []
        self.fieldObject = {}
        self.rows = 0

    def addFields(self, fieldName):
        self.fieldName.append(fieldName)
        self.table[fieldName] = {}

    # def addItem(self, item):
    #     # item 是 field 数据类型的
    #     self.rows += 1
    #     for key in item.keys():
    #         self.table[key][self.rows] = item[key]

    def addItem(self, item):
        # item 是 field 数据类型的
        for key in item.keys():
            self.table[key][item["alarmName"]] = item[key]

    def searchItem(self, fieldType, fieldValue):
        result_key = []
        for key in self.table[fieldType]:
            value = self.table[fieldType][key]
            if value == fieldValue:
                result_key.append(key)
        return result_key
        # return self.returnFormat(result_key)

    def returnFormat(self, key):
        final = []
        result = {}
        for aimKey in key:
            for key in self.table.keys():
                result[key] = self.table[key][aimKey]
            final.append(result)

        return final

    def delteItem(self, fieldType, fieldValue):
        # itemKey = self.searchItem(fieldType, fieldValue)
        result_key = []
        for key in self.table[fieldType]:
            value = self.table[fieldType][key]
            if value == fieldValue:
                result_key.append(key)

        for key in self.table.keys():
            subDict = self.table[key]
            for deleteKey in result_key:
                subDict.pop(deleteKey)
        # return result_key
        # return self.returnFormat(result_key)

    def modifyItem(self, key, valueType, value):
        result_item = self.searchItem("alarmName", key)
        print("!!!!!!")
        print(result_item)
        # for key in t.table.keys():
        #     for modifiedItem in result_item:
        #         # print(t.table[modifiedItem])
        #         # print("Nedded modified".format(modifiedItem))
        #
        #         t.table[modifiedItem] = value
        #         # print("result")
        #         # print(modifiedItem)
        for modifiedItem in result_item:
            t.table[valueType][modifiedItem] = value



if __name__ == '__main__':
    item = [{"alarmName": "aaa", "siteName": "bbb", "metrics": "fkxbbswf"}, {"alarmName": "ccc", "siteName": "ddd", "metrics": "fkxbbswf"}]
    t = Table()
    fieldNameList = ["metrics", "siteName", "alarmName"]
    for field in fieldNameList:
        t.addFields(field)

    for subItem in item:
        t.addItem(subItem)

    print(t.table)

    search_result = t.searchItem("alarmName", "aaa")

    print("The return result will be {}".format(search_result))

    # 根据别的 field 去找
    print("根据别的 field 去找")
    search_result = t.searchItem("metrics", "fkxbbswf")
    print("The return result will be {}".format(search_result))

    # 改变某个 alarmName 的值
    print("改变某个 alarmName 的值")
    t.modifyItem("aaa", "metrics", "ljxbbswf")

    print(t.table)

    # delete item
    print("delete a certain value")
    t.delteItem("alarmName", "aaa")

    print(t.table)

