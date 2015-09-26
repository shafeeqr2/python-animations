#SolarSystem

from visual import *
import math

def main():

    window = display(x = 0, y = 0, height = 600, width = 600, background = color.black)


    lamp = local_light(pos=(0,0,0), color=color.yellow)
    sun = sphere(pos = vector(0,0,0), radius = 20, color = color.yellow)
    earth = sphere(pos = vector (10, 0, 0), radius = 10,  material = materials.earth, make_trail = True, trail_type = "points", interval = 5) 
    moon = sphere(pos = vector(12, 0, 12), radius = 2.5, color = (0.96, 0.96, 0.96))

    axis1 = cylinder(pos = vector(10,-12.5,0), radius = 0.5, length = 25, axis = (-0.15, 1, 0), color = color.white, center = earth.pos)
    #axis1.visible = false
    
    i = 0
    j = 0

    while true:

        rate(35)

        i = i - ((2*pi)/365)
        j = j - ((2*pi)/28)

        x = 100*cos(i)
        z = 100*sin(i)
		
        earth.pos = (x,0,z)

        axis1.pos.x = earth.pos.x
        axis1.pos.z = earth.pos.z
        
        moon.pos.x = earth.pos.x + 20*cos(j)
        moon.pos.z = earth.pos.z + 20*sin(j)

        earth.rotate(angle = (pi/60) ,axis=(-0.15, 1, 0), origin = earth.pos)

main()	
