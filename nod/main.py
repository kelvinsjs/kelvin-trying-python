import random

i = 0
array = []
easyArray = [2, 3, 5, 7, 11, 13, 17, 19]

def calc(a):
    k = 0
    result = ""
    if a == 1:
        print(result)
        return a
    else:
        if k < 1:
            for i in easyArray:
                if a % i == 0:
                    result = result + " * " + str(i)
                    k = k + 1
                    print(i)
                    calc(a / i)

calc(44)