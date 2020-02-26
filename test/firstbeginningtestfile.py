import pytest

class TestAlarmClass():

    @pytest.fixture        # 这样可以写一个所有 test 都能用都变量
    def staticvalule(self):
        return 2
    @pytest.fixture
    def staticvalue2(self):
        return 3
    def test_passing(self):
        assert(1,2,3) == (1,2,3)

    def test_other(self):
        assert 1+2 ==4

    def test_equal(self, staticvalule, staticvalue2):   # 可以用一个或者多个
        assert staticvalule == staticvalue2             # 需要声明这里需要进行什么操作

    def test_printout(self, staticvalule):     # 如果不发生错误则不会输出
        print("The value is {}".format(staticvalule))



if __name__ == '__main__':

    pytest.main(["firstbeginningtestfile.py"])   # 这里写需要测试的文件名
