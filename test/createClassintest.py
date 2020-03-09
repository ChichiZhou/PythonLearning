import pytest
from test.creatclassfortest import AbstractClass

class TestAbstractClass:

    # @pytest.fixture
    # def Case(self):
    #     class createSubclass(AbstractClass):
    #         def __int__(self):
    #             self.s = None
    #         def implementit(self):
    #             self.s = "hi there"
    #     return createSubclass()

    class createSubclass(AbstractClass):
        def __int__(self):
            self.s = None
        def implementit(self):
            self.s = "hi there"


    # def setup_class(self):
    #     class createSubclass(AbstractClass):
    #         def __int__(self):
    #             self.s = None
    #         def implementit(self):
    #             self.s = "hi there"


    def test_initialize(self):
        test = self.createSubclass()
        test.implementit()
        assert test.s== "hello"


if __name__ == '__main__':
    pytest.main(["test_abstractClass"])

