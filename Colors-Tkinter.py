# -*- coding: utf-8 -*-
from Tkinter import *
import tkMessageBox
import Tkinter
import pygame
pygame.init()
screen = pygame.display.set_mode((300, 300))
pygame.display.set_caption("Colored box")

print("PRESS A BUTTON FROM THE CONSOLE WINDOW, WAITING FOR INSTRUCTIONS...")


root = Tk()
root.title('MAIN COLOR CHANGES BUTTON CONSOLE')


def black():
    import os
    os.system('clear')
    screen = pygame.display.set_mode((300, 300))
    pygame.display.set_caption("BLACK BOX")
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

        print("=============================================================")
        print("BLACK")
        print("=============================================================")

        break
    
buttonblack = Button(root, text="BLACK BOX", fg="white", bg="black", width=55, command=black)
buttonblack.grid(row=0, column=0)

def blue():
    import os
    os.system('clear')
    screen = pygame.display.set_mode((300, 300))
    pygame.display.set_caption("BLUE BOX")
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
    
buttonblue = Button(root, text="BLUE BOX", fg="blue", bg="blue", width=55, command=blue)
buttonblue.grid(row=1, column=0)


def grey():
    import os
    os.system('clear')
    screen = pygame.display.set_mode((300, 300))
    pygame.display.set_caption("GREY BOX")
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

        print("=============================================================")
        print("GREY")
        print("=============================================================")

        break
    
buttongrey = Button(root, text="GREY BOX", fg="grey", bg="grey", width=55, command=grey)
buttongrey.grid(row=3, column=0)

def green():
    import os
    os.system('clear')
    screen = pygame.display.set_mode((300, 300))
    pygame.display.set_caption("GREEN BOX")
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

        print("=============================================================")
        print("GREEN")
        print("=============================================================")

        break
    
buttongreen = Button(root, text="GREEN BOX", fg="green", bg="green", width=55, command=green)
buttongreen.grid(row=4, column=0)

def orange():
    import os
    os.system('clear')
    screen = pygame.display.set_mode((300, 300))
    pygame.display.set_caption("ORANGE BOX")
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

        print("=============================================================")
        print("ORANGE")
        print("=============================================================")

        break
    
buttonorange = Button(root, text="ORANGE BOX", fg="orange", bg="orange", width=55, command=orange)
buttonorange.grid(row=5, column=0)

def pink():
    import os
    os.system('clear')
    screen = pygame.display.set_mode((300, 300))
    pygame.display.set_caption("PINK BOX")
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

        print("=============================================================")
        print("PINK")
        print("=============================================================")

        break
    
buttonpink = Button(root, text="PINK BOX", fg="pink", bg="pink", width=55, command=pink)
buttonpink.grid(row=6, column=0)

def red():
    import os
    os.system('clear')
    screen = pygame.display.set_mode((300, 300))
    pygame.display.set_caption("RED BOX")
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

        print("=============================================================")
        print("RED")
        print("=============================================================")

        break
    
buttonred = Button(root, text="RED BOX", fg="red", bg="red", width=55, command=red)
buttonred.grid(row=7, column=0)

def violet():
    import os
    os.system('clear')
    screen = pygame.display.set_mode((300, 300))
    pygame.display.set_caption("VIOLET BOX")
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

        print("=============================================================")
        print(" VIOLET")
        print("=============================================================")

        break
    
buttonviolet = Button(root, text="VIOLET BOX", fg="violet", bg="violet", width=55, command=violet)
buttonviolet.grid(row=8, column=0)

def white():
    import os
    os.system('clear')
    screen = pygame.display.set_mode((300, 300))
    pygame.display.set_caption("WHITE BOX")
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

        print("=============================================================")
        print(" WHITE")
        print("=============================================================")

        break
    
buttonwhite = Button(root, text="WHITE BOX", fg="white", bg="white", width=55, command=white)
buttonwhite.grid(row=9, column=0)

def yellow():
    import os
    os.system('clear')
    screen = pygame.display.set_mode((300, 300))
    pygame.display.set_caption("YELLOW BOX")
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

        print("=============================================================")
        print(" YELLOW")
        print("=============================================================")

        break
    
buttonyellow = Button(root, text="YELLOW BOX", fg="yellow", bg="yellow", width=55, command=yellow)
buttonyellow.grid(row=10, column=0)


def commandlinecolors():
    import os
    os.system('clear')
    os.system('gnome-terminal -e "python /home/gus/Python-pygames/changing-colors.py"')
    
    
buttoncommandlinecolors = Button(root, text="LAUNCH COMMAND LINE COLOR INTERFACE", fg="black", bg="white", width=55, command=commandlinecolors)
buttoncommandlinecolors.grid(row=0, column=1)

def automaticexternal():
    import os
    os.system('clear')
    os.system('gnome-terminal -e "python /home/gus/Python-pygames/automatic-colors.py"')
    
    
buttonautomaticexternal = Button(root, text="AUTOMATIC MULTICOLOR CHANGES", fg="white", bg="orange", width=55, command=automaticexternal)
buttonautomaticexternal.grid(row=1, column=1)

def automaticgradient():
    import os
    os.system('clear')
    os.system('gnome-terminal -e "python /home/gus/Python-pygames/automatic-gradient.py"')
    
    
buttonautomaticgradient = Button(root, text="AUTOMATIC GRADIENCE RED", fg="black", bg="red", width=55, command=automaticgradient)
buttonautomaticgradient.grid(row=2, column=1)


def automaticgradient2():
    import os
    os.system('clear')
    os.system('gnome-terminal -e "python /home/gus/Python-pygames/automatic-gradient-2.py"')
    
    
buttonautomaticgradient2 = Button(root, text="AUTOMATIC GRADIENCE MULTICOLOR", fg="black", bg="green", width=55, command=automaticgradient2)
buttonautomaticgradient2.grid(row=3, column=1)

def automaticgradient3():
    import os
    os.system('clear')
    os.system('gnome-terminal -e "python /home/gus/Python-pygames/automatic-gradient-3.py"')
    
    
buttonautomaticgradient3 = Button(root, text="AUTOMATIC GRADIENCE MULTICOLOR 2", fg="black", bg="blue", width=55, command=automaticgradient3)
buttonautomaticgradient3.grid(row=4, column=1)

root.mainloop()





