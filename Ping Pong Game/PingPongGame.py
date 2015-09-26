#pingpong

from visual import *
import math
import random
import string

scene.width = scene.height = 800
scene.title = "Ping Pong"
scene.forward = (0,-0.25,-1)
scene.background = (.96,.96,.96)
center = (0,0,0)
stopper = 1
score = 0
sentence = ""
computer = box (pos = vector(0,0,-3), color = color.green, size = (1.5, 0.05, 0.30))
player = box (pos = vector(0,0,3), color = color.blue, size = (1.5, 0.05, 0.30))
ball = sphere(pos = vector(0,2,0), radius = 0.1, color = color.red)
glass = box(pos = vector(0,1.5,0), color = color.blue, size = (3,3,6), opacity = 0.1)
scoreboard = text (text = sentence, align='center', depth = -0.3, color = color.blue, height = 1,
                   pos = vector(0,1.2,0))
miniscoreboard = label(pos=(0,3.8,0), text ="", color = color.black)

ball.velocity = vector (0,0,0.65)
dt = 0
g = -0.2

right_text = text(text="right", align='center', depth = -0.3, color = color.green)
left_text = text(text="left", align='center', depth = -0.1, color = color.green)
gmover = text(text="GAME OVER", align='center', depth = -0.1, color = color.red)

gmover.visible = False
right_text.visible = False
left_text.visible = False
scoreboard.visible = False

while True:

    dt = dt + 0.002
    score = score + dt*500*stopper
    miniscoreboard.text = "SCORE: %d" %score
    ball.velocity.y = ball.velocity.y + g*dt
    ball.pos.x = ball.pos.x + ball.velocity.x*dt
    ball.pos.y = ball.pos.y + ball.velocity.y*dt
    ball.pos.z = ball.pos.z + ball.velocity.z*dt

    plminx = player.pos.x - 0.75
    plmaxx = player.pos.x + 0.75

    plminz = player.pos.z - 0.15

    cpminz = computer.pos.z + 0.15
    cpmaxz = computer.pos.z - 0.15

    computer.pos.x = ball.pos.x

    if scene.kb.keys:
        key = scene.kb.getkey()
        if key == "a" or key == "A":
##            right_text.visible = False
##            left_text.vislbe = True
            if player.pos.x > -1:
                player.pos.x = player.pos.x - 1*stopper
                
        if key == "d" or key == "D":
##            left_text.visible = False
##            right_text.visible = True
            if player.pos.x < 1:
                player.pos.x = player.pos.x + 1*stopper

## 0.075 comes from the radius of the ball + height of slider above ground .i.e. 0.0

    if (plminz <= ball.pos.z):
        if (plminx <= ball.pos.x):
            if (ball.pos.x <= plmaxx):
                if (ball.pos.y <= 0.075):

                    ball.pos.z = 2.85
                    ball.pos.y = 0.076
                    ball.velocity.x = random.random()
                    ball.velocity.y = ball.velocity.y*(-1)
                    ball.velocity.z = ball.velocity.z*(-1)
                    dt = 0.45
                    score = score + 100

    if (cpminz >= ball.pos.z):
        if (ball.pos.y < 0.075):

            ball.pos.z = -2.85
            ball.pos.y = 0.076
            ball.velocity.x = random.random()
            ball.velocity.y = ball.velocity.y*(-1)
            ball.velocity.z = ball.velocity.z*(-1)
            dt = 0.45

    if (ball.pos.x >= 1):
        ball.pos.x = 1
        ball.velocity.x = ball.velocity.x*(-1)

    if (ball.pos.x <= -1):
        ball.pos.x = -1
        ball.velocity.x = ball.velocity.x*(-1)

    if (ball.pos.y <= 0):
        ball.pos.y = 0
        ball.velocity.x = 0
        ball.velocity.y = 0
        ball.velocity.z = 0
        stopper = 0
        gmover.visible = True
        scoreboard.text = "YOUR SCORE IS %d" %score
        miniscoreboard.visible = False
        scoreboard.visible = True
        right_text.visilbe = False
        left_text.visible = False
        glass.visible = False
    
    rate(18)
            
