import pygame
"""
Snake class is used by PlayMap to model the snake game environment
"""
class Snake:
    """
    Snake class encapsulates the characteristics of the snake

    State variables:
        life: boolean
        direction: integer
        points[]: list of pygame.Rect objects

    assumption: __init__ is executed first
    """
    
    # x,y coordinate of the head of the snake
    def __init__(self):
        """
            Constructor method for Snake
            Transition: initialized into new snake of length 20
            input:none
            output:none
        """
        #DIRECTIONS: -1=down,1=up,-2=left,2=right
        self.direction = -1
        # READ AS: points[i] shows [x,y] for ith object
        self.points = []

        #make a vertical snake 20 points long
        for i in range(20):
            self.points.insert(i,pygame.Rect(250,290-i*10,10,10))



    def __repr__(self) :
        return (str(self.points)+str(self.direction))
    
        
    # updates direction if it is valid
    def changeDir(self,direction):
        """
            function to change the current direction the snake is headed
            
            Transition: changes value of the direction based on passed value
            input:integer value corresponding to new direction
            output:none

            exception: when the new direction is the same or opposite direction of current direction,
                        dont update
        """
        if (self.direction!=direction and self.direction!=-direction): self.direction = direction

    # increase size of the snake
    def grow(self):
        """
            function to increase the size of the snake
            
            Transition: adds a point to the snake
            input:none
            output:none
        """
        #appends a duplicate of the last point of snake to the points list
        self.points.insert(len(self.points)+1,self.points[-1])

    # Moves snake in current direction
    def move(self) :
        """
            function to move the snake forward
            
            Transition: moves the points of the snake forward by one
            input:none
            output:none
        """
        #remove tail of the snake
        self.points.pop(-1)

        #based on the direction, add a new point to the head
        if self.direction==1:
            self.points.insert(0,pygame.Rect(self.points[0].left,self.points[0].top-10,10,10))
        if self.direction==-1:
            self.points.insert(0,pygame.Rect(self.points[0].left,self.points[0].top+10,10,10))
        if self.direction==2:
            self.points.insert(0,pygame.Rect(self.points[0].left+10,self.points[0].top,10,10))
        if self.direction==-2:
            self.points.insert(0,pygame.Rect(self.points[0].left-10,self.points[0].top,10,10))
    
    # remove all points after passed index
    def remove(self,index) :
        """
            function to remove all points on the snake after index passed
            
            Transition: removes points on the snake after passed index
            input:integer value corresponding to an index value
            output:none
        """
        try:
            while len(self.points) != index+1 : self.points.pop()
        except IndexError:
            pass
                        
