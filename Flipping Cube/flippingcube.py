#flipping cube

from visual import *
import math

def main():

    window = display(title="Color Box", x=0, y=0, width = 600, height = 600,
                     center=(0,0,0), background=(.96,.96,.96))

    redbox = box(pos=vector(-0.25,0.25,0.25), size=(.5,.5,.5),
                 color = (0,.35,0))
    redbox1a = box(pos=vector(0.25,0.25,0.25), size=(.5,.5,.5),
                 color = color.blue, opacity = 0.15)
    redbox2a = box(pos=vector(0.25,-0.25,0.25), size=(.5,.5,.5),
                  color = color.blue, opacity = 0.15)
    redbox3a = box(pos=vector(-0.25,-0.25,0.25), size=(.5,.5,.5),
                  color = color.blue, opacity = 0.15)
    redbox4a = box(pos=vector(-0.25,0.25,0.25), size=(.5,.5,.5),
                  color = color.blue, opacity = 0.15)
    redbox1b = box(pos=vector(0.25,0.25,-0.25), size=(.5,.5,.5),
                 color = color.blue, opacity = 0.15)
    redbox2b = box(pos=vector(0.25,-0.25,-0.25), size=(.5,.5,.5),
                  color = color.blue, opacity = 0.15)
    redbox3b = box(pos=vector(-0.25,-0.25,-0.25), size=(.5,.5,.5),
                  color = color.blue, opacity = 0.15)
    redbox4b = box(pos=vector(-0.25,0.25,-0.25), size=(.5,.5,.5),
                  color = color.blue, opacity = 0.15)

    ang = 0

    redaxis = arrow(pos=vector(1,1,1), axis=(1,0,0), color = color.red)
    blueaxis = arrow(pos=vector(1,1,1), axis=(0,1,0), color = color.blue)
    greenaxis = arrow(pos=vector(1,1,1), axis=(0,0,1), color = color.green)

    while true:
        rate(100)
              
        while (redbox.pos >= (-2.5,2.5,2.5)):
                while (redbox.pos.x < 2.5):
                    redbox.rotate(angle=-(pi/180), axis=(0,1,0), origin=(0,0,0.5))
                    redbox.color = (0,.35,0)
            
##        if (-2.5 <= redbox.pos.x <= 2.5 && 0 < redbox.pos.y <= 2.5 && 0 < redbox.pos.z <= 2.5):
##            redbox.rotate(angle=-(pi/180), axis=(1,0,0), origin=(0,0,0.25))
##            redbox.color = (.93,.46,0)
##                        
##        if (-2.5 <= redbox.pos.x <= 2.5 && 0 < redbox.pos.y <= 2.5 && 0 < redbox.pos.z <= 2.5):
##            redbox.rotate(angle=-(pi/180), axis=(0,1,0), origin=(0,0,0))
##            redbox.color = (.93,.79, 0)
##   
##        if (-2.5 <= redbox.pos.x <= 2.5 && 0 < redbox.pos.y <= 2.5 && 0 < redbox.pos.z <= 2.5):
##            redbox.rotate(angle=(pi/180), axis=(1,0,0), origin=(0,0,0))
##            redbox.color = (0,.25,.53)

##        ang = ang + (pi/180)
##        
##        if (ang <= (pi/2)):
##            redbox.rotate(angle=(pi/180), axis=(0,1,0), origin=(0,0,0))
##            redbox.color = (0,.35,0)
##            
##        if ((pi/2) < ang <= pi):
##            redbox.rotate(angle=-(pi/180), axis=(1,0,0), origin=(0,0,0))
##            redbox.color = (.93, .46,0)
##                        
##        if (pi < ang <= (3*pi/2)):
##            redbox.rotate(angle=-(pi/180), axis=(0,1,0), origin=(0,0,0))
##            redbox.color = (.93, .79, 0)
##   
##        if ((3*pi/2) < ang <= (2*pi)):
##            redbox.rotate(angle=(pi/180), axis=(1,0,0), origin=(0,0,0))
##            redbox.color = (0,.25,.53)
##   
##        if (ang > (2*pi)):
##            ang = 0
