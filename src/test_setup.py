import pytest
from creatclassfortest import AbstractClass

class TestSohu(object):

    class createSubclass(AbstractClass):
        def __int__(self):
            self.s = None
        def implementit(self):
            self.s = "hi there"

    temp = createSubclass()

    def test_initialize(self):
        # test = self.createSubclass()
        # test.implementit()
        self.temp.implementit()
        assert self.temp.s== "hello"






