def cutIntoSection(uplimit, formatDict):
    sectionList = []
    start = 0
    while start < len(formatDict):
        tempstart = start
        tempcount = 0
        sublist = []
        while tempstart < len(formatDict) and tempcount < uplimit:
            sublist.append(formatDict[tempstart])
            tempstart += 1
            tempcount += 1

        start = tempstart
        sectionList.append(sublist)

    return sectionList


if __name__ == '__main__':
    a = [1,2,3,43,6,7,8,9,96,75,4,3,23,2,5,7]

    print(cutIntoSection(3,a))