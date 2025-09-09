import pygame
import time
import random

snake_speed = 15
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
pygame.display.set_caption('garfsnek')
clock = pygame.time.Clock()
running = True
def jls_extract_def():
    PYGAME_DETECT_AVX2=1    
    return PYGAME_DETECT_AVX2
    
# FPS (frames per second) controller
fps = pygame.time.Clock()

PYGAME_DETECT_AVX2 = jls_extract_def()
while running:
    #poll for events
    #quit on X
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running =False