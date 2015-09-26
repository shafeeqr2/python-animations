##visual4.py
##This works!
from visual import *
import math

def main():
    
    Background = display(title='Google',
    x=0, y=0, width=600, height=600, center=(0,0,0),
    background=(.96,.96,.96))
    
    # Here are the letters.
    G = text(text='G', pos=vector(-10,0,0), depth=-0.5,
                  color=(.2,.2,1), font = "Times",
                  material=materials.emissive, height = 4)
    
    O1 = text(text='o', pos=vector(-6,1,0), depth=-0.5,
                  color=(.89,.07,.19), font = "Times",
                  material=materials.emissive, height = 4)
    
    O2 = text(text='o', pos=vector(-3,3,0), depth=-0.5,
                  color=(.89,.51,.09), font = "Times",
                  material=materials.emissive, height = 4)

    smallG = text(text='g', pos=vector(0,2,0), depth=-0.4,
                  color=(.2,.2,1), font = "Times",
                  material=materials.emissive, height = 4)

    l = text(text='l', pos=vector(3,3,0), depth=-0.5,
                  color=(0,.55,0), font = "Times",
                  material=materials.emissive, height = 4)

    e = text(text='e', pos=vector(5,4,0), depth=-0.5,
                  color=(.89,.07,.19), font = "Times",
                  material=materials.emissive, height = 4)
    
    #Here's the bottom plate.

    plate = box(pos=vector(-1.5,-5,0), size=(0.25,22,5),
                color = (.99,.99,.99), axis = (0,1,0))

    #Motion under gravity
   
    G.velocity = vector(0,-1,0)
    O1.velocity = vector(0,-1,0)
    O2.velocity = vector(0,-1,0)
    smallG.velocity = vector(0,-1,0)
    l.velocity = vector(0,-1,0)
    e.velocity = vector(0,-1,0)
    dt = 0.01

    while 1:
        rate (100)
        
        G.pos = G.pos + G.velocity*dt
        if G.y < (plate.pos.y + 0.25):
            G.velocity.y = abs(G.velocity.y)
        else:
            G.velocity.y = G.velocity.y - 1.62*dt

        O1.pos = O1.pos + O1.velocity*dt
        if O1.y < (plate.pos.y + 0.25):
            O1.velocity.y = abs(O1.velocity.y)
        else:
            O1.velocity.y = O1.velocity.y - 1.62*dt

        O2.pos = O2.pos + O2.velocity*dt
        if O2.y < (plate.pos.y + 0.25):
            O2.velocity.y = abs(O2.velocity.y)
        else:
            O2.velocity.y = O2.velocity.y - 1.62*dt

        smallG.pos = smallG.pos + smallG.velocity*dt
        if smallG.y < (plate.pos.y + 2 + 0.25):
            smallG.velocity.y = abs(G.velocity.y)
        else:
            smallG.velocity.y = smallG.velocity.y - 1.62*dt

        l.pos = l.pos + l.velocity*dt
        if l.y < (plate.pos.y + 0.25):
            l.velocity.y = abs(l.velocity.y)
        else:
            l.velocity.y = l.velocity.y - 1.62*dt

        e.pos = e.pos + e.velocity*dt
        if e.y < (plate.pos.y + 0.25):
            e.velocity.y = abs(e.velocity.y)
        else:
            e.velocity.y = e.velocity.y - 1.62*dt

main()
    
