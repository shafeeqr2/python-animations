##this project is still in the works. For now the code is not very clean.

from visual import *

import math


scene.title = "Network Visualization"
scene.forward = (0,0,-1)
scene.background = color.black
center = (0,0,0)
n = 5
nextLine = False
timing_counter = 0
ball=[]
IP_Address=[]
Network_Times = []
victim=[]
attacker=[]
IP_Address_List = ['00:00:00:00:32:00','11:00:00:00:00:00','00:00:00:00:00:11','00:00:00:00:11:00','00:00:00:45:00:00']
rec_hour = '0'
rec_second = '0'
rec_minute = '0'
#hosts with virtual containing
num_of_raw_lines = 0
nu1m_of_hosts = 0
line = ""

#all timings are recorded and stored into Network_Times. This excecutes
# only once.
def get_timings():

    #num_of_hosts = true_hosts()
    thefile2 = open('share.txt', 'rb')
    count2 = 0
    counter = 0
    lines = thefile2.readlines()
    for i in range(len(lines)):
        #print lines[i]      
        #if (lines[i].find('00:00:00:00:00:00') == -1):
        count2 = count2 + 1

        lines[i] = lines[i][1:9]
        #print lines[i]
        Network_Times.append(lines[i])
            
    #print count2
    thefile2.close()

second = 50
hour = 11
minute = 4


    

#this goes third. It records the first element in the list and puts it into second,
#minute and hour.
    
def get_current_timing():
    rec_hour = Network_Times[timing_counter][0:2]
    rec_minute = Network_Times[timing_counter][3:5]
    rec_second = Network_Times[timing_counter][6:8]
    
    print int(rec_hour)
    print int(rec_minute)
    print int(rec_second)

    

#this goes fourth. It simply checks time to see if current time is the time stored in
def check_time():
    if int(rec_hour) == hour:
        print 'well...............................'
        if int(rec_minute) == (minute):
            if int(rec_second) == (second):
                nextLine = True
                print 'this is trueeeeeeeeeeeeeeeeeeeeee'


    
#returns the number of lines
def file_len():
    count = 0
    thefile = open('share.txt', 'rb')
    while 1:
        buffer = thefile.read(8192*1024)
        if not buffer: break
        count += buffer.count('\n')
    #print count
    thefile.close()
    return count



num_of_raw_lines = file_len()
    
#num_of_hosts = true_hosts()
thefile2 = open('share.txt', 'rb')
count2 = 0
counter = 0
lines = thefile2.readlines()

for i in range(num_of_raw_lines):
    #print lines[i]      
    #if (lines[i].find('00:00:00:00:00:00') == -1):
    count2 = count2 + 1

    lines[i] = lines[i][1:9]
    print lines[i]
                
    #IP_Address_List.append(lines[i])
        
    #print count2
    thefile2.close()
    num_of_hosts = count2
    

    

    get_timings()
while True:
    rate(5)
    check_time()
    #circumference
    cfm = 5
    factor = 2*math.pi/n
    #print factor



    #increment_time()

    #for i in Network_Times:
        #print 'howdy'
        #print i
    
    second = second + 1
    if second == 60:
        minute = minute + 1
        second = 0
        
    if minute == 60:
        hour = hour + 1
        minute = 0

    if hour == 12:
        hour = 0



    print str(hour) + str(minute) + str(second) + "ths"
    print rec_hour + 'x' + rec_minute + 'x' + rec_second
    #increment timing_counter by 1 and store the value.
    if (nextLine == True):
        get_current_timing()
        nextLine = False
        
        if (timing_counter < len(Network_Times)):
           timing_counter = timing_counter + 1

    for i in range(n):
        ball.append(sphere(pos=(cfm*sin(factor*i),cfm*cos(factor*i),1), radius=0.5, color = color.yellow))
        IP_Address.append(label(pos=(cfm*sin(factor*i),cfm*cos(factor*i),1), text= IP_Address_List[i], color = color.blue, box = false, yoffset = -3))

    #method for changing color of hosts.
    victim_box = sphere(visible = False)
    attacker_box = sphere(visible = False)
    for i in range(n):
    
        if (IP_Address[i].text == '00:00:00:00:11:00'):
            victim_box.pos = ball[i].pos
            victim_box.visible = False
            ball[i].color = color.blue
            #ball[i].visible = False
            
        if (IP_Address[i].text == '00:00:00:00:00:11'):
            attacker_box.pos = ball[i].pos
            attacker_box.visible = False
            ball[i].color = color.red
           # ball[i].visible = False
           
    attack_arrow = arrow(pos=(victim_box.pos), shaftwidth = 0.5,  axis=(attacker_box.pos - victim_box.pos))


