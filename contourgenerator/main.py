import math
import random
import matplotlib.pyplot as plt
import numpy
import re, sys

data_file = open("ex.csv", "r")
data_list = [i.split(";") for i in data_file.readlines()]
convert_list = []
counter = 0
while counter < len(data_list):
    convert_list.append([])
    for k in data_list[counter]:
        convert_list[counter].append(float(k))
    counter += 1

for i in convert_list:
    plt.plot(i[0], i[1], "r*")
    

N = int(len(convert_list)) # number of primes wanted (from command-line)
l = []

for i in range(N):
    l.append(random.randint(1000, 10000000))

for i in range(N):
    convert_list[i].append(l[i])


    
a = 0
weight = 2

arrayOfCountourPoints = []
excludeRepeat = []

while a < len(convert_list):
    c = 0
    while c < len(convert_list):
        if a == c:
            aaa = 0
        # elif convert_list[a][3] + convert_list[c][3] in excludeRepeat:
        #     asdagfa = 0
        else:
            difference = abs(convert_list[a][2] - convert_list[c][2])
            countOfSlices = int(difference/weight)
            for i in range(countOfSlices):
                if i != 1.0:
                    x = [convert_list[a][0], convert_list[c][0]]
                    y = [convert_list[a][1], convert_list[c][1]]
                    # print(((i+1)*weight)/difference)
                    coef = (((i+1)*weight)/difference)
                    calculateX = (x[0] + coef*x[1])/(1+coef)
                    calculateY = (y[0] + coef*y[1])/(1+coef)
                    calculateZ = convert_list[a][2] + (weight + i*(((convert_list[a][2] - convert_list[c][2])/difference)))
                    arrayOfCountourPoints.append([calculateX, calculateY, calculateZ])
                else:
                    asdad = 0
            excludeRepeat.append(convert_list[a][3] + convert_list[c][3])
        c += 1
    a += 1

newArrayCP = []
lenArrayCP = len(arrayOfCountourPoints)-1

for i in range(lenArrayCP):
    try:
        if arrayOfCountourPoints[i][0] in newArrayCP:
            del arrayOfCountourPoints[i]
        else:
            newArrayCP.append(arrayOfCountourPoints[i][0])
    except IndexError:
        break
    
print(len(arrayOfCountourPoints))

ArrayOfValues = [min([i[2] for i in convert_list]), max([i[2] for i in convert_list])]
betweenMaxAndMin = [i+ArrayOfValues[0] for i in range(int(ArrayOfValues[1]-ArrayOfValues[0])+1)]

sameValues = [[] for i in range(int(ArrayOfValues[1]-ArrayOfValues[0])+1)]
print(sameValues)

for i in range(len(sameValues)-1):
    for k in arrayOfCountourPoints:
        if k[2] == betweenMaxAndMin[i]:
            sameValues[i].append(k)
    
for i in range(1):
    while len(sameValues[i]) > 1:
        currentLen = len(sameValues[i])-1
        xbxa = sameValues[i][0][0] - sameValues[i][currentLen][0]
        ybya = sameValues[i][0][1] - sameValues[i][currentLen][1]
        curenntLowestDistance = math.sqrt((xbxa*xbxa)+(ybya*ybya))
        currentSmallestElement = currentLen
        while currentLen > 0:
            ybyj = sameValues[i][0][1] - sameValues[i][currentLen][1]
            if curenntLowestDistance > math.sqrt((xbxa*xbxa)+(ybyj*ybyj)):
                currentSmallestElement = math.sqrt((xbxa*xbxa)+(ybyj*ybyj))
                currentSmallestElement = currentLen
            currentLen += -1
        xval = [sameValues[i][0][0], sameValues[i][currentSmallestElement][0]]
        yval = [sameValues[i][0][1], sameValues[i][currentSmallestElement][1]]
        print(xval)
        plt.plot(xval, yval)
        pushOnTop = sameValues[i][currentSmallestElement]
        del sameValues[i][currentSmallestElement]
        del sameValues[i][0]
        sameValues[i].insert(0, pushOnTop)
            
    

    

# kak = 0
# while kak < len(arrayOfCountourPoints):
#     plt.scatter(arrayOfCountourPoints[kak][0], arrayOfCountourPoints[kak][1], s=0.2)
#     print(f"iter num: {kak}")
#     kak += 1
    
plt.show()
    


