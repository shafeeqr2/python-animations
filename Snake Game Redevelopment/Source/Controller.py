
"""
The Controller Module
-The controller.py Module contains the GUI of the game and manages user input
 and output

"""

        
import sys, pygame
from MainMenu import *
from PlayMap import *
from Snake import *
from Food import *
from pygame.locals import KEYDOWN, K_RETURN, K_ESCAPE, K_SPACE,K_1, K_2, K_3, K_UP, K_RIGHT, K_DOWN, K_LEFT, QUIT, K_m, K_a, K_w, K_s, K_d, K_r, K_q
from itertools import count


"""
initialize state variables : size, clock, screen, fonts, mainMenu
"""


# Set up pygame and other environment variables
size=x,y=550,500

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)

# Fonts for the menus
titleFont = pygame.font.Font(None,50)
buttonFont = pygame.font.Font(None,25)
gameFont = pygame.font.Font(None,20)

mainMenu = MainMenu()
gameSpeeds = [5,10,15]
currentSpeed = 5

# RGB values for colours
foreground, background , red, green, yellow, gray= (255, 255, 255), (0, 0, 0), (255,0,0), (0,130,0) , (255,255,0), (50,50,50)

##############################################################################
##############################################################################

def updateGUIDisplay() :
    """
    Function Description: This function is called by the main code to update the GUI on the display.
    input:none
    output:none
    exceptions:none
    """

    global currentSpeed
    selectionDiff = [pygame.Rect(88,388,75,75),pygame.Rect(188,388,75,75),pygame.Rect(288,388,75,75)]
    screen.fill(background)
    # obj is the array of objects to display on the screen
    obj=mainMenu.updateState()

    # Instructions for drawing the main menu objects
    if mainMenu.state=='menu' :
        if currentSpeed==gameSpeeds[0] : pygame.draw.rect(screen,foreground,selectionDiff[0])
        if currentSpeed==gameSpeeds[1] : pygame.draw.rect(screen,foreground,selectionDiff[1])
        if currentSpeed==gameSpeeds[2] : pygame.draw.rect(screen,foreground,selectionDiff[2])
        
        pygame.draw.rect(screen,foreground,obj[0])
        pygame.draw.rect(screen,foreground,obj[1])
        pygame.draw.rect(screen,green,obj[2])
        pygame.draw.rect(screen,yellow,obj[3])
        pygame.draw.rect(screen,red,obj[4])
        
        title = titleFont.render('Nibbles',True,red)        
        surfacePlay = buttonFont.render('Play Game [SPACE]', True, red)
        surfaceQuit = buttonFont.render('Quit Game [q]', True, red)
        surfaceDiff = buttonFont.render('Difficulty ',True,foreground)
        surfaceDiff0 = buttonFont.render('1',True,background)
        surfaceDiff1 = buttonFont.render('2',True,background)
        surfaceDiff2 = buttonFont.render('3',True,background)
        
        screen.blit(title, (200,50))
        screen.blit(surfacePlay, (65, 240))
        screen.blit(surfaceQuit, (335, 240))
        screen.blit(surfaceDiff, (200,350))
        screen.blit(surfaceDiff0, (100,400))
        screen.blit(surfaceDiff1, (200,400))
        screen.blit(surfaceDiff2, (300,400))
        
        pygame.display.flip()

    # Instructions for drawing the instructions objects
    if mainMenu.state=='instructions' :
        
        upM = buttonFont.render(obj[0], True, foreground)
        downM = buttonFont.render(obj[1], True, foreground)
        rightM = buttonFont.render(obj[2],True,foreground)
        leftM = buttonFont.render(obj[3],True,foreground)
        featureM = buttonFont.render(obj[4],True,foreground)
        feature2M = buttonFont.render(obj[5],True,foreground)
        continueM = buttonFont.render(obj[6],True,red)
        
        screen.blit(upM, (150, 100))
        screen.blit(downM, (150, 150))
        screen.blit(rightM, (150,200))
        screen.blit(leftM, (150,250))
        screen.blit(featureM, (150,300))
        screen.blit(feature2M, (150,350))
        screen.blit(continueM,(150,400))
        
        pygame.display.flip()

    # State changing if snake dies        
    if mainMenu.state=='game':
        if obj==-1 : mainMenu.changeState('gameOver')

    # Instructions for drawing the game menu objects
    if mainMenu.state=='game' :
        for i in range(3) :
            if i==0:
                for j in range(len(obj[0])-1):
                    if mainMenu.gameMap.powerUpStatus and j==0 : pygame.draw.rect(screen,red,obj[0][j])
                    else : pygame.draw.rect(screen,foreground,obj[0][j])
            if i==1 : pygame.draw.rect(screen,foreground,obj[1])
            if i==2 : pygame.draw.rect(screen,foreground,obj[2])    

        gameDiff = red
        if currentSpeed==gameSpeeds[0] : gameDiff=green
        if currentSpeed==gameSpeeds[1] : gameDiff=yellow
        if currentSpeed==gameSpeeds[2] : gameDiff=red

        pygame.draw.rect(screen,gameDiff,pygame.Rect(450,2,15,15))
        
        gameScore = gameFont.render('SCORE:  '+str(mainMenu.gameMap.score), True, green)
        pauseNote = gameFont.render('Esc to Pause', True, green)
        screen.blit(gameScore, (200, 0))
        screen.blit(pauseNote, (0,0))

        pygame.display.flip()

    # Instructions for drawing the game over menu objects
    if mainMenu.state=='gameOver' :
        obj = mainMenu.updateState()
        surfaceScore = titleFont.render(str(obj[0]),True,red)
        screen.blit(surfaceScore,(25,100))

        pygame.draw.rect(screen,foreground,obj[1])
        surfaceRetry = buttonFont.render(obj[2], True, background)
        screen.blit(surfaceRetry,(114,240))

        pygame.draw.rect(screen,foreground,obj[3])
        surfaceQuit = buttonFont.render(obj[4], True, background)
        screen.blit(surfaceQuit,(338,240)) 
            
        pygame.display.flip()


    # Instructions for drawing the game pause menu objects
    if mainMenu.state=='gamePause' :
        obj = mainMenu.updateState()
        surfaceScore = titleFont.render(str(obj[0]),True,red)
        screen.blit(surfaceScore,(25,100))

        pygame.draw.rect(screen,foreground,obj[3])
        surfaceMenu = buttonFont.render(obj[4], True, background)
        screen.blit(surfaceMenu,(333,240))
        
        pygame.draw.rect(screen,foreground,obj[1])
        surfaceResume = buttonFont.render(obj[2], True, background)
        screen.blit(surfaceResume,(102,240))

        pygame.draw.rect(screen,foreground,obj[5])
        surfaceExit = buttonFont.render(obj[6], True, background)
        screen.blit(surfaceExit,(240,390)) 
            
        pygame.display.flip()            


