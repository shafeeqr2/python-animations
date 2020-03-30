#pingpong

from vpython import *
import math
import random
import string


GRAVITY = -0.2
HALF_RADIUS_OF_BALL = 0.075
TIME_COEFFICIENT = 0.45
score = 0
game_over = False

color_list = [color.red, color.blue, color.black, color.yellow]
color_index = 0

computer = box (pos = vector(0, 0, -3), color = color.green, size = vector(1.5, 0.05, 0.30))
player = box (pos = vector(0, 0, 3), color = color.blue, size = vector(1.5, 0.05, 0.30))
ball = sphere(pos = vector(0, 2, 0), radius = 0.1, color = color_list[0])
glass = box(pos = vector(0, 1.5, 0), color = color.blue, size = vector(3, 3, 6), opacity = 0.1)
scoreboard = label(pos=vector(0, 3.8, 0), text ="", color = color.black)
scene.background = vector(.96, .96, .96)
game_over_text = text(pos=vector(-5, 0,0), text="GAME OVER", align=vector(0, 0, 0), depth = -0.1, color = color.red, visible = False)

scene.width = scene.height = 800

def prepare_game():
    
    scene.forward = vector(0, -0.25, -1)
    ball.velocity = vector(0,0,0.65)
    ball.velocity.x = random.random()*0.5
    ball.pos = vector(0, 2, 0)
    game_over_text.visible = False
    glass.visible = True
    player.pos.x = 0

prepare_game()

while True:

    if not game_over:
    
        score = score + 1
        scoreboard.text = "SCORE: %d" %score

        ball.velocity.y = ball.velocity.y + GRAVITY*TIME_COEFFICIENT

        ball.pos.x = ball.pos.x + ball.velocity.x*TIME_COEFFICIENT
        ball.pos.y = ball.pos.y + ball.velocity.y*TIME_COEFFICIENT
        ball.pos.z = ball.pos.z + ball.velocity.z*TIME_COEFFICIENT


        plminx = player.pos.x - 0.75
        plmaxx = player.pos.x + 0.75
        plminz = player.pos.z - 0.15

        cpminz = computer.pos.z + 0.15
        cpmaxz = computer.pos.z - 0.15

        computer.pos.x = ball.pos.x


        ## HALF_RADIUS_OF_BALL comes from the radius of the ball + height of slider above ground .i.e. 0.0
        if (plminz <= ball.pos.z):
            if (plminx <= ball.pos.x <= plmaxx):
                if (ball.pos.y <= HALF_RADIUS_OF_BALL):

                    ball.pos.z = 2.85
                    ball.pos.y = 0.076
                    ball.velocity.x = random.random()*0.5
                    ball.velocity.y = -ball.velocity.y
                    ball.velocity.z = -ball.velocity.z
                    score = score + 100
                    color_index = (color_index + 1)%4
                    ball.color = color_list[color_index]

        if (cpminz >= ball.pos.z):
            if (ball.pos.y < HALF_RADIUS_OF_BALL):

                ball.pos.z = -2.85
                ball.pos.y = 0.076
                ball.velocity.x = random.random()*0.5
                ball.velocity.y = -ball.velocity.y
                ball.velocity.z = -ball.velocity.z
                color_index = (color_index + 1)%4
                ball.color = color_list[color_index]


        if (ball.pos.x <= -1.5):
            ball.pos.x = -1.5
            ball.velocity.x = -ball.velocity.x

        if (ball.pos.x >= 1.5):
            ball.pos.x = 1.5
            ball.velocity.x = -ball.velocity.x
        
        if (ball.pos.y <= 0):
            game_over = True
            glass.visible = False
            game_over_text.visible = True

            print ('Game over!!')
    
    k = keysdown()
    
    if not game_over:

        #move left
        if 'a' in k or 'A' in k: 
            if player.pos.x > -1:
                player.pos.x = player.pos.x - 1
        
        #move right
        if 'd' in k or 'D' in k:            
            if player.pos.x < 1:
                player.pos.x = player.pos.x + 1
    
    else:
        #Restart the game
        if 'r' in k or 'R' in k:
            TIME_COEFFICIENT = 0.45
            score = 0
            game_over = False
            prepare_game()
    
    rate(18)
            
