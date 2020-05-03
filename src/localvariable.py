def fff(tst_list):
    alarm = None
    for element in tst_list:
        if element == 1:
            alarm = tst_list.index(element)

    print(alarm)



if __name__ == '__main__':
    tst_list = [1,2,3,4,4,5,4,3,5,6]

    fff(tst_list)