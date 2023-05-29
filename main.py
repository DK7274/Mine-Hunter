import pygame
import random

#variables for mine randomiser
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

pygame.init() # initializing pygame

#button variables
button_dark = (1, 73, 128)
button_light = (2, 127, 222)




#section for sprite images to be defined
mineImage = pygame.image.load("Images\mine.png")
mineImage = pygame.transform.scale(mineImage,(20,20)) #squaring and making image smaller


#displaying window with height 1000 and width 950, with a blue background
screen = pygame.display.set_mode((700,700))
backColour = (0,26,46)
screen.fill(backColour)
pygame.display.flip()
width = screen.get_width()
height = screen.get_height()

#bool that checks if game quit or not
gameQuit = False

#creating mine object
class mine(object): #tells pyhton object
    def __init__(self,x,y,width,height):   #the def function defines what code will run when a new type of this object is created.
        self.x= x
        self.y = y
        self.width = width
        self.height = height
    def draw(self,screen):
        screen.blit(mineImage,(self.x,self.y))

def mineSpawn():
    global mineCount
    global yMines
    xMines = [1,1,1,1,1,1,1,1,1,1] #array for x mines to come from
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
    print(xMines)
    print(yMines)

#class button(object):

#def gameBoard(): #displays game screen

#def helpScreen(): #displays help screen with tutorial

#def menuScreen(): #displays menu screen to start game, open help screen





gameStart = False #variable that determines if the actual game play on menu screen has been pressed

# keep running until quit
while not gameQuit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #
            gameQuit = True
    #if gameStart == True:
    #    gameBoard()
    #else:
        #menuScreen
