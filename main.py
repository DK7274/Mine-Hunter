import pygame
import random


pygame.init() # initializing pygame

mouseX,mouseY = (0,0) #sets mouse coordinate

LEFT = 1 #variables for detection of which mouse button is pressed
RIGHT = 3

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

#variables for colours that don't need to be in functions
text_color = (0, 0, 0)
flag_color = (237, 19, 19)
button_light = (2, 127, 222)
title_text_color = (25, 40, 156)
button_color = (25, 40, 156)
button_over_color = (6, 17, 99)

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
    global yButtonState

    #variables for mine randomiser
    mineCount = 20 #overall amound of mines

    mineRow1 = [0,0,0,0,0,0,0,0] #set of arrays for mine placement
    mineRow2 = [0,0,0,0,0,0,0,0]
    mineRow3 = [0,0,0,0,0,0,0,0]
    mineRow4 = [0,0,0,0,0,0,0,0]
    mineRow5 = [0,0,0,0,0,0,0,0]
    mineRow6 = [0,0,0,0,0,0,0,0]
    mineRow7 = [0,0,0,0,0,0,0,0]
    mineRow8 = [0,0,0,0,0,0,0,0]

    yMines = [mineRow1,mineRow2,mineRow3,mineRow4,mineRow5,mineRow6,mineRow7,mineRow8]

    #array that holds mine arrays within it to be called

    buttonState1 = [0,0,0,0,0,0,0,0] #set of arrays for button detection
    buttonState2 = [0,0,0,0,0,0,0,0]
    buttonState3 = [0,0,0,0,0,0,0,0]
    buttonState4 = [0,0,0,0,0,0,0,0]
    buttonState5 = [0,0,0,0,0,0,0,0]
    buttonState6 = [0,0,0,0,0,0,0,0]
    buttonState7 = [0,0,0,0,0,0,0,0]
    buttonState8 = [0,0,0,0,0,0,0,0]

    yButtonState = [buttonState1,buttonState2,buttonState3,buttonState4,buttonState5,buttonState6,buttonState7,buttonState8]



    xMines = [0,0,0,0,0,0,0,0] #array for x mines to come from
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


def clearedSquare(): #clears the square then subsequently checks surrounding squares to give a number
    pygame.draw.rect(screen,backColour,button_rect)
    yButtonState[clickY][clickX] = 1
    surround_font = pygame.font.SysFont("impact",40)
    mineDetectCount = 0
    if clickY > 0: #have to split them all up into seperate if statements because otherwise it rolls over through to the other edge
        if yMines[clickY - 1][clickX] == 1:
            mineDetectCount += 1
        if clickX > 0:
            if yMines[clickY - 1][clickX - 1] == 1:
                mineDetectCount += 1
        if clickX < 7:
            if yMines[clickY - 1][clickX + 1] == 1:
                mineDetectCount += 1
    if clickY < 7:
        if yMines[clickY + 1][clickX] == 1:
            mineDetectCount += 1
        if clickX > 0:
            if yMines[clickY + 1][clickX - 1] == 1:
                mineDetectCount += 1
        if clickX < 7:
            if yMines[clickY + 1][clickX + 1] == 1:
                mineDetectCount += 1
    if clickX > 0:
        if yMines[clickY][clickX - 1] == 1:
            mineDetectCount += 1
    if clickX < 7:
        if yMines[clickY][clickX + 1] == 1:
            mineDetectCount += 1
    if mineDetectCount > 0:
        surround_text = surround_font.render(str(mineDetectCount),True,flag_color)
        screen.blit(surround_text,(button_rect[0] + 20,button_rect[1] + 5))
    print("surrouding mines" + str(mineDetectCount))
    print("clearedSquare run")

