import abc

class AbstractClass(metaclass= abc.ABCMeta):
    @abc.abstractmethod
    def implementit(self): pass