import os
import time
import pygame
pygame.init()

screen = pygame.display.set_mode((300, 300))
pygame.display.set_caption("AUTOMATIC COLOR CHANGES")

loop = 1
while (loop==1):
    
    #E - Entities (just background for now)
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 255))

    #A - Action (broken into ALTER steps)

        #A - Assign values to key variables
    clock = pygame.time.Clock()
    keepGoing = True

        #L - Set up main loop
    while keepGoing:

        #T - Timer to set frame rate
        clock.tick(30)

        #E - Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False

        #R - Refresh display
        screen.blit(background, (0, 0))
        pygame.display.flip()
        

        #E - Entities (just background for now)
        background = pygame.Surface(screen.get_size())
        background = background.convert()
        background.fill((255, 255, 0))

        #A - Action (broken into ALTER steps)

            #A - Assign values to key variables
        clock = pygame.time.Clock()
        keepGoing = True

            #L - Set up main loop
        while keepGoing:

            #T - Timer to set frame rate
            clock.tick(30)

            #E - Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    keepGoing = False

            #R - Refresh display
            screen.blit(background, (0, 0))
            pygame.display.flip()
            
            
            #E - Entities (just background for now)
            background = pygame.Surface(screen.get_size())
            background = background.convert()
            background.fill((255, 0, 0))

            #A - Action (broken into ALTER steps)

                #A - Assign values to key variables
            clock = pygame.time.Clock()
            keepGoing = True

                #L - Set up main loop
            while keepGoing:

                #T - Timer to set frame rate
                clock.tick(30)

                #E - Event handling
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        keepGoing = False

                #R - Refresh display
                screen.blit(background, (0, 0))
                pygame.display.flip()
                

                #E - Entities (just background for now)
                background = pygame.Surface(screen.get_size())
                background = background.convert()
                background.fill((255, 64, 0))

                #A - Action (broken into ALTER steps)

                    #A - Assign values to key variables
                clock = pygame.time.Clock()
                keepGoing = True

                    #L - Set up main loop
                while keepGoing:

                    #T - Timer to set frame rate
                    clock.tick(30)

                    #E - Event handling
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            keepGoing = False

                    #R - Refresh display
                    screen.blit(background, (0, 0))
                    pygame.display.flip()
                    

                    #E - Entities (just background for now)
                    background = pygame.Surface(screen.get_size())
                    background = background.convert()
                    background.fill((0, 255, 0))

                    #A - Action (broken into ALTER steps)

                        #A - Assign values to key variables
                    clock = pygame.time.Clock()
                    keepGoing = True

                        #L - Set up main loop
                    while keepGoing:

                        #T - Timer to set frame rate
                        clock.tick(30)

                        #E - Event handling
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                keepGoing = False

                        #R - Refresh display
                        screen.blit(background, (0, 0))
                        pygame.display.flip()
                        

                        #E - Entities (just background for now)
                        background = pygame.Surface(screen.get_size())
                        background = background.convert()
                        background.fill((255, 0, 255))

                        #A - Action (broken into ALTER steps)

                            #A - Assign values to key variables
                        clock = pygame.time.Clock()
                        keepGoing = True

                            #L - Set up main loop
                        while keepGoing:

                            #T - Timer to set frame rate
                            clock.tick(30)

                            #E - Event handling
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    keepGoing = False

                            #R - Refresh display
                            screen.blit(background, (0, 0))
                            pygame.display.flip()
                            

                            #E - Entities (just background for now)
                            background = pygame.Surface(screen.get_size())
                            background = background.convert()
                            background.fill((128, 128, 128))

                            #A - Action (broken into ALTER steps)

                                #A - Assign values to key variables
                            clock = pygame.time.Clock()
                            keepGoing = True

                                #L - Set up main loop
                            while keepGoing:

                                #T - Timer to set frame rate
                                clock.tick(30)

                                #E - Event handling
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        keepGoing = False

                                #R - Refresh display
                                screen.blit(background, (0, 0))
                                pygame.display.flip()
                                

                                #E - Entities (just background for now)
                                background = pygame.Surface(screen.get_size())
                                background = background.convert()
                                background.fill((255, 255, 179))

                                #A - Action (broken into ALTER steps)

                                    #A - Assign values to key variables
                                clock = pygame.time.Clock()
                                keepGoing = True
                                

                                    #L - Set up main loop
                                while keepGoing:

                                    #T - Timer to set frame rate
                                    clock.tick(30)

                                    #E - Event handling
                                    for event in pygame.event.get():
                                        if event.type == pygame.QUIT:
                                            keepGoing = False
                                            

                                    #R - Refresh display
                                    screen.blit(background, (0, 0))
                                    pygame.display.flip()
                                    

                                    #E - Entities (just background for now)
                                    background = pygame.Surface(screen.get_size())
                                    background = background.convert()
                                    background.fill((0, 255, 255))

                                    #A - Action (broken into ALTER steps)

                                        #A - Assign values to key variables
                                    clock = pygame.time.Clock()
                                    keepGoing = True
                                    

                                        #L - Set up main loop
                                    while keepGoing:

                                        #T - Timer to set frame rate
                                        clock.tick(30)

                                        #E - Event handling
                                        for event in pygame.event.get():
                                            if event.type == pygame.QUIT:
                                                keepGoing = False
                                                

                                        #R - Refresh display
                                        screen.blit(background, (0, 0))
                                        pygame.display.flip()
                                        

                                        #E - Entities (just background for now)
                                        background = pygame.Surface(screen.get_size())
                                        background = background.convert()
                                        background.fill((255, 255, 255))

                                        #A - Action (broken into ALTER steps)

                                            #A - Assign values to key variables
                                        clock = pygame.time.Clock()
                                        keepGoing = True
                                        
                                        

                                            #L - Set up main loop
                                        while keepGoing:

                                            #T - Timer to set frame rate
                                            clock.tick(30)

                                            #E - Event handling
                                            for event in pygame.event.get():
                                                if event.type == pygame.QUIT:
                                                    keepGoing = False
                                                    

                                            #R - Refresh display
                                            screen.blit(background, (0, 0))
                                            pygame.display.flip()
                                            

                                            #E - Entities (just background for now)
                                            background = pygame.Surface(screen.get_size())
                                            background = background.convert()
                                            background.fill((0, 0, 0))

                                            #A - Action (broken into ALTER steps)

                                                #A - Assign values to key variables
                                            clock = pygame.time.Clock()
                                            keepGoing = True
                                            
                                            

                                                #L - Set up main loop
                                            while keepGoing:

                                                #T - Timer to set frame rate
                                                clock.tick(30)

                                                #E - Event handling
                                                for event in pygame.event.get():
                                                    if event.type == pygame.QUIT:
                                                        keepGoing = False
                                                        

                                                #R - Refresh display
                                                screen.blit(background, (0, 0))
                                                pygame.display.flip()
                                                

                                                #E - Entities (just background for now)
                                                background = pygame.Surface(screen.get_size())
                                                background = background.convert()
                                                background.fill((0, 0, 0))

                                                #A - Action (broken into ALTER steps)

                                                    #A - Assign values to key variables
                                                clock = pygame.time.Clock()
                                                keepGoing = False
                                                loop = 1
                                                

                                                    #L - Set up main loop
                                                while keepGoing:

                                                    #T - Timer to set frame rate
                                                    clock.tick(30)

                                                    #E - Event handling
                                                    for event in pygame.event.get():
                                                        if event.type == pygame.QUIT:
                                                            keepGoing = False
                                                            

                                                    #R - Refresh display
                                                    screen.blit(background, (0, 0))
                                                    pygame.display.flip()
                                                    
