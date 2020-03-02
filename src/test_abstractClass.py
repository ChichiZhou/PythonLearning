import pytest
from creatclassfortest import AbstractClass

class TestAbstractClass:

    # @pytest.fixture
    # def Case(self):
    #     class createSubclass(AbstractClass):
    #         def __int__(self):
    #             self.s = None
    #         def implementit(self):
    #             self.s = "hi there"
    #     return createSubclass()

    # test  pytest
    @pytest.fixture
    def Case(self):
        class createSubclass(AbstractClass):
            def __int__(self):
                self.s = None
            def implementit(self):
                self.s = "hi there"
        return createSubclass()

    def test_initialize(self, Case):
        test = Case
        test.implementit()
        assert test.s== "hello"


if __name__ == '__main__':
    pytest.main(["test_abstractClass"])

