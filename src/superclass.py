class father:
    def __init__(self, name):
        self.name = name


class son(father):
    def __init__(self, name, age):
        father.__init__(self, name)
        self.age = age



if __name__ == '__main__':
    f = father("1")
    s = son("2", 13)

    print(s.age)
