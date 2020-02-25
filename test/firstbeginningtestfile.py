import pytest

class TestAlarmClass():

    @pytest.fixture
    def staticvalule(self):
        return 2
    def test_passing(self):
        assert(1,2,3) == (1,2,3)

    def test_other(self):
        assert 1+2 ==4

    def test_equal(self, staticvalule):
        assert staticvalule == 3



if __name__ == '__main__':

    pytest.main(["firstbeginningtestfile.py"])   # 这里写需要测试的文件名
