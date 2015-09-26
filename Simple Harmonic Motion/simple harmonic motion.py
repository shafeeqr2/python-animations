#simple harmonic motion

from visual import *
import math

def main():

    Screen = display(x=0, y=0, width=600, height=600, center=(0,0,0),
    background=(.49,.75,.93))
    a = sphere(pos=vector(0,0,0), radius = 0.5, color = color.cyan)
    b = box(pos=vector(0,5,0), size=(1,1,1), color = color.green)
    c = cylinder(pos=vector(0,5,0), radius = 0.05, axis = a.pos-b.pos, color=color.red)

    r = vector(0,0,0)
    t = 0
    A = 5.00
    w = 5.00
    phi = 0.121*math.pi

    while true:
        rate(500)
        a.pos = r
        r.x = A*math.cos(w*t + phi)
        r.y = -abs(A*math.sin(w*t))
        t = t + 0.001
        c.axis = a.pos - b.pos

main()
