import random
import math

lengthArr = [57.08, 16.36, 66.69, 62.89, 78.18, 39.69, 121.57]
radArray = [5.417618, 5.223305, 4.318614, 2.25098, 3.313275, 1.956456, 0.396277]

count = 0
while count < 1000000:
    if count % 50000 == 0:
        print("Now {} test".format(count))
    i = 0
    newLengthArr = []
    getXArray = []
    getYArray = []
    startCoordX = 5575394.851
    startCoordY = 3369846.31
    while i < len(lengthArr):
        if lengthArr[i] != 121.57:
            newLengthArr.append(lengthArr[i] + (random.randrange(-4, 3)) * 0.01)
            newStep = [round(newLengthArr[i] * math.cos(radArray[i]), 3), round(newLengthArr[i] * math.sin(radArray[i]), 3)]
            getXArray.append(newStep[0])
            startCoordX = round(startCoordX + newStep[0], 3)
            startCoordY = round(startCoordY + newStep[1], 3)
            getYArray.append(newStep[1])
        else:
            newLengthArr.append(lengthArr[i])
            newStep = [newLengthArr[i] * math.cos(radArray[i]), newLengthArr[i] * math.sin(radArray[i])]
            getXArray.append(newStep[0])
            getYArray.append(newStep[1])
        i = i + 1
    k = 0
    if sum(getXArray) == 0 and sum(getYArray) == 0:
        getFault: float = -1
    else:
        getFault: float = sum(newLengthArr) / math.sqrt(((sum(getXArray) ** 2 + sum(getYArray) ** 2)))
    if abs(startCoordX - 5575282.734) <= 0.001 and abs(startCoordY - 3369799.397) <= 0.001:
        finalText = "Popytka podbora nomer {} \n ____________________ \n".format(count)
        while k < len(newLengthArr):
            finalText = finalText + ("\n Dlinna " + str(k + 1) + " : " + str(newLengthArr[k]) + "\n")
            k = k + 1
        if getFault > 10000 or getFault == -1:
            print(finalText + "\nPogreshnost = 1/" + str(getFault) + "\n _______________________________________")
            print("\n X = {}, Y = {} \n _________________________________________ \n".format(startCoordX, startCoordY))
    count = count + 1