def gameOverWindow():
    global gameOver
    global mouseX
    global mouseY
    game_over_rect = (205,200,350,350)
    quit_rect = (250,390,100,75)
    restart_rect = (410,390,100,75)
    pygame.draw.rect(screen, (0, 90, 158),game_over_rect)
    game_over_font = pygame.font.SysFont("impact",40)
    restart_quit_font = pygame.font.SysFont("impact",20)
    quit_text = restart_quit_font.render("QUIT",True,text_color)
    restart_text = restart_quit_font.render("RESTART",True,text_color)
    game_over_text = game_over_font.render("GAME OVER",True,flag_color)
    screen.blit(game_over_text,(game_over_rect[0] + game_over_text.get_width() / 2,220))

    endWindow = False
    while endWindow == False: #loop preventing buttons on the board to be pressed, just the restart and the quit buttons
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseX,mouseY = event.pos
                if (quit_rect[0] <= mouseX <= quit_rect[0] + quit_rect[2] and  # quit buton on the game over pop-up
                        quit_rect[1] <= mouseY <= quit_rect[1] + quit_rect[3]):
                    gameOver = True
                    endWindow = True
                if (restart_rect[0] <= mouseX <= restart_rect[0] + restart_rect[2] and  # restart button on the game over pop-up, resets all mine positions and states
                        restart_rect[1] <= mouseY <= restart_rect[1] + restart_rect[3]):
                    endWindow = True
                    gameBoard()
            if event.type == pygame.MOUSEMOTION:
                mouseX, mouseY = event.pos
        if (quit_rect[0] <= mouseX <= quit_rect[0] + quit_rect[2] and
                quit_rect[1] <= mouseY <= quit_rect[1] + quit_rect[3]):
            pygame.draw.rect(screen, button_over_color, quit_rect)
        elif (restart_rect[0] <= mouseX <= restart_rect[0] + restart_rect[2] and
                restart_rect[1] <= mouseY <= restart_rect[1] + restart_rect[3]):
            pygame.draw.rect(screen, button_over_color, restart_rect)
        else:
            pygame.draw.rect(screen, button_light, quit_rect)
            pygame.draw.rect(screen, button_light, restart_rect)
        screen.blit(quit_text, (quit_rect[0] + 30, quit_rect[1] + 25))
        screen.blit(restart_text, (restart_rect[0] + 20, restart_rect[1] + 25))

        pygame.display.update()



def gameBoard(): #displays game screen
    global gameStart
    global mouseX
    global mouseY
    global button_rect
    global clickX
    global clickY
    global gameOver
    gameOver = False
    flagCount = 20
    mineSpawn() #randomises mines
    # setting up variables for displaying timer, flag counter, buttons#
    screen.fill(backColour)
    game_font = pygame.font.SysFont("impact", 20)
    quit_rect = [500,20,70,50]
    quit_text = game_font.render("QUIT",True, text_color)

    #draws score text, quit button onto the screen
    pygame.draw.rect(screen, button_light, quit_rect)
    screen.blit(quit_text,(quit_rect[0] + (70 - quit_text.get_width()) / 2,
                              quit_rect[1] + (50 / 2 - quit_text.get_height() / 2)))
    flagCount_text = game_font.render(str(flagCount), True, flag_color)
    screen.blit(flagCount_text, (330, 20))

    #variables for button dimesnsions and placement
    button_width = 60
    button_height = 60
    buttonX = 100
    buttonY = 100
    buttonSpacing = 10
    buttonXCount = 8
    buttonYCount = 8
    clickX = 0
    clickY = 0
    #actual loop to draw buttons#
    #loops through 8 times repeating on X axis, then repeats that sequence 8 times down the Y axis
    while buttonYCount > 0:
        while buttonXCount > 0:
            button_rect = (buttonX,buttonY,button_width,button_height)
            pygame.draw.rect(screen,button_light,button_rect)
            buttonX = buttonX + button_width + buttonSpacing
            buttonXCount -= 1
        buttonX = 100
        buttonXCount = 8
        buttonY = buttonY + button_height + buttonSpacing
        buttonYCount -= 1

    buttonX = 100 #resets coordinates of buttons back to default position
    buttonY = 100


    while gameOver == False: #main loop for game, everything will on the game board will happen in here
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseX,mouseY = event.pos
                if (quit_rect[0] <= mouseX <= quit_rect[0] + quit_rect[2] and #quit buton on the game board
            quit_rect[1] <= mouseY <= quit_rect[1] + quit_rect[3]):
                    gameOver = True
                print("clicked")
                button_rect = [buttonX,buttonY,button_width,button_height]
                while clickY < 8 and gameOver is False: #left click for remove box checking on the y-axis
                    button_rect[1] = buttonY
                    if (button_rect[1] <= mouseY <= button_rect[1] + button_rect[3]): #checking whether the location is in the correct y-axis
                        print("correct line")
                        while clickX < 8 and gameOver is False:
                            button_rect[0] = buttonX
                            if button_rect[0] <= mouseX <= button_rect[0] + button_rect[2]: #checking whether click location is in the correct x-axis
                                print("correct square")
                                if event.button == LEFT: #checking what happens on the left click, clear square, game over, or nothing
                                    if yMines[clickY][clickX] == 1:
                                        print("game Over, mine clicked!")
                                        gameOverWindow()
                                    elif yButtonState[clickY][clickX] == 0:
                                        clearedSquare()
                                    else:
                                        print("square already cleared/flagged")
                                elif event.button == RIGHT:
                                    print('right clicked')
                                    if yButtonState[clickY][clickX] == 0 and flagCount > 0:
                                        pygame.draw.rect(screen,flag_color,button_rect)
                                        print("square flagged")
                                        yButtonState[clickY][clickX] = 2
                                        flagCount -= 1
                                    elif yButtonState[clickY][clickX] == 1:
                                        print("square already cleared")
                                    elif yButtonState[clickY][clickX] == 2:
                                        print("unflagging square")
                                        pygame.draw.rect(screen,button_light,button_rect)
                                        flagCount += 1
                                        yButtonState[clickY][clickX] = 0
                                    else:
                                        print("out of flags")
                                    flagCount_text = game_font.render(str(flagCount), True, flag_color)
                                    flagRefreshRect = [330,20,70,50]
                                    pygame.draw.rect(screen,backColour,flagRefreshRect)
                                    screen.blit(flagCount_text, (330, 20))

                                break
                            else:
                                buttonX = buttonX + button_width + buttonSpacing
                                clickX += 1
                            print(str(clickX))
                        clickX = 0
                        buttonX = 100
                        break
                    else:
                        buttonY = buttonY + button_height + buttonSpacing
                        clickY += 1
                    print(str(clickY))
                clickY = 0
                buttonY = 100


        pygame.display.update()
    gameStart = False

