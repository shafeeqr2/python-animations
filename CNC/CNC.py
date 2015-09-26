#CNC - 2D

from visual import *
from visual.filedialog import get_file
import math

def main():

    xc = 0
    yc = 0
    zc = -0.5
    vn = " A"
    vis = True
    res = 0
    allcodes = ""
    codelist = []
    code = ""
    letter = ""
    typein = 0
    rowin = 0
    xint = 0

    m = 1
    t = 2
    ink = 0.1

    scene.width = 800
    scene.height = 600
    scene.title = "2D CNC"
    scene.forward = (0,1,0)
    scene.background = color.white
    center = (0,0,0)

    lamp = local_light(pos = (0,-2.5,1.5), color = color.white)
    blackyellow = ((0,1,0,1,0,1,0,1),(0,1,0,1,0,1,0,1))
    blackyellow2 = ((0,0),(1,1),(0,0),(1,1),(0,0),(1,1),(0,0),(1,1))
    horlines = materials.texture(data = blackyellow, mapping = "rectangular", interpolate = False)
    verlines = materials.texture(data = blackyellow2, mapping = "rectangular", interpolate = False)

    pen = cylinder(pos = (0,0,-0.5), axis = (0,0,1), radius = 0.25)
    pen.length = 4
    pen.material = materials.shiny
    pen.color = color.black

    peak = cone(pos = (0,0,-0.5), axis = (0,0,-1), radius = 0.25)
    peak.color = color.black
    peak.material = materials.shiny
    peak.length = 1

    ballpoint = sphere(pos = vector (0,0,-5), color = color.blue, radius = 0.05)
    ballpoint.visible = False

    pole1 = box(pos = (-5,-5,0), size = (1,1,5), color = color.yellow, material = horlines)
    pole2 = box(pos = (5,-5,0), size = (1,1,5), color = color.yellow, material = horlines)
    pole3 = box(pos = (-5,5,0), size = (1,1,5), color = color.yellow, material = horlines)
    pole4 = box(pos = (5,5,0), size = (1,1,5), color = color.yellow, material = horlines)

    bridge12 = box(pos=(-5,0,2), size = (1,9,1), material = materials.blazed)
    bridge34 = box(pos=(5,0,2), size = (1,9,1), material = materials.blazed)

    hormet1 = cylinder(pos = (-4.25, 0.75 + yc, 3), axis = (1,0,0), length = 8.5,
                       radius = 0.25, material = materials.shiny)

    hormet2 = cylinder(pos = (-4.25, -0.75 + yc, 3), axis = (1,0,0), length = 8.5,
                       radius = 0.25, material = materials.shiny)

    xaxisbox = box(pos =(0,0,3), size = (1.5, 3, 1.1), color = color.yellow, material = verlines)

    yaxisbridge12 = box(pos=(-5,0,2.375), size = (1.5, 2.5, 2.75), color = color.yellow, material = verlines)
    yaxisbridge34 = box(pos=(5,0,2.375), size = (1.5, 2.5, 2.75), color = color.yellow, material = verlines)

    platform = box(pos=(0,0,-2.5), size = (12,12,0.125), material = materials.wood)
    sheet = box(pos=(0,0,-2.375), size = (10,10,0.125), material = materials.plastic)

    xcoord = label(yoffset = 260, xoffset = 265, line = 0, text = "", color = color.black)
    ycoord = label(yoffset = 230, xoffset = 265, line = 0, text = "", color = color.black)
    zcoord = label(yoffset = 200, xoffset = 265, line = 0, text = "PEN UP", color = color.black)
    viewn = label(yoffset = 170, xoffset = 265, line = 0, text = "", color = color.black)
    thickness = label(yoffset = 140, xoffset = 265, line = 0, text = "", color = color.black)

    while True:
        rate(1000)
	
        if scene.kb.keys:
            key = scene.kb.getkey()

            if key == "d" or key == "D":
                xc = xc + ink*m
                if zc == -1.25:
                    if (-3.5 <= xc <= 3.5) and (-3.3 <= yc <= 3.3):
                        box(pos = (xc,yc,zc - 1), size = (ink*m, ink*m, 0.1), color = color.black)

            if key == "a" or key == "A":
                xc = xc - ink*m
                if zc == -1.25:
                    if (-3.5 <= xc <= 3.5) and (-3.3 <= yc <= 3.3):
                        box(pos = (xc,yc,zc - 1), size = (ink*m, ink*m, 0.1), color = color.black)

            if key == "w" or key == "W":
                yc = yc + ink*m
                if zc == -1.25:
                    if (-3.5 <= xc <= 3.5) and (-3.3 <= yc <= 3.3):
                        box(pos = (xc,yc,zc - 1), size = (ink*m, ink*m, 0.1), color = color.black)

            if key == "x" or key == "X":
                yc = yc - ink*m
                if zc == -1.25:
                    if (-3.5 <= xc <= 3.5) and (-3.3 <= yc <= 3.3):
                        box(pos = (xc,yc,zc - 1), size = (ink*m, ink*m, 0.1), color = color.black)

            if key == "e" or key == "E":
                xc = xc + ink*m
                yc = yc + ink*m

                if zc == -1.25:
                    if (-3.5 <= xc <= 3.5) and (-3.3 <= yc <= 3.3):
                        box(pos = (xc,yc,zc - 1), size = (ink*m, ink*m, 0.1), color = color.black)
    
            if key == "q" or key == "Q":
                xc = xc - ink*m
                yc = yc + ink*m

                if zc == -1.25:
                    if (-3.5 <= xc <= 3.5) and (-3.3 <= yc <= 3.3):
                        box(pos = (xc,yc,zc - 1), size = (ink*m, ink*m, 0.1), color = color.black)
		
            if key == "z" or key == "Z":
                yc = yc - ink*m
                xc = xc - ink*m

                if zc == -1.25:
                    if (-3.5 <= xc <= 3.5) and (-3.3 <= yc <= 3.3):
                        box(pos = (xc,yc,zc - 1), size = (ink*m, ink*m, 0.1), color = color.black)
		
            if key == "c" or key == "C":
                xc = xc + ink*m
                yc = yc - ink*m

                if zc == -1.25:
                    if (-3.5 <= xc <= 3.5) and (-3.3 <= yc <= 3.3):
                        box(pos = (xc,yc,zc - 1), size = (ink*m, ink*m, 0.1), color = color.black)

            if key == "s" or key == "S":
                if zc == -0.5:
                    zc = -1.25
                    zcoord.text = "PEN DOWN"
                else:
                    zc = -0.5
                    zcoord.text = "PEN UP"

            if key == "1":
                scene.forward = (0,1,0)
                vn = 1

            if key == "2":
                scene.forward = (0,1,-1)
                vn = 2
		
            if key == "3":
                scene.forward = (0,0,-1)
                vn = 3

            if key == "4":
                if vis == True:
                    vis = False
                else:
                    vis = True

            if key == "r" or key == "R":
			
                xc = 0
                yc = 0
                zc = -0.5
                pen.pos.x = xc
                peak.pos.x = xc
                xaxisbox.pos.x = xc

                pen.pos.y = yc
                peak.pos.y = yc
                xaxisbox.pos.y = yc
                yaxisbridge12.pos.y = yc
                yaxisbridge34.pos.y = yc
                hormet1.pos.y = yc + 0.75
                hormet2.pos.y = yc - 0.75
		
                pen.pos.z = zc
                peak.pos = (xc,yc,zc)
                
                ballpoint.pos.x = xc
                ballpoint.pos.y = yc
                ballpoint.pos.z = -2.25
			
                t = 2
                ink = 0.1
                m = 1

            if key == "v" or key == "V":

                xc = -3.5
                yc = 3.3
                zc = -0.5
                pen.pos.x = xc
                peak.pos.x = xc
                xaxisbox.pos.x = xc

                pen.pos.y = yc
                peak.pos.y = yc
                xaxisbox.pos.y = yc
                yaxisbridge12.pos.y = yc
                yaxisbridge34.pos.y = yc
                hormet1.pos.y = yc + 0.75
                hormet2.pos.y = yc - 0.75

                pen.pos.z = zc
                peak.pos = (xc, yc, zc)

                ballpoint.pos.x = xc
                ballpoint.pos.y = yc
                ballpoint.pos.z = -2.25

                t = 2
                ink = 0.1
                m = 1
		
            if key == "m" or key == "M":
                m = m + 1
			
                if m > 5:
                    m = 1
		
            if key == "t" or key == "T":
		
                t = t + 1
			
                if t == 2:
                    ink = 0.1
			
                if t == 3:
                    ink = 1
			
                if t > 3:
                    t = 1
                    ink = 0.01
		
            if key == "n" or key == "N":
			
                xint = xc
			
                design = get_file()
                allcodes = design.read()
                codelist = allcodes.split()
			
                rowin = len(codelist)
                res = len(codelist[0])
			
                #print allcodes
                #print rowin
                #print res
			
                for i in range (rowin):
                    code = codelist[i]
                		
                    for j in range (res - 1):		
                        letter = code[j]
                        typein = int(letter)
                        		
                        #print letter
                        #print "typein" + str(typein)

                        if typein == 1:
                            zc = -1.25
				    
                        if typein == 0:
                            zc = -0.5
					
                        for k in range (3):
                            pen.pos.z = zc
					
                            #print pen.pos.x
                            #print pen.pos.z
					
                            xc = xc + ink*m
                            pen.pos.x = xc
                            peak.pos.x = xc
                            xaxisbox.pos.x = xc
						
                            pen.pos.y = yc
                            peak.pos.y = yc
                            xaxisbox.pos.y = yc
                            yaxisbridge12.pos.y = yc
                            yaxisbridge34.pos.y = yc
                            hormet1.pos.y = yc + 0.75
                            hormet2.pos.y = yc - 0.75
						
                            ballpoint.pos.x = xc
                            ballpoint.pos.y = yc
						
                            if typein == 1:
                                box(pos = (xc,yc,zc - 1), size = (ink*m,ink*m,ink*m), color = color.black)
						
                            if xc >= 3.5:
                                xc = 3.5
						
                            if xc <= -3.5:
                                xc = -3.5
						
                            if yc >= 3.3:
                                yc = 3.3
						
                            if yc <= -3.3:
                                yc = -3.3
				
                    yc = yc - ink*m
                    xc = xint
                                    
        if xc >= 3.5:
            xc = 3.5
                
        if xc <= -3.5:
            xc = -3.5
                        
        if yc >= 3.3:
            yc = 3.3
                        
        if yc <= -3.3:
            yc = -3.3
                        
        if vis == False:
            pen.opacity = 0.1
            peak.opacity = 0.1
            hormet1.opacity = 0.1
            hormet2.opacity = 0.1
            xaxisbox.opacity = 0.1
            ballpoint.visisble = True

        else:
            pen.opacity = 1
            peak.opacity = 1
            hormet1.opacity = 1
            hormet2.opacity = 1
            xaxisbox.opacity = 1
            ballpoint.visible = False
                
        pen.pos.x = xc
        peak.pos.x = xc
        xaxisbox.pos.x = xc
                        
        pen.pos.y = yc
        peak.pos.y = yc
        xaxisbox.pos.y = yc
        yaxisbridge12.pos.y = yc
        yaxisbridge34.pos.y = yc
        hormet1.pos.y = yc + 0.75
        hormet2.pos.y = yc - 0.75

        ballpoint.pos.x = xc
        ballpoint.pos.y = yc
        ballpoint.pos.z = -2.25
                        
        xcoord.text = "x-coordinate:" + str(xc)
        ycoord.text = "y-coordinate:" + str(yc)
        viewn.text = "View:" + str(vn)
        thickness.text = str(ink) + " x " + str(m)

main()
