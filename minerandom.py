import random
xMines = [1,1,1,1,1,1,1,1,1,1] #array for n umber of mines down the x Axis

mineCount = 20 #overall amound of mines

mineRow1 = [0,0,0,0,0,0,0,0,0,0] #set of arrays for mine placement
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
#array that holds mine arrays within it to be called

while mineCount > 0: #sequence to sort the extra 20 mines into different X axis
    for n in range(0,len(xMines)): #repeats through the array until all mines are used
        mineChance = random.randint(0,10) #1 in 10 chance of mine being placed per slot
        if mineChance == 1:
            if mineCount > 0:
                mineCount -= 1
                xMines[n] += 1

for n in range(0,len(yMines)): #sorts through each mine array X axis
    mineCount = xMines[n]
    while mineCount > 0: #as long as mine count isn't depleted
        for m in range(0,len(yMines[n])): #sorts through each individual x axis array
            if yMines[n][m] == 0: #if no mine there
                mineChance = random.randint(0,10) #1 in 10 chance of mine being placed
                if mineChance == 1:
                    if mineCount > 0:
                        yMines[n][m] += 1
                        mineCount -= 1

print(yMines)
