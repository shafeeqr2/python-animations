import pygame

class GameOver:
    """
        GameOver class to emulate the game state 'game over'
        state variables:
            score:integer
            retryButton: pygame.Rect object
            exitButton: pygame.Rect object
    """
    def __init__(self,score) :
        """
            constructor for GameOver.py
            
            Transition: initializes a game over screen
            input:none
            output:none
        """
        self.retryMessage = 'Retry [SPACE]'
        self.exitMessage = 'Quit [q]'
        self.score = 'Game Over!       SCORE: '+str(score)
        self.retryButton = pygame.Rect(100,200,150,100)
        self.exitButton = pygame.Rect(300,200,150,100)
        
    def updateState(self,score) :
        """
            function to update the score at the time of game over
            
            Transition: changes the current score at game over time
            input:integer value for score
            output:none
        """
        self.score='Game Over!       SCORE: ' + str(score)
        
    def getCurrentState(self) :
        """
            function to return the current game state
            
            Transition: returns the objects to display on the main screen
            input:none
            output:an array of objects
        """
        return [self.score,self.retryButton,self.retryMessage,self.exitButton,self.exitMessage]
