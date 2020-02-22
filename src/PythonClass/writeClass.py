'''
使用python写类和继承
'''
class Factory:

    def __int__(self):
        pass

    def output(self):
        print("hello there")

    def hithere(self):
        # 要想引用，必须在前面写 self
        self.output()


class SubFactory(Factory):
    pass


if __name__ == '__main__':
    subfactory = SubFactory()
    subfactory.hithere()

