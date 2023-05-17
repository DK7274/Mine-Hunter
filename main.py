import pygame

# initializing pygame
pygame.init()

# displaying a window of height
# 500 and width 400
screen = pygame.display.set_mode((1000, 950))
backColour = (0,26,46)
screen.fill(backColour)
pygame.display.flip()

#bool that checks if game quit or not
gameQuit = False

# keep running until quit
while not gameQuit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #
            gameQuit = True