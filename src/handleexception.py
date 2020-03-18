import re

def handle(test_list):
    alarm = None
    try:
        for element in test_list:
            if element == 1:
                alarm = test_list.index(element)
        print(alarm)
    except ValueError:
        print("metric error")

if __name__ == '__main__':
    test_list = [0,2,3,4,5]
    handle(test_list)

