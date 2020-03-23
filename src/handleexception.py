import re

def handle(var):
    alarm = None
    try:
        return int(var)
    except ValueError:
        print("metric error")

def throw_exception(var):
    try:
        if var == 0:
            raise ValueError
    except ValueError:
        print("f")

if __name__ == '__main__':
    # test_list = [0,2,3,4,5]
    throw_exception(0)


