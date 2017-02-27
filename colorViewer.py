""" colorViewer.py
    basic GUI for testing colors
    Andy Harris 5/17/06
    """

import pygame
pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Color Viewer - use arrows to pick colors, space bar to switch between hex and decimal")

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((0x00, 0x00, 0x00))

nameFont = pygame.font.SysFont("arial", 12)
numberFont = pygame.font.SysFont("arial", 20)
displayMode = "decimal"

class ColorLabel(pygame.sprite.Sprite):
    def __init__(self, colorName):
        """ initialize label """
        pygame.sprite.Sprite.__init__(self)
        self.value = 0
        self.selected = False
        self.bgColor = (0x99, 0x99, 0x99)

        self.image = pygame.Surface((50, 50))
        self.image.fill(self.bgColor)

        self.colName = numberFont.render(colorName, True, (0x00, 0x00, 0x00))
        self.image.blit(self.colName,(10, 0))
        
        self.rect = self.image.get_rect()
        self.rect.centerx = 200
        self.rect.centery = 350

    def update(self):
        """ refresh display """
        self.image.fill(self.bgColor)
        self.image.blit(self.colName,(10, 0))
        if displayMode == "decimal":
            numText = str(self.value)
        else:
            numText = hex(self.value)

        val = numberFont.render(numText, True, (0x00, 0x00, 0x00))
        self.image.blit(val, (10, 20))

        #move vertically according to value
        self.rect.centery = 350 - self.value


    def increaseColor(self):
        """ add five to value """
        self.value += 5
        if self.value > 255:
            self.value = 255

    def decreaseColor(self):
        """ subtract 5 from value """
        self.value -= 5
        if self.value < 0:
            self.value = 0

    def setSelected(self, selValue):
        """ set Boolean selected value and background color"""
        if selValue == True:
            self.bgColor = (0xff, 0xff, 0xff)
            self.selected == True
        else:
            self.bgColor = (0x99, 0x99, 0x99)
            self.selected == False

def drawBars():
    """ draw vertical bars """
    
    pygame.draw.line(background, (0x99, 0x99, 0x99), (200, 350), (200, 350-255), 3)
    pygame.draw.line(background, (0x66, 0x66, 0x66), (198, 350), (198, 350-255), 2)
    pygame.draw.line(background, (0x33, 0x33, 0x33), (202, 350), (202, 350-255), 2)

    pygame.draw.line(background, (0x99, 0x99, 0x99), (300, 350), (300, 350-255), 3)
    pygame.draw.line(background, (0x66, 0x66, 0x66), (298, 350), (298, 350-255), 2)
    pygame.draw.line(background, (0x33, 0x33, 0x33), (302, 350), (302, 350-255), 2)

    pygame.draw.line(background, (0x99, 0x99, 0x99), (400, 350), (400, 350-255), 3)
    pygame.draw.line(background, (0x66, 0x66, 0x66), (398, 350), (398, 350-255), 2)
    pygame.draw.line(background, (0x33, 0x33, 0x33), (402, 350), (402, 350-255), 2)


# set up color labels
clRed = ColorLabel("red")
clRed.rect.center = (200, 200)
clRed.setSelected(True)

clGreen = ColorLabel("green")
clGreen.rect.center = (300, 200)

clBlue = ColorLabel("blue")
clBlue.rect.center = (400, 200)

clCurrent = clRed

keepGoing = True
allSprites = pygame.sprite.RenderUpdates(clRed, clGreen, clBlue)
clock = pygame.time.Clock()

while keepGoing:
    clock.tick(30)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keepGoing = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if displayMode == "decimal":
                    displayMode = "hex"
                else:
                    displayMode = "decimal"
                    
            elif event.key == pygame.K_RIGHT:            
                if clCurrent == clRed:
                    clCurrent = clGreen
                elif clCurrent == clGreen:
                    clCurrent = clBlue
                else:
                    clCurrent = clRed

                clRed.setSelected(False)
                clGreen.setSelected(False)
                clBlue.setSelected(False)
                clCurrent.setSelected(True)

            elif event.key == pygame.K_LEFT:
                if clCurrent == clRed:
                    clCurrent = clBlue
                elif clCurrent == clGreen:
                    clCurrent = clRed
                else:
                    clCurrent = clGreen
            
                clRed.setSelected(False)
                clGreen.setSelected(False)
                clBlue.setSelected(False)
                clCurrent.setSelected(True)

            elif event.key == pygame.K_ESCAPE:
                keepGoing = False

            
    #up and down taken out of event queue for faster processing
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        clCurrent.increaseColor()
    elif keys[pygame.K_DOWN]:
        clCurrent.decreaseColor()
                
    #change background to the current color
    background.fill((clRed.value, clGreen.value, clBlue.value))

    drawBars()
    
    screen.blit(background, (0, 0))

    allSprites.clear(screen, background)
    allSprites.update()
    allSprites.draw(screen)

    pygame.display.flip()
                           
