import abc

class Factory(metaclass=abc.ABCMeta):
    def orderpizza(self):
        self.createpizza()

    @abc.abstractmethod
    def createpizza(self): pass



class TexasRoad(Factory):
    def createpizza(self):
        print("I Love Texas")


if __name__ == '__main__':
    texaspizza = TexasRoad()
    texaspizza.createpizza()
