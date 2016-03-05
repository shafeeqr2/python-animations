import pygame
import random

class Food:
    """
    Food class to encapsulate position of food particle
    state variables:
        position: pygame.Rect object
    """
    def __init__(self):
        """
            constructor for Food.py
            
            Transition: initializes a food object with random position
            input:none
            output:none
        """

        #width of block
        blockWidth = 10

        #length of block
        blockLength = 10

        #scale factor to multiply by the randomly generated number to appear on screen.
        scaleFactor = 10

     
        #offset to skip the header (which contains score)
        offset = 20

        #randomly generate the a x position on the screen to display the food
        xVal = random.randrange(55)

        #randomly generate the an y position on the screen to display the food
        yVal = random.randrange(48)

        #position has x and y values.
        self.position = pygame.Rect(xVal * scaleFactor, yVal * scaleFactor + offset, blockWidth, blockLength)


