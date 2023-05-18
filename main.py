import pygame

# initializing pygame
pygame.init()


#section for sprite images to be defined
mineImage = pygame.image.load("Images\mine.png")


#displaying window with height 1000 and width 950, with a blue background
screen = pygame.display.set_mode((1000,950))
backColour = (0,26,46)
screen.fill(backColour)
pygame.display.flip()

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
mine1 =mine(100,100,100,100)
mine2 = mine(200,200,50,50)
mine1.draw(screen)
pygame.display.update()
#def mineSpawn():


# keep running until quit
while not gameQuit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #
            gameQuit = True