##############################################################################
##############################################################################
        
def eventChecker() :
    """
    This method is the controller for our software model. This method
    manages the behaviour changes of the system based on input from hardware.
    """
    
    changedDir = False
    global currentSpeed
    # Loops through the list of events that occured
    for event in pygame.event.get() :
            if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
            
            # Controlling for when the mouse is unclicked
            elif event.type == pygame.MOUSEBUTTONUP :
                pos = pygame.mouse.get_pos()
                 
                if mainMenu.state=='menu' and mainMenu.startGameButton.collidepoint(pos) :
                        mainMenu.changeState('instructions')
                if mainMenu.state=='menu' and mainMenu.exitGameButton.collidepoint(pos) :
                        pygame.event.post(pygame.event.Event(QUIT))
                if mainMenu.state=='menu' and mainMenu.diff0Button.collidepoint(pos) :
                        mainMenu.gameMap.setDiff(0)
                        currentSpeed = gameSpeeds[0]
                if mainMenu.state=='menu' and mainMenu.diff1Button.collidepoint(pos) :
                        mainMenu.gameMap.setDiff(1)
                        currentSpeed = gameSpeeds[1]
                if mainMenu.state=='menu' and mainMenu.diff2Button.collidepoint(pos) :
                        mainMenu.gameMap.setDiff(2)
                        currentSpeed = gameSpeeds[2]
                        
                if mainMenu.state=='gameOver' and mainMenu.gameOver.retryButton.collidepoint(pos) :
                        mainMenu.changeState('game')
                if mainMenu.state=='gameOver' and mainMenu.gameOver.exitButton.collidepoint(pos) :
                        pygame.event.post(pygame.event.Event(QUIT))
                        
                if mainMenu.state=='gamePause' and mainMenu.gamePause.menuButton.collidepoint(pos) :
                        mainMenu.changeState('menu')
                if mainMenu.state=='gamePause' and mainMenu.gamePause.exitButton.collidepoint(pos) :
                        pygame.event.post(pygame.event.Event(QUIT))
                if mainMenu.state=='gamePause' and mainMenu.gamePause.resumeButton.collidepoint(pos) :
                        mainMenu.changeState('game')
                        
            # Event handling when keyboard key is pressed                
            elif event.type == KEYDOWN :
                # Difficulty changing
                if mainMenu.state=='menu' :
                    if event.key == K_1 : currentSpeed = gameSpeeds[0]
                    if event.key == K_2 : currentSpeed = gameSpeeds[1]
                    if event.key == K_3 : currentSpeed = gameSpeeds[2]

                # moving the snake
                if mainMenu.state=='game' and not(changedDir):
                        if event.key == K_UP or event.key == K_w:
                            mainMenu.gameMap.snake.changeDir(1)
                        elif event.key == K_RIGHT or event.key == K_d:
                            mainMenu.gameMap.snake.changeDir(2)
                        elif event.key == K_DOWN or event.key == K_s:
                            mainMenu.gameMap.snake.changeDir(-1)
                        elif event.key == K_LEFT or event.key == K_a:
                            mainMenu.gameMap.snake.changeDir(-2)
                        changedDir = True

                if event.key==K_RETURN and mainMenu.state=='instructions' :
                    mainMenu.changeState('game')
                if event.key==K_ESCAPE and mainMenu.state=='game' :
                        mainMenu.changeState('gamePause')
                if event.key == K_SPACE :
                    if mainMenu.state == 'menu' : mainMenu.changeState('instructions')
                    elif mainMenu.state!='game' : mainMenu.changeState('game')
                
                if event.key == K_m and (mainMenu.state=='gamePause' or mainMenu.state=='gameOver') : mainMenu.changeState('menu')
                if event.key == K_q:
                    pygame.event.post(pygame.event.Event(QUIT))
    return 1

##############################################################################
##############################################################################

def main() :
        while 1:
                # Constant framerate for menus, variable framerate for game (difficulty)
                if mainMenu.state!='game' : clock.tick(30)
                else: clock.tick(min(currentSpeed + (mainMenu.gameMap.score / 4), 30))
                    
                if eventChecker() == 0 :
                        return
                updateGUIDisplay()

main()
