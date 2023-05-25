import random
import array as arr

xMines = [1,1,1,1,1,1,1,1,1,1]

mineCount = 20

yCount = 10

mineRow1 = [0,0,0,0,0,0,0,0,0,0]
mineRow2 = [0,0,0,0,0,0,0,0,0,0]
mineRow3 = [0,0,0,0,0,0,0,0,0,0]
mineRow4 = [0,0,0,0,0,0,0,0,0,0]
mineRow5 = [0,0,0,0,0,0,0,0,0,0]
mineRow6 = [0,0,0,0,0,0,0,0,0,0]
mineRow7 = [0,0,0,0,0,0,0,0,0,0]
mineRow8 = [0,0,0,0,0,0,0,0,0,0]
mineRow9 = [0,0,0,0,0,0,0,0,0,0]
mineRow0 = [0,0,0,0,0,0,0,0,0,0]

yMines = [mineRow1,mineRow2,mineRow3,mineRow4,mineRow5,mineRow6,mineRow7,mineRow8,mineRow9,mineRow0]


while mineCount > 0:
    for n in range(0,len(xMines)):
        mineChance = random.randint(0,10)
        if mineChance == 1:
            if mineCount > 0:
                mineCount -= 1
                xMines[n] += 1

print(xMines)

m = 0

mineDisplay = 0

for n in range(0,len(yMines)):
    mineCount = xMines[n]
    while mineCount > 0:
        for m in range(0,len(yMines[n])):
            if yMines[n][m] == 0:
                mineChance = random.randint(0,10)
                if mineChance == 1:
                    if mineCount > 0:
                        yMines[n][m] += 1
                        mineCount -= 1




print(yMines)

