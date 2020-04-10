#NOTES 04/09/2020
#Dj Hahn
#space shooting game step by step video 

import pygame
import random
import math

from pygame import mixer

#Initialize the pygame
pygame.init()

#Create a screen (( width , height ))
#x and y axis start in top left corner (0,0)
screen = pygame.display.set_mode((800,600))


#Title and Icon (icons 32 bits)
pygame.display.set_caption("Space Jam")
icon = pygame.image.load('joystick.png')
pygame.display.set_icon(icon)

#Adding a background
background = pygame.image.load('background.png')

#Background Sound
mixer.music.load('background.wav')
mixer.music.play(-1)


#Player
playerImg = pygame.image.load('space_invaders.png')
playerX = 370
playerY = 480
playerX_change = 0

#Alien
alienImg = []
alienX = []
alienY = []
alienX_change = []
alienY_change = []
num_of_aliens = 6

for i in range(num_of_aliens):
    alienImg.append(pygame.image.load('alien.png'))
    alienX.append(random.randint(0,735))
    alienY.append(random.randint(50,150))
    alienX_change.append(4)
    alienY_change.append(40)

#Corona Virus Bullet
#Ready - You can't see the virus bullet on the screen
#Fire - The viruse bullet is currently moving
coronaImg = pygame.image.load('corona.png')
coronaX = 0
coronaY = 480
coronaX_change = 0
coronaY_change = 7
corona_state = "ready"

#Creating the SCORE
score_value = 0
font = pygame.font.Font('freesansbold.ttf',32)

textX = 10
textY = 10

#Game Over Text
over_font = pygame.font.Font('freesansbold.ttf',64) 


def show_score(x,y):
    score = font.render("Score :" + str(score_value),True, (255,255,255))
    screen.blit(score, (x,y))

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255,0,0))
    screen.blit(over_text, (200,250))
    
def player(x,y):
    screen.blit(playerImg, (x, y))

def alien(x,y,i):
    screen.blit(alienImg[i], (x, y))

def fire_corona(x,y):
    global corona_state
    corona_state = "fire"
    screen.blit(coronaImg,(x+16,y+10))

def isCollision(alienX,alienY,coronaX,coronaY):
    distance = math.sqrt((math.pow(alienX-coronaX,2))+ (math.pow(alienY-coronaY,2)))
    if distance < 27:
        return True
    else:
        return False
    
#Game loop (this is where the player and other objects will go)
running = True
while running:

    
    #R,G,B - Red,Green,Blue max 255 and min 0 values         
    screen.fill((0,0,128))

    #Background Image
    screen.blit(background, (0,0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #if keystroke is pressed check whether right or left or space
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                if corona_state is "ready":
                    #Sound for the corona virus blasting from the ship
                    corona_Sound = mixer.Sound('laser.wav')
                    corona_Sound.play()
                    #Get the current X cordinate of the spaceship
                    coronaX = playerX
                    fire_corona(coronaX,coronaY)


        #if keystroke is released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    #5 = 5 + -0.1 -> 5 - 0.1
    #5 = 5 + 0.1

    #Keeping the spachip/player inside the screen we created           
    playerX += playerX_change

    if playerX <=0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    #Alien Movement         
    for i in range(num_of_aliens):

        #Game Over
        if alienY[i] > 440:
            for j in range(num_of_aliens):
                alienY[j] = 2000
            game_over_text()
            break
        
        alienX[i] += alienX_change[i]

        if alienX[i] <=0:
            alienX_change[i] = 4
            alienY[i] += alienY_change[i]
        elif alienX[i] >= 736:
            alienX_change[i] = -4
            alienY[i] += alienY_change[i]

       #Collision
        collision = isCollision(alienX[i],alienY[i],coronaX,coronaY)
        if collision:
           #Sound for the corona virus blasting the aliens
            explosion_Sound = mixer.Sound('explosion.wav')
            explosion_Sound.play() 
            coronaY = 480
            corona_state = "ready"
            score_value += 1
            alienX[i] = random.randint(0,735)
            alienY[i] = random.randint(50,150) 

        alien(alienX[i],alienY[i],i)
        
    #Corona virus/bullet movemtent
    if coronaY <= 0:
        coronaY = 480
        corona_state = "ready"
    if corona_state is "fire":
        fire_corona(coronaX,coronaY)
        coronaY -= coronaY_change

    




        
    player(playerX,playerY)
    show_score(textX,textY)
    pygame.display.update()

    
