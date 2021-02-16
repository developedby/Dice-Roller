import random
import sys

def diceroller(dicelist):
    diceResults = []
    diceRolls = []
    dicelist = dicelist.split()
    for i, dicecall in enumerate(dicelist):
        diceNumber = 0
        diceSides = 0
        diceSum = 0
        dicelist[i] = dicelist[i].split('d')
        diceNumber = int(dicelist[i][0])
        diceSides = int(dicelist[i][1])
        for number in range(diceNumber):
            result = random.randint(1, diceSides)
            diceSum += result
            diceRolls.append(str(result))
        diceResults.append(str(diceSum)) 
    return ' '.join(diceResults) + ":  " + ' '.join(diceRolls)

for arg in sys.argv[1:]:
    print(diceroller(arg))
    
