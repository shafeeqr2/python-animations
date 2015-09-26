#bouncing ball

from visual import *
import math

def main():
    
    Screen = display (x = 0, y = 0, width = 600, height = 600, center = (0,0,0),
                      background = ((.96,.96,.96)))

    ball = sphere(pos=vector(-0.25,0.25,0), radius = 0.1,
                  color = color.red, make_trail=True,
                  trail_type="curve")
    mybox = box(pos=vector(0,0,0), length=1, height=1,
                width=1, color = color.blue,
                center = (0,0,0), opacity=0.20)
    ball.velocity = vector(.1,.2,.3)
    square = vector(0.5,0.5,0.5)
    square2 = vector(-0.5,-0.5,-0.5)
    dt = 0.01
                      
    while true:
        rate(100)

        ball.pos = ball.pos + ball.velocity*dt
            
        if (ball.x >= square.x - 0.1):
            ball.velocity.x = (-1)*ball.velocity.x
            if(ball.y >= square.y - 0.1):
                ball.velocity.y = (-1)*ball.velocity.y
                if (ball.z >= square.z - 0.1):
                    ball.velocity.z = (-1)*ball.velocity.z
            if (ball.z >= square.z - 0.1):
                ball.velocity.z = (-1)*ball.velocity.z
                if(ball.y >= square.y - 0.1):
                    ball.velocity.y = (-1)*ball.velocity.y

        if(ball.y >= square.y - 0.1):
            ball.velocity.y = (-1)*ball.velocity.y
            if (ball.x >= square.x - 0.1):
                ball.velocity.x = (-1)*ball.velocity.x
                if (ball.z >= square.z - 0.1):
                    ball.velocity.z = (-1)*ball.velocity.z
            if (ball.z >= square.z - 0.1):
                ball.velocity.z = (-1)*ball.velocity.z
                if (ball.x >= square.x - 0.1):
                    ball.velocity.x = (-1)*ball.velocity.x

        if (ball.z >= square.z - 0.1):
            ball.velocity.z = (-1)*ball.velocity.z
            if (ball.x >= square.x - 0.1):
                ball.velocity.x = (-1)*ball.velocity.x
                if(ball.y >= square.y - 0.1):
                    ball.velocity.y = (-1)*ball.velocity.y
            if(ball.y >= square.y - 0.1):
                ball.velocity.y = (-1)*ball.velocity.y
                if (ball.x >= square.x - 0.1):
                    ball.velocity.x = (-1)*ball.velocity.x

        if (ball.x <= square2.x + 0.1):
            ball.velocity.x = (-1)*ball.velocity.x       
            if(ball.y <= square2.y + 0.1):
                ball.velocity.y = (-1)*ball.velocity.y
                if (ball.z <= square2.z + 0.1):
                    ball.velocity.z = (-1)*ball.velocity.z
            if (ball.z <= square2.z + 0.1):
                ball.velocity.z = (-1)*ball.velocity.z
                if(ball.y <= square2.y + 0.1):
                    ball.velocity.y = (-1)*ball.velocity.y

        if(ball.y <= square2.y + 0.1):
            ball.velocity.y = (-1)*ball.velocity.y
            if (ball.x <= square2.x + 0.1):
                ball.velocity.x = (-1)*ball.velocity.x
                if (ball.z <= square2.z + 0.1):
                    ball.velocity.z = (-1)*ball.velocity.z
            if (ball.z <= square2.z + 0.1):
                ball.velocity.z = (-1)*ball.velocity.z
                if (ball.x <= square2.x + 0.1):
                    ball.velocity.x = (-1)*ball.velocity.x

        if (ball.z <= square2.z + 0.1):
            ball.velocity.z = (-1)*ball.velocity.z
            if (ball.x <= square2.x + 0.1):
                ball.velocity.x = (-1)*ball.velocity.x
                if(ball.y <= square2.y + 0.1):
                    ball.velocity.y = (-1)*ball.velocity.y
            if(ball.y <= square2.y + 0.1):
                ball.velocity.y = (-1)*ball.velocity.y
                if (ball.x <= square2.x + 0.1):
                    ball.velocity.x = (-1)*ball.velocity.x

main()
