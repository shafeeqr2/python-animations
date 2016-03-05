import pygame
import random

class PowerUp:
    """
    PowerUp class to encapsulate position of powerup particle
    state variables:
        position: pygame.Rect object
    """
    def __init__(self):
        """
            constructor for PowerUp.py
            
            Transition: initializes a powerup object with random position
            input:none
            output:none
        """
        self.position = pygame.Rect(random.randrange(55) * 10, random.randrange(45) * 10, 10, 10)