import random
import sys

def diceroller(dice):
    dice = dice.split('d')
    diceNumber = int(dice[0])
    diceSides = int(dice[1])

    diceRolls = []
    diceSum = 0
    for number in range(diceNumber):
        result = random.randint(1, diceSides)
        diceSum += result
        diceRolls.append(str(result))
    return f"{diceSum}: {' '.join(diceRolls)}"

for arg in sys.argv[1:]:
    print(diceroller(arg))
