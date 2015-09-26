#tornado along the z-axis

from visual import *
import math

def main():

    Screen = display(x=0, y=0, width=600, height=600, center=(0,0,0),
    background=(.49,.75,.93))

    x = 0
    y = 0
    z = 0
    i = 1
    m = []
    n = []
    o = []
    p = []
    
    while i <= 101:
        m.append(sphere(pos=vector(x,y,z),radius=.5,color=color.cyan))
        x = i*math.cos(i)
        y = i*math.sin(i)
        z = math.sqrt(270*i)
        i = i + 1

    x = 0
    y = 0
    z = 0
    i = 1
    while i <= 101:
        n.append(sphere(pos=vector(x,y,z),radius=.6,color=color.red))
        x = i*math.cos(i)
        y = i*math.sin(i)
        z = math.sqrt(270*i)
        i = i + 1

    x = 0
    y = 0
    z = 0
    i = 1

    while i <= 101:
        o.append(sphere(pos=vector(x,y,z),radius=.7,color=color.blue))
        x = i*math.cos(i)
        y = i*math.sin(i)
        z = math.sqrt(270*i)
        i = i + 1

    x = 0
    y = 0
    z = 0
    i = 1

    while i <= 101:
        p.append(sphere(pos=vector(x,y,z),radius=.5,color=color.green))
        x = i*math.cos(i)
        y = i*math.sin(i)
        z = math.sqrt(270*i)
        i = i + 1

    box1 = box(pos=vector(17,12,67),size=(7,7,7),color=color.blue) 
    box2 = box(pos=vector(-42,38,194),size=(7,7,7),color=color.red)
    box3 = box(pos=vector(71,-21,147),size=(7,7,7),color=color.magenta)
    box4 = box(pos=vector(-17,-12,157),size=(7,7,7),color=color.orange)
    box5 = box(pos=vector(-42,-38,86),size=(7,7,7),color=color.cyan)
    box6 = box(pos=vector(71,-23,136),size=(7,7,7),color=color.blue)

    r1 = vector(17,12,67)
    r2 = vector(-42,38,194)
    r3 = vector(71,-21,147)
    r4 = vector(-17,-12,57)
    r5 = vector(-42,-38,86)
    r6 = vector(71,-23,36)

    sr1 = math.sqrt((17**2) + (12**2))
    sr2 = math.sqrt((43**2) + (38**2))
    sr3 = math.sqrt((71**2) + (21**2))
    sr4 = math.sqrt((17**2) + (12**2))
    sr5 = math.sqrt((43**2) + (38**2))
    sr6 = math.sqrt((71**2) + (21**2))
        
    t = 0

    while (1 < 2):
    
        rate(100)
        for f in range(1,101):

            xin = f
            yin = f
            
            r = m[f].pos
            r.x = xin*math.cos(t)
            r.y = yin*math.sin(t)
        
            r = n[f].pos
            r.x = xin*math.cos(t + (math.pi/2))
            r.y = yin*math.sin(t + (math.pi/2))

            r = o[f].pos
            r.x = xin*math.cos(t + math.pi)
            r.y = yin*math.sin(t + math.pi)
       
            r = p[f].pos
            r.x = xin*math.cos(t + (3*math.pi/2))
            r.y = yin*math.sin(t + (3*math.pi/2))
            
            box1.pos = r1
            box2.pos = r2
            box3.pos = r3
            box4.pos = r4
            box5.pos = r5
            box6.pos = r6
            
            r1.x = sr1*math.cos(t/2)
            r1.y = sr1*math.sin(t/2)
            r2.x = sr2*math.cos((t/3) + (math.pi/2))
            r2.y = sr2*math.sin((t/3) + (math.pi/2))
            r3.x = sr3*math.cos((t/4) + (3*math.pi/2))
            r3.y = sr3*math.sin((t/4) + (3*math.pi/2))
            r4.x = sr4*math.cos((t/5) + (math.pi/4))
            r4.y = sr4*math.sin((t/5) + (math.pi/4))
            r5.x = sr5*math.cos((t/6) + (9*math.pi/2))
            r5.y = sr5*math.sin((t/6) + (9*math.pi/2))
            r6.x = sr6*math.cos((t/7) + (7*math.pi/2))
            r6.y = sr6*math.sin((t/7) + (7*math.pi/2))
            
##WARNING: ACTIVATING THIS PART OF THE CODE WILL CREATE LIGHTNING IN THE TORNADO!  

            box1.axis = m[100].pos - m[0].pos
            box2.axis = n[100].pos - n[0].pos
            box3.axis = o[100].pos - o[0].pos
            box4.axis = p[100].pos - p[0].pos
            box5.axis = m[100].pos - m[0].pos
            box6.axis = n[100].pos - n[0].pos

            box1.size=(0.5,0.5,0.5)
            box2.size=(0.5,0.5,0.5)
            box3.size=(0.5,0.5,0.5)
            box4.size=(0.5,0.5,0.5)
            box5.size=(0.5,0.5,0.5)
            box6.size=(0.5,0.5,0.5)

        t = t + 0.1
        
main() 