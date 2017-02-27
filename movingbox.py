#Entities
#yellow background
import os
import time
import pygame
pygame.init()

screen = pygame.display.set_mode((300, 300))
pygame.display.set_caption("Moving Box")

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((0, 0, 0))


#make a red 25 x 25 box
box = pygame.Surface((25, 25))
box = box.convert()
box.fill((255, 0, 0))

# set up some box variables
box_a = 0
box_y = 200

#ACTION

    #Assign 
clock = pygame.time.Clock()
keepGoing = True

    #Loop
while keepGoing:

    #Time
    clock.tick(30)

    #Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keepGoing = False

    #modify box value
    box_a +=6         
    #check boundaries
    if box_a > screen.get_width():
        box_a = 0


    #Refresh screen
    screen.blit(background, (100, 0))
    screen.blit(box, (box_a, box_y))
    pygame.display.flip()
