def divide(file_names):

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

def conqure(file_names_list):
    if len(file_names_list) == 1:
        return file_names_list[0]
    temp = 0
    file_names_merge = []
    while temp < len(file_names_list):
        count = 0
        temp_list = []
        while count < 2 and temp < len(file_names_list):
            file_name = file_names_list[temp]
            temp_list.append(file_name)
            count += 1
            temp += 1

        result = create_file(temp_list)
        file_names_merge.append(result)

    # print(file_names_merge)

    return conqure(file_names_merge)

def create_file(temp_list):
    result = []
    for element in temp_list:
        result += element

    return result

if __name__ == '__main__':
    a = [1,2,3,45,3,54,3,54,3,5,3,5,3]

    b = divide(a)

    print(b)

    c = conqure(b)

    print(c)

    print(len(c))
