##visual4.py
##This works!
from visual import *
import math

def main():
    
    WindowsOS = display(title='Windows',
    x=0, y=0, width=600, height=600, center=(0,0,0),
    background=(.49,.75,.93))

    MyText = text(text='Windows', align = "center", depth=-0.4,
                  color=(.96,.96,.96), font = "Verdana",
                  material=materials.emissive, height = 4)

    diam = (5/sqrt(2))

    a = box(pos=vector(10,10,10), size=(5,5,5), color = (0,.35,0))
    b = box(pos=vector(-10,10,10), size=(5,5,5), color =  (.93, .46,0))
    c = box(pos=vector(-10,-10,10), size=(5,5,5), color = (.93, .79, 0))
    d = box(pos=vector(10,-10,10), size=(5,5,5), color = (0,.25,.53))
    e = sphere(pos=vector(10,10,-10), radius = diam, color = (0,.35,0))
    f = sphere(pos=vector(-10,10,-10), radius = diam, color = (.93, .46,0))
    g = sphere(pos=vector(-10,-10,-10), radius = diam, color = (.93, .79, 0))
    h = sphere(pos=vector(10,-10,-10), radius = diam, color = (0,.25,.53))

    r1 = vector(10,10,10)
    r2 = vector(-10,10,10)
    r3 = vector(-10,-10,10)
    r4 = vector(10,-10,10)
    r5 = vector(10,10,-10)
    r6 = vector(-10,10,-10)
    r7 = vector(-10,-10,-10)
    r8 = vector(-10,-10,-10)

    t = 0
    while true:
        rate(1000)
        a.pos = r1
        b.pos = r2
        c.pos = r3
        d.pos = r4
        e.pos = r5
        f.pos = r6
        g.pos = r7
        h.pos = r8
    
        m = math.cos(t)
        n = math.sin(t)

        r1.x = 10*m
        r1.y = 10*m
        r1.z = 10*n

        r2.x = -10*m
        r2.y = 10*m
        r2.z = 10*n

        r3.x = 10*m
        r3.y = -10*m
        r3.z = 10*n

        r4.x = -10*m
        r4.y = -10*m
        r4.z = 10*n

        r5.x = 10*m
        r5.y = 10*m
        r5.z = -10*n

        r6.x = -10*m
        r6.y = 10*m
        r6.z = -10*n

        r7.x = 10*m
        r7.y = -10*m
        r7.z = -10*n

        r8.x = -10*m
        r8.y = -10*m
        r8.z = -10*n
        
        t = t + 0.001
        

##
##        if 0 <= t < 90:
##            r.x = 10*m
##            r.y = 10*n
##
##        if 90 <= t < 180:
##            r.x = 10*m
##            r.y = 10*n
##
##        if 180 <= t < 270:
##            r.x = 10*m
##            r.y = 10*n
##            
##        if 270 <= t <= 360:
##            r.x = 10*m
##            r.y = 10*n
##
##        else:
##            t = 0
            
main() 
        
