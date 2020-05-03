from src.singleton.tableclass import Table
class SingleTon:

    # instance = None

    # class __OnlyOne():
    #     def __init__(self, value):
    #         self.instance = Table(value)

        # def get_instance(self):
        #     if self.instance is None:
        #         return self.__init__(1)
        #     else:
        #         return self.instance

    # def __init__(self):
    #     if not SingleTon.instance:
    #         SingleTon.instance = SingleTon.__OnlyOne(1)

    instance = Table(1)


# class Table:
#     instance = None
#     def __init__(self, val):
#         if not Table.instance:
#             self.instance = Table(val)



if __name__ == '__main__':
    s1 = SingleTon()
    s2 = SingleTon()

    print(s1.instance.val)
    print(s2.instance.val)

    print(id(s1.instance) == id(s2.instance))

    s1.instance.val = 2

    print("s2 value is {}".format(s2.instance.val))