class ReturnValueForStatic:
    @staticmethod
    def plusOne(value):
        return value + 1



if __name__ == '__main__':
    a = ReturnValueForStatic.plusOne(1)
    print(a)