import pygame
import time
import random
import sys

# startuo shit
pygame.init()
garf = pygame.image.load('assets/garf.jpeg')
logo = pygame.transform.scale(garf, (100, 50))

speed = [2,2]

# window size
window_width = 1280
window_height = 720

#colors
BG_COLOR = (201, 8, 182)

#garf setup
garf = pygame.image.load("assets/garf.jpeg")
garf = pygame.transform.scale(garf, (100,50))
garf_rect = garf.get_rect(center=(window_width//2, window_height//2))

#lasagna setup
lasagna_img = pygame.image.load("assets/lasagna.jpeg")
lasagna_img = pygame.transform.scale(lasagna_img,(40, 30))

def random_lasagna():
    x = random.randint(0, window_width-40)
    y = random.randint(0, window_height-30)
    return lasagna_img.get_rect(topleft=(x, y))

lasagnas = [random_lasagna() for _ in range(5)]

#screen setup 
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('garfbounce')
clock = pygame.time.Clock()
running = True

while running:
     # 100 fps
    clock.tick(100)

    #events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #move garf
    garf_rect = garf_rect.move(speed)

    #bounce
    if garf_rect.left < 0 or garf_rect.right > window_width:
        speed[0] = -speed[0]
        speed[1] += random.choice([-1, 1])
    if garf_rect.top < 0 or garf_rect.bottom > window_height:
        speed[1] = -speed[1]
        
        speed[1] += random.choice([-1, 1])
    #collisions
    for lasagna in lasagnas[:]:
        if garf_rect.colliderect(lasagna):
            lasagnas.remove(lasagna)
            #get bigger
            w = int(garf_rect.width * 1.2)
            h = int(garf_rect.height * 1.2)
            garf = pygame.transform.scale(garf, (w, h))
            garf_rect = garf.get_rect(center=garf_rect.center)
            #get faster
            speed = [s + (1 if s > 0 else -1) for s in speed]
            #spawn new one
            lasagnas.append(random_lasagna())
 # actually finally draw thingssss
    screen.fill(BG_COLOR)
    screen.blit(garf, garf_rect)
    for lasagna in lasagnas:
        screen.blit(lasagna_img, lasagna)

    pygame.display.flip()

pygame.quit()
sys.exit()




    