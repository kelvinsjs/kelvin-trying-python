import random
import math

lengthArr = [19.21, 14.97, 28.02, 22.02, 74.3, 35.1, 97.48, 28.57]
radArray = [5.28585, 4.76937, 3.60451, 3.52693, 3.56262, 2.00125, 0.40215, 0.39628]

count = 0
while count < 10:
    if count % 500 == 0:
        print("Now {} test".format(count))
    i = 0
    newLengthArr = []
    getXArray = []
    getYArray = []
    startCoordX = 5575394.851
    startCoordY = 3369846.31
    countOfZeros = 100
    while i < len(lengthArr):
        if lengthArr[i] != 28.57:
            newLengthArr.append(lengthArr[i] + (random.randrange(int(-1.9 * (countOfZeros*0.1)), int(1.9 * (countOfZeros*0.1)))) * 1/countOfZeros)
            newStep = [round(newLengthArr[i] * math.cos(radArray[i]), 3), round(newLengthArr[i] * math.sin(radArray[i]), 3)]
            getXArray.append(newStep[0])
            startCoordX = round(startCoordX + newStep[0], 3)
            startCoordY = round(startCoordY + newStep[1], 3)
            getYArray.append(newStep[1])
        else:
            newLengthArr.append(lengthArr[i]+ (random.randrange(-19, 19)) * 0.01)
            newStep = [newLengthArr[i] * math.cos(radArray[i]), newLengthArr[i] * math.sin(radArray[i])]
            getXArray.append(newStep[0])
            getYArray.append(newStep[1])
        i = i + 1
    k = 0
    # print(newLengthArr)
    if sum(getXArray) == 0 and sum(getYArray) == 0:
        getFault: float = -1
    else:
        getFault: float = sum(newLengthArr) / math.sqrt(((sum(getXArray) ** 2 + sum(getYArray) ** 2)))
    # print(startCoordX, startCoordY)
    print(getFault)
    if abs(startCoordX - 5575394.851) <= 50 and abs(startCoordY - 5575394.851) <= 50:
        finalText = "Popytka podbora nomer {} \n ____________________ \n".format(count)
        while k < len(newLengthArr):
            finalText = finalText + ("\n Dlinna " + str(k + 1) + " : " + str(newLengthArr[k]) + "\n")
            k = k + 1
        if getFault > 0 or getFault == -1:
            print(finalText + "\nPogreshnost = 1/" + str(getFault) + "\n _______________________________________")
            print("\n X = {}, Y = {} \n _________________________________________ \n".format(startCoordX, startCoordY))
        else:
        	print(getFault)
    count = count + 1
