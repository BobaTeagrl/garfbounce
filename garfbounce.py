import pygame
import time
import random

# startuo shit
logo = pygame.image.load('garf.jpeg')
BG_COLOR = (201, 8, 182)


# window size
window_y = 1280
window_x = 720

# defining colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)




#setup 
pygame.init()
screen = pygame.display.set_mode((window_y, window_x))
pygame.display.set_caption('garfbounce')
clock = pygame.time.Clock()
running = True

#background
screen.fill(BG_COLOR)
pygame.display.flip()
# FPS (frames per second) controller
fps = pygame.time.Clock()

while exit == False:
    screen.fill(BG_COLOR)

while running:
    #poll for events
    #quit on X
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running =False