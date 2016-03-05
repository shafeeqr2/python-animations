import pygame

class GameInstructions:
    """
        GameOver class to emulate the game state 'game paused'
        state variables:
            score:integer
            menuButton: pygame.Rect object
            retryButton: pygame.Rect object
            exitButton: pygame.Rect object
    """
    def __init__(self) :
        """
            constructor for GamePause.py
            
            Transition: initializes a pause screen
            input:none
            output:none
        """
        self.upMessage = '[W] OR [UP] to move up'
        self.downMessage = '[S] OR [DOWN] to move down'
        self.rightMessage = '[A] OR [RIGHT] to move right'
        self.leftMessage = '[D] OR [RIGHT] to move left'
        self.featureMessage = 'The red tip of the snake means you'
        self.featureMessage2 = 'can eat yourself once without losing.'
        
        self.continueMessage = 'Press Enter to Continue'
        
        
        
    def updateState(self) :
        """
            function to update the score at the time of game pause
            
            Transition: changes the current score at game pause time
            input:integer value for score
            output:none
        """
        x = 1
        
    def getCurrentState(self) :
        """
            function to return the current game state
            
            Transition: returns the objects to display on the main screen
            input:none
            output:an array of objects
        """
        return [self.upMessage,self.downMessage,self.rightMessage,self.leftMessage,self.featureMessage,self.featureMessage2,self.continueMessage]
