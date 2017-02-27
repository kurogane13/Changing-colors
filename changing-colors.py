""" idea.py
    simplest possible pygame display
    demonstrates IDEA / ALTER model
    Andy Harris, 5/06
    """

#I - Import and initialize
import os
import time
import pygame
pygame.init()

#orange= 255, 64, 0 
#green= 0, 255, 0 
#violet= 255, 0, 255
#grey= 128, 128, 128
#pink= 255, 179, 179
#D - Display configuration
loop = 0
while (loop==0):
    
    screen = pygame.display.set_mode((300, 300))
    pygame.display.set_caption("Colored box")
    import os
    os.system('clear')
    print("##############################################################")
    print("COLORED BOXES MODE SELECTION")
    print("##############################################################")
    print("'B' - BLACK BOX")
    print("--------------------------------------------------------------")
    print("'b' - BLUE BOX")
    print("--------------------------------------------------------------")
    print("'G' - GREY BOX")
    print("--------------------------------------------------------------")
    print("'g' - GREEN BOX")
    print("--------------------------------------------------------------")
    print("'o' - ORANGE BOX")
    print("--------------------------------------------------------------")
    print("'p' - PINK BOX")
    print("--------------------------------------------------------------")
    print("'r' - RED BOX")
    print("--------------------------------------------------------------")
    print("'v' - VIOLET BOX")
    print("--------------------------------------------------------------")
    print("'w' - WHITE BOX")
    print("--------------------------------------------------------------")
    print("'y' - YELLOW BOX")
    print("==============================================================")
    print("'i' - FOR AUTOMATIC COLOR CHANGES - ")
    print("==============================================================")
    print("'e' - EXTERNAL WINDOW WITH AUTOMATIC COLOR CHANGES - ")
    print("==============================================================")
    print("'i1' - FOR AUTOMATIC GRADIENCE CHANGES - ")
    print("==============================================================")
    print("'e1' - EXTERNAL WINDOW WITH GRADIENCE CHANGES - ")
    print("==============================================================")
    print("'m' - FOR MOVING BOX - ")
    print("==============================================================")
    coloredboxselection=raw_input("WAITING FOR SELECTION: ")
    black=("B")
    bluebox=("b")
    yellowbox=("y")
    redbox=("r")
    orange=("o")
    pink=("p")
    green=("g")
    white=("w")
    violet=("v")
    grey=("G")
    automatic=("i")
    externalwindowautomatic=("e")
    automaticgradience=("i1")
    externalwindowgradience=("e1")
    movingbox=("m")
        
    
    if coloredboxselection==bluebox:

        
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

            print("=============================================================")
            print("BLUE")
            print("=============================================================")

            break

            loop = 0


    elif coloredboxselection==yellowbox:
        
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
            break

            loop = 0

    elif coloredboxselection==redbox:
        
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
            break

            loop = 0

    elif coloredboxselection==orange:
        
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
            break

            loop = 0

    elif coloredboxselection==movingbox:
        
        os.system('gnome-terminal -e "python /home/gus/Python-pygames/movingbox.py"')
        loop = 0

    elif coloredboxselection==externalwindowautomatic:
        
        os.system('gnome-terminal -e "python /home/gus/Python-pygames/automatic-colors.py"')
        loop = 0

    elif coloredboxselection==automaticgradience:

        import os
        import time
        import pygame
        pygame.init()
        screen = pygame.display.set_mode((300, 300))
        pygame.display.set_caption("AUTOMATIC GRADIENCE DEMO")
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
                                                                            loop = 0
                                                                            

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


    elif coloredboxselection==externalwindowgradience:
        os.system('gnome-terminal -e "python /home/gus/Python-pygames/automatic-gradient.py"')
        loop = 0

    elif coloredboxselection==green:
        
        #E - Entities (just background for now)
        background = pygame.Surface(screen.get_size())
        background = background.convert()
        background.fill((0, 255, 0))

        #A - Action (broken into ALTER steps)

        #A - Assign values to key variables
        clock = pygame.time.Clock()
        keepGoing = True

        #T - Timer to set frame rate
        clock.tick(30)

        #E - Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = True
                break
                loop = 0

        #R - Refresh display
        screen.blit(background, (0, 0))
        pygame.display.flip()
            

            

    elif coloredboxselection==white:
        
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
            break

            loop = 0

    elif coloredboxselection==black:
        
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
            break

            loop = 0

    elif coloredboxselection==violet:
        
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
            break

            loop = 0

    elif coloredboxselection==grey:
        
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
            break

            loop = 0

    elif coloredboxselection==pink:
        
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
            break
            loop = 0

    elif coloredboxselection==automatic:
        
        loop = 1
        while (loop==1):
            
            screen = pygame.display.set_mode((300, 300))
            pygame.display.set_caption("AUTOMATIC COLOR CHANGING DEMO")
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
                                                        loop = 0
                                                        

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
                                            
                                            

                        
            


    else:
        import os
        os.system('clear')
        print("PLEASE ONLY INPUT OPTIONS IN THE MENU...")
        import time
        time.sleep(2)
        os.system('clear')
        

