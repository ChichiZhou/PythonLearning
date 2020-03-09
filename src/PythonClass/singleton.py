"""
http://kuanghy.github.io/2015/12/19/python-variable
https://zhuanlan.zhihu.com/p/37534850
https://www.cnblogs.com/huchong/p/8244279.html

"""
class singleton:
    _instance = None   # 这种写法属于类变量，也就是 static

    def __new__(cls, *args, **kw):
        if cls._instance is None:
            cls._instance = object.__new__(cls, *args, **kw)
        return cls._instance
    
    def __init__(self):
        self.var = "This is singleton"


if __name__ == '__main__':
    s1 = singleton()
    s2 = singleton()
    print(s1.var)
    print(s2.var)
    print(id(s1) == id(s2))
