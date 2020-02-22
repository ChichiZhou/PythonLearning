import abc

class FactoryOne(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def output(self):pass

class SonFactory(FactoryOne):
    def output(self):
        print("I am son")

class SonFactory2(FactoryOne):
    def output(self):
        print("ok I will listen to my father")

if __name__ == '__main__':
    son1 = SonFactory()
    son1.output()

    son2 = SonFactory2()
    son2.output()

