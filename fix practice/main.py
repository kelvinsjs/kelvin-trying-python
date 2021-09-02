import random
import math

lengthArr = [57.08, 16.36, 66.69, 62.89, 78.18, 39.69, 121.57]
radArray = [5.417618, 5.223305, 4.318614, 2.25098, 3.313275, 1.956456, 0.396277]
count = 0
while count < 100:
    i = 0
    newLengthArr = []
    getXArray = []
    getYArray = []
    while i < len(lengthArr):
        if lengthArr[i] != 121.57:
            newLengthArr.append(lengthArr[i] + (random.randrange(-20, 20)) * 0.01)
            getXArray.append(newLengthArr[i] * math.cos(radArray[i]))
            getYArray.append(newLengthArr[i] * math.sin(radArray[i]))
        else:
            newLengthArr.append(lengthArr[i])
            getXArray.append(newLengthArr[i] * math.cos(radArray[i]))
            getYArray.append(newLengthArr[i] * math.sin(radArray[i]))
        i = i + 1
    k = 0
    sumGetXArray = sum(getXArray)
    sumGetYArray = sum(getYArray)
    getPogreshnost: float = sum(newLengthArr) / math.sqrt(((sumGetXArray*sumGetXArray + sumGetYArray*sumGetYArray)))
    finalText = ""
    while k < len(newLengthArr):
        finalText = finalText + ("Dlinna " + str(k + 1) + " : " + str(newLengthArr[k]) + "\n")
        k = k+1
    if getPogreshnost > 3000:
        print(finalText + "\n" + str(getPogreshnost) + "\n _______________________________________")
    count = count + 1
