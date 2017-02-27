import os
import time
import pygame
pygame.init()

screen = pygame.display.set_mode((300, 300))
pygame.display.set_caption("AUTOMATIC GRADIENCE RED")

loop = 1
while (loop==1):
    
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
        background.fill((255, 230, 230))

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
            background.fill((255, 204, 204))

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
                background.fill((255, 179, 179))

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
                    background.fill((255, 153, 153))

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
                        background.fill((255, 128, 128))

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
                            background.fill((255, 102, 102))

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
                                background.fill((255, 77, 77))

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
                                    background.fill((255, 51, 51))

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
                                        background.fill((255, 26, 26))

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
                                                background.fill((230, 0, 0))

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
                                                    background.fill((204, 0, 0))

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
                                                        background.fill((179, 0, 0))

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
                                                            background.fill((128, 0, 0))

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
                                                                background.fill((102, 0, 0))

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
                                                                    background.fill((77, 0, 0))

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
                                                                        background.fill((26, 0, 0))

                                                                        #A - Action (broken into ALTER steps)

                                                                            #A - Assign values to key variables
                                                                        clock = pygame.time.Clock()
                                                                        keepGoing= False
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

                                                                            

                                                                            

                                                                            

                                                                            

                                                                            

                                                                            

                                                                            

                                                                            


                                                                            

                                                                            

                                                    
                                            



                                                        
