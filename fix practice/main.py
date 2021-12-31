import random
import math

lengthArr = [37.90, 72.91, 45.40, 43.20]
radArray = [0.139626340159546, 4.60775649172763, 2.56127067730168, 1.38884575227449]

count = 0
while count < 10000:
    if count % 500 == 0:
        print("Now {} test".format(count))
    i = 0
    newLengthArr = []
    getXArray = []
    getYArray = []
    startCoordX = 1000
    startCoordY = 2000
    countOfZeros = 100
    while i < len(lengthArr):
        if lengthArr[i] != 121.57:
            newLengthArr.append(lengthArr[i] + (random.randrange(-0.9 * (countOfZeros*0.1), 0.9 * (countOfZeros*0.1))) * 1/countOfZeros)
            newStep = [round(newLengthArr[i] * math.cos(radArray[i]), 3), round(newLengthArr[i] * math.sin(radArray[i]), 3)]
            getXArray.append(newStep[0])
            startCoordX = round(startCoordX + newStep[0], 3)
            startCoordY = round(startCoordY + newStep[1], 3)
            getYArray.append(newStep[1])
        else:
            newLengthArr.append(lengthArr[i]+ (random.randrange(-900000000, 900000000)) * 0.000000000001)
            newStep = [newLengthArr[i] * math.cos(radArray[i]), newLengthArr[i] * math.sin(radArray[i])]
            getXArray.append(newStep[0])
            getYArray.append(newStep[1])
        i = i + 1
    k = 0
    if sum(getXArray) == 0 and sum(getYArray) == 0:
        getFault: float = -1
    else:
        getFault: float = sum(newLengthArr) / math.sqrt(((sum(getXArray) ** 2 + sum(getYArray) ** 2)))
    if abs(startCoordX - 1000) <= 1 and abs(startCoordY - 2000) <= 1:
        finalText = "Popytka podbora nomer {} \n ____________________ \n".format(count)
        while k < len(newLengthArr):
            finalText = finalText + ("\n Dlinna " + str(k + 1) + " : " + str(newLengthArr[k]) + "\n")
            k = k + 1
        if getFault > 2000 or getFault == -1:
            print(finalText + "\nPogreshnost = 1/" + str(getFault) + "\n _______________________________________")
            print("\n X = {}, Y = {} \n _________________________________________ \n".format(startCoordX, startCoordY))
    count = count + 1
