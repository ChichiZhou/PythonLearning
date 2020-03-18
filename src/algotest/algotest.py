def test(file_names):

    file_names_list = []
    temp = 0
    while temp < len(file_names):
        count = 0
        temp_list = []
        while count < 2 and temp < len(file_names):
            file_name = file_names[temp]
            temp_list.append(file_name)
            count += 1
            temp += 1
        file_names_list.append(temp_list)

    return file_names_list


if __name__ == '__main__':
    a = [1,2,3,45,3,54,3,54,3,5,3,5,3]
    print(test(a))
