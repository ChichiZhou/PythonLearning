def testone(a, b, *c):
    print(a)
    print(b)
    if len(c) > 0:
        print("the value of c is {}".format(c[0]))

if __name__ == '__main__':
    # testone(1, 2)

    testone(1, 2, 0)

    testone(1,2)