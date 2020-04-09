#pygame learning

import random
import pygame, sys
from pygame.locals import *
#Color     RGB Values
AQUA=       (   0, 255, 255)
BLACK=      (   0,   0,   0)
BLUE=       (   0,   0, 255)
FUCHSIA=    ( 255,   0, 255)
GRAY=       ( 128, 128, 128)
GREEN=      (   0, 128,   0)
LIME=       (   0, 255,   0)
MAROON=     ( 128,   0,   0)
NAVY=       (   0,   0, 128)
OLIVE=      ( 128, 128,   0)
PURPLE=     ( 128,   0, 128)
RED=        ( 255,   0,   0)
SILVER=     ( 192, 192, 192)
TEAL=       (   0, 128, 128)
WHITE=      ( 255, 255, 255)
YELLOW=     ( 255, 255,   0)


class runner:         #(X,Y) are starting point for stick figure from center of head
    def __init__(self,x, y):
        
        pygame.draw.circle(DISPLAYSURF, RED, (x,y), 10)
        pygame.draw.line(DISPLAYSURF, RED, (x,y),(x,y+40), 2)
        pygame.draw.line(DISPLAYSURF, RED, (x,y+40),(x-10, y+70), 2)
        pygame.draw.line(DISPLAYSURF, RED, (x,y+40), (x+10, y+70),2)
        pygame.draw.line(DISPLAYSURF, RED, (x,y+30), (x+15, y+10), 2)
        pygame.draw.line(DISPLAYSURF, RED, (x,y+30), (x-15, y+10), 2)
        pygame.display.update()
    def move(self, x, y):
        pygame.draw.circle(DISPLAYSURF, RED, (x,y), 10)
        pygame.draw.line(DISPLAYSURF, RED, (x,y),(x,y+40), 2)
        pygame.draw.line(DISPLAYSURF, RED, (x,y+40),(x-10, y+70), 2)
        pygame.draw.line(DISPLAYSURF, RED, (x,y+40), (x+10, y+70),2)
        pygame.draw.line(DISPLAYSURF, RED, (x,y+30), (x+15, y+10), 2)
        pygame.draw.line(DISPLAYSURF, RED, (x,y+30), (x-15, y+10), 2)
        pygame.display.update()
        
def gamepath():
    #BAORD RAND NUMBERS FOR LEVEL LENGTH
    r=random.randint(10, 300) #MID
    s=random.randint(100,400)#TOP
    w=random.randint(700, 900) #MID
    z=random.randint(500,700) #TOP
    #DRAW LOWEST LEVEL
    x=0
    y=600
    while x<1300:
        pygame.draw.rect(DISPLAYSURF, LIME, pygame.Rect(x,600, 30,30))
        x=x+32
        pygame.display.update()
    y=400 
    #DRAW MID LEVEL
    while r<w:
        pygame.draw.rect(DISPLAYSURF, AQUA, pygame.Rect(r, y, 30, 30))
        r=r+32
        pygame.display.update()
    y=200
    
    #DRAW TOP LEVEL
    while s<z:
        pygame.draw.rect(DISPLAYSURF, BLUE, pygame.Rect(s, y, 30, 30))
        s=s+32
        pygame.display.update()
    #DRAW KONG LEVEL
    y=100
    x=random.randint(1, 500)
    i=0
    for i in range (0, 4):
        pygame.draw.rect(DISPLAYSURF, BLUE, pygame.Rect(x, y, 30, 30))
        pygame.display.update()
        i=i+1
        x=x+32
    #LADDER HIGH
    j=random.randint(400,500)
    y=400
    pygame.draw.line(DISPLAYSURF, SILVER, (j, y), (j, y-200),3)
    pygame.draw.line(DISPLAYSURF, SILVER, (j+32, y), (j+32, y-200), 3)
    while y>199:    
        pygame.draw.line(DISPLAYSURF, SILVER, (j, y), (j+32, y), 3)
        y=y-20
        pygame.display.update()
    #LADDER LOW
    j=random.randint(300,700)
    y=600
    pygame.draw.line(DISPLAYSURF, SILVER, (j, y), (j, y-200),3)
    pygame.draw.line(DISPLAYSURF, SILVER, (j+32, y), (j+32, y-200), 3)
    while y>399:    
        pygame.draw.line(DISPLAYSURF, SILVER, (j, y), (j+32, y), 3)
        y=y-20
        pygame.display.update()
    

pygame.init()
DISPLAYSURF = pygame.display.set_mode((1300, 700))
pygame.display.set_caption('PYTHON PALS')

FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()

runnerx=20
runnery=530
direction= 'right'
runner=runner(runnerx, runnery)
while True: #main game loop
    gamepath()
    baseSurf=DISPLAYSURF.copy() #create board copy to use for animation
    #runner=runner(runnerx, runnery)
    #DISPLAYSURF.blit(DISPLAYSURF, runner)
    if direction == 'right':
        runnerx= runnerx+5
        runner.move(runnerx, runnery)
        pygame.display.update()
    elif direction == 'left':
        runnerx= runnerx-5
        runner.move(runnerx, runnery)
        pygame.display.udate()
    elif direction == 'up':
        runnery= runnery+10
        runner.move(runnerx,runnery)
        pygame.display.update()
    #DISPLAYSURF.blit(runner, (runnerx, runnery))
    for event in pygame.event.get():
        #DISPLAYSURF.fill(BLACK)
        
        pygame.display.update()
        running= True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                #elif event.type=KEYUP:
                 #   if event.Key in (K_Left,K_a) and isValidMove(mainBoard, LEFT):
                  #      slideTo=LEFT
                  #    elif event.key in (K_RIGHT, K_d) and isValidMove(mainBoard, RIGHT):
                   #     slideTo=RIGHT
                    #elif event.key in (K_UP, K_w) and isValidMove(mainBoard, UP):
                    #    slideTo= UP
                    #elif event.key in((K_DOWN, K_s) and isValidMove(mainBoard, DOWN):
                     #   slideTo=DOWN
        sys.exit()
    pygame.display.update()
