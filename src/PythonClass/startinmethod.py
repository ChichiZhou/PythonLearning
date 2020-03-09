'''
可变参数（或者叫可选参数？）
'''
def createInputMap(a, *parameterList):
    b, c = parameterList

    d = {"A": a, "B":b, "C":c}
    return d

if __name__ == '__main__':
    createInputMap([1])
