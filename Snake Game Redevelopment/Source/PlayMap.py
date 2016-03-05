from Snake import *
import pygame
from Food import *
from PowerUp import *

"""
PlayMap object to represent the 'game board' for logic
"""

class PlayMap:
        """
        PlayMap has state variables:
                height:integer
                width: integer
                snake: Snake object
                food: Food object
                powerUp: powerUp object
                powerUpStatus: boolean
                gameStatsBar: pygame.Rect object
                powerUpIndicator: pygame.Rect object
                score: integer
        assumptions: __init__ is executed first
        """
                

        def __init__(self):
                """
                Constructor method for PlayMap
                Transition: initialized into new game state
                input:none
                output:none
                """
                
                self.height = 500
                self.width = 550
                self.snake = Snake() # starting coord of snake
                self.food = Food()
                self.powerUp = PowerUp()

                self.powerUpStatus = True
                self.gameStatsBar = pygame.Rect(0,0,550,20)
                self.powerUpIndicator = pygame.Rect(10,0,10,10)
                self.score = len(self.snake.points)
                self.diff = 0


        def setDiff(self,difficulty) :
                """
                function to set the base difficulty of the game (speed of snake)
                
                transition: updates the difficulty of the game
                input: integer to represent difficulty
                output: none
                """
                self.diff=difficulty
        
        def updateState(self):
                """
                function to update the current state of the game board
                aka what is the state one time unit in the future

                Transition: moves snake, grows, or dies based on situation
                input:none
                output:none
                """

                self.snake.move()
                # deal with food
                
                head = self.snake.points[0]
                if head == self.food.position:
                        self.snake.grow()
                        self.food = Food()
                        self.score += 1


        def isSnakeDead(self):
                """
                function to check if snake is dead

                Transition: checks whether snake violates any rules of life
                input:none
                output:Boolean value
                """
                status = self.didSnakeHitBorder() or self.didSnakeHitSelf()
                return status

        def getCurrentState(self):
                """
                function to return the current state of the game board to MainMenu.py

                Transition: returns current state of the board
                input:none
                output:an array of objects
                """
                if self.isSnakeDead():
                        return -1
                if self.powerUpStatus:
                        return [self.snake.points, self.food.position, self.gameStatsBar, self.powerUpIndicator, self.powerUp.position]
                if self.powerUpStatus==False:
                        return [self.snake.points, self.food.position, self.gameStatsBar, -1, -1]


        def didSnakeHitBorder(self):
                """
                function to check whether snake hit edge of the window

                Transition: checks against position of the borders to determine if snake is hitting the border
                input:none
                output:Boolean value
                """
                head = self.snake.points[0]
                if head.left < 0: return True
                if head.left >= self.width: return True
                if head.top-20 < 0: return True
                if head.top >= self.height: return True
                return False


        def didSnakeHitSelf(self):
                """
                function to check whether snake hit itself

                Transition: checks against position of itself to determine if snake is hitting itself
                input:none
                output:Boolean value
                """
                temp = len(self.snake.points)
                i = 1
                while i < temp :
                    if self.snake.points[0]==self.snake.points[i] :
                        if self.powerUpStatus :
                                self.powerUpStatus=False
                                self.snake.remove(i)
                        else : return True
                    i+=1
                    temp = len(self.snake.points)

                return False
