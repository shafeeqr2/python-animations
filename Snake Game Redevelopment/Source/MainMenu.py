from PlayMap import *
import pygame
from GameOver import *
from GamePause import *
from GameInstructions import *

"""
Main Menu Class encapsulates the 'window' of the game
as the logic(backend) and decides what to send to Controller.py to display
"""

class MainMenu :
    """
    MainMenu has state variables:
    gameMap: PlayMap object
    gameOver: GameOver object
    state: string
    startGameButton: pygame.Rect object
    exitGameButton: pygame.Rect object

    Assumptions: __init__() is called before any other access program
    
    """

    def __init__(self) :
        """
        Constructor for MainMenu class
        Transition: initialized to main menu state
        exception: none
        """
        self.STATES = ['menu','game','gameOver','gamePause','instructions']
        self.gameMap = PlayMap()
        self.gameOver = GameOver(20)
        self.gamePause = GamePause(20)
        self.gameInstructions = GameInstructions()
        self.pauseStatus = False
        
        # What stage of the interface the game is on
        self.state = 'menu'
        
        # Display objects for the GUI
        self.startGameButton = pygame.Rect(50,200,200,100)
        self.exitGameButton = pygame.Rect(300,200,200,100)
        self.diff0Button = pygame.Rect(100,400,50,50)
        self.diff1Button = pygame.Rect(200,400,50,50)
        self.diff2Button = pygame.Rect(300,400,50,50)
        
        self.updateState()


    # Changed representation by python of object for ease of testing
    def __repr__(self) :
        return (str(self.startGameButton)+str(self.exitGameButton)+str(self.diff0Button)+ str(self.diff1Button) + str(self.diff2Button) + str(self.state))

    #Add ValueError exception
    #change value of self.state
    def changeState(self,newState) :
        """
        function to change the current state of the main menu
        Transition: self.state is updated to new state
        exception: none
        input: newState - string value of new state
        output: none
        """

        if self.STATES.count(newState)==1 : self.state = newState
        if self.state =='menu' : self.pauseStatus = False
        if self.state == 'instructions' : self.pauseStatus = False
        if self.state=='game' :
            if not(self.pauseStatus) :
                self.gameMap = PlayMap()
        if self.state=='gameOver':
            self.pauseStatus = False
            self.gameOver = GameOver(self.gameMap.score)
        if self.state=='gamePause':
            self.pauseStatus = True
            self.gamePause = GamePause(self.gameMap.score)
        
    #call necessary functions based on current state
    def updateState(self) :
        """
        function to return which objects to display on GUI (current state of game)
        Transition: an array of objects to display on the screen is returned
        exception: none
        input: none
        output: an array of objects (pygame)
        """
        #print "MainMenu.updateState ran"
        if self.state=='menu' :
            return [self.startGameButton,self.exitGameButton,self.diff0Button,self.diff1Button,self.diff2Button]
        if self.state=='instructions' :
            return self.gameInstructions.getCurrentState()
        if self.state=='game' :
            self.gameMap.updateState()
            return self.gameMap.getCurrentState()     
        if self.state=='gameOver' :
            self.gameOver.updateState(self.gameMap.score)
            return self.gameOver.getCurrentState()
        if self.state=='gamePause' :
            self.gamePause.updateState(self.gameMap.score)
            return self.gamePause.getCurrentState()
