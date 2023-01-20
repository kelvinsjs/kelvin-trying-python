from chanceArray import chanceArray, multiplyArray
import random
import numpy as np
from collections import Counter


possibilities = [0.5, 50, 47, 44, 41, 38, 35, 32, 26, 23]

def getAnElement():
    index = random.randint(0, (len(chanceArray)-1))
    return chanceArray[index]

mainArray = []

mainArray = [random.random() for i in range(30)]

for k in range(len(mainArray)):
    if mainArray[k] < 0.5:
        mainArray[k] = getAnElement()

for k in range(len(mainArray)):
    if mainArray[k] < 1:
        mainArray[k] = 0.5
            
gameState = "process"
currentBet = 100
currentWin = 0
betRatio = [0.5, 0.8, 1, 1.6, 2, 3, 4, 5, 10, 20]
multiplyArrayLength = len(multiplyArray)
countOfIterations = 0

while gameState == "process":
    countOfPlays = 0
    multiplyBonus = 1
    thisTurnWin = 0
    print(f"Умножение: {multiplyBonus}")
    a = dict(Counter(mainArray))
    print(a)
    for key in a:
        if int(key) == 29:
            for i in range(a[key]):
                increaseBonus = multiplyArray[random.randrange(0, multiplyArrayLength)]
                multiplyBonus += increaseBonus
        if int(a[key]) > 6.99 and int(a[key]) != 29:
            countOfPlays += 1
            thisTurnWin += currentBet*(betRatio[possibilities.index(key)])
            print(f"Сумма: {thisTurnWin}")
            for i in range(len(mainArray)):
                if mainArray[i] == key:
                    if random.random() > 0.35:
                        mainArray[i] = getAnElement()
                    else:
                        mainArray[i] = 0.5
        if thisTurnWin == 0:
            multiplyBonus = 1
    currentWin += thisTurnWin*multiplyBonus  
    print(f"Win = {thisTurnWin} * {multiplyBonus} = {currentWin}")      
    print(mainArray)
    if countOfPlays == 0:
        gameState = "stop"
        print(f"mp bonus = {multiplyBonus}")
        print(f"Итого: {currentWin}")
                    