def guideScreen(): #displays help screen with tutorial
    global guideOpen
    print('guide')
    guideOpen = False
def menuScreen(): #displays menu screen to start game, open help screen, and quit
    global mouseX
    global mouseY
    global gameStart
    global gameQuit
    global guideOpen
    #blitting the menu window#
    screen.fill((0,26,46))
    #variables for buttons
    button_width = 200
    button_height = 100
    play_rect = [(screen.get_width() - button_width) / 2 , 250,button_width, button_height]
    guide_rect = [(280-button_width),400,button_width,button_height]
    quit_rect = [(560-button_width),400,button_width,button_height]
    #fonts and texts for the buttons
    button_font = pygame.font.SysFont("impact",20)
    play_text = button_font.render("PLAY", True, text_color)
    guide_text = button_font.render("GUIDE",True,text_color)
    quit_text = button_font.render("QUIT",True, text_color)
    #font and text for the title
    title_font = pygame.font.SysFont("impact", 50)
    title_text = title_font.render("MINEHUNTER", True, title_text_color)

    #draws the button rectangles onto the screen
    pygame.draw.rect(screen, button_color, play_rect)
    pygame.draw.rect(screen, button_color, quit_rect)
    pygame.draw.rect(screen, button_color, guide_rect)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN: #event triggered on clicking the mouse
            print(event.button)
            mouseX,mouseY = event.pos #get mouse pos
            if(play_rect[0] <= mouseX <= play_rect[0] + play_rect[2] and
            play_rect[1] <= mouseY <= play_rect[1] + play_rect[3]):
                gameStart = True #if click on the button then you start the game#
                print("gameStart")
            elif (quit_rect[0] <= mouseX <= quit_rect[0] + quit_rect[2] and
            quit_rect[1] <= mouseY <= quit_rect[1] + quit_rect[3]):
                gameQuit = True #if clcik on button then game quits
            elif (guide_rect[0] <= mouseX <= guide_rect[0] + guide_rect[2] and
                  guide_rect[1] <= mouseY <= guide_rect[1] + guide_rect[3]):
                guideOpen = True #if click on button then open the guide
        if event.type == pygame.MOUSEMOTION: #event triggered on mouse movement
            mouseX,mouseY = event.pos
    #these three if statements change the color of seperate buttons if they are moused over
    if (play_rect[0] <= mouseX <= play_rect[0] + play_rect[2] and
            play_rect[1] <= mouseY <= play_rect[1] + play_rect[3]):
        pygame.draw.rect(screen, button_over_color, play_rect)
    elif (quit_rect[0] <= mouseX <= quit_rect[0] + quit_rect[2] and
            quit_rect[1] <= mouseY <= quit_rect[1] + quit_rect[3]):
        pygame.draw.rect(screen,button_over_color,quit_rect)
    elif (guide_rect[0] <= mouseX <= guide_rect[0] + guide_rect[2] and
            guide_rect[1] <= mouseY <= guide_rect[1] + guide_rect[3]):
        pygame.draw.rect(screen,button_over_color,guide_rect)
    #sets the text on the screen
    screen.blit(play_text, (play_rect[0] + (button_width - play_text.get_width()) / 2,
                              play_rect[1] + (button_height / 2 - play_text.get_height() / 2)))
    screen.blit(quit_text,(quit_rect[0] + (button_width - quit_text.get_width()) / 2,
                              quit_rect[1] + (button_height / 2 - quit_text.get_height() / 2)))
    screen.blit(guide_text, (guide_rect[0] + (button_width - guide_text.get_width()) / 2,
                            guide_rect[1] + (button_height / 2 - guide_text.get_height() / 2)))

    screen.blit(title_text,(356.625,100))

    pygame.display.update()





gameStart = False #variable that determines if the actual game play on menu screen has been pressed
guideOpen = False

# keep running until quit
while not gameQuit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameQuit = True
    if gameStart == True:
        gameBoard()
    elif guideOpen == True:
        guideScreen()
    else:
        menuScreen()
