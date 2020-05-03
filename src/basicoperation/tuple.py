a = (1,2)

b = (1,)

if __name__ == '__main__':
    print(a[0])
    print(b[1] if len(b) == 2 else None)