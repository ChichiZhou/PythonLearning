class test():
    """
    方法的重载
    """
    def samename(self, a, b):
        print(a + b)

    def samename(self, a):
        print(a)


if __name__ == '__main__':
    t = test()
    t.samename(1)
