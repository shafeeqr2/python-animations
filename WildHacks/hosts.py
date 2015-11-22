
from visual import *
IP_Address_List = []
#hosts with virtual containing
num_of_raw_lines = 0
num_of_hosts = 0
line = ""
second = 0
minute = 0
Network_Times = []
hour= 0
nextLine = False
time_counter = 0
#returns the number of lines
def file_len():
    count = 0
    thefile = open('share.txt', 'rb')
    while 1:
        buffer = thefile.read(8192*1024)
        if not buffer: break
        count += buffer.count('\n')
    print count
    thefile.close()
    return count

def increment_time():
    second = second + 1
    if second == 60:
        minute = minute + 1
        second = 0
        
    if minute == 60:
        hour = hour + 1
        minute = 0

    if hour == 12:
        hour = 0

def check_time():
    if rec_hour == hour:
        if rec_minute == minute:
            if rec_second == second:
                nextLine == True

if (nextLine == True):
    time_counter = time_counter + 1
    halo = Network_Times[time_counter]
                
def get_timings():

    #num_of_hosts = true_hosts()
    thefile2 = open('share.txt', 'rb')
    count2 = 0
    counter = 0
    lines = thefile2.readlines()
    for i in range(len(lines)):
        print lines[i]      
        if (lines[i].find('00:00:00:00:00:00') == -1):
            count2 = count2 + 1

            lines[i] = lines[i][2:9]
            print lines[i]
        
            second = int(lines[i][1:2])
            minute = int(lines[i][4:5])
            hour = int(lines[i][7:8])

def get_current_timing():
    timing_counter = timing_counter + 1

    second = int(lines[i][1:2])
    minute = int(lines[i][4:5])
    hour = int(lines[i][7:8])

        
    print count2
    thefile2.close()
    num_of_hosts = count2
    

#returns actual number of devices connected
def true_hosts():
    thefile2 = open('share.txt', 'rb')
    count2 = 0
    lines = thefile2.readlines()
    for i in range(2,num_of_raw_lines):
        print lines[i]      
        if (lines[i].find('00:00:00:00:00:00') == -1):
            count2 = count2 + 1
            

    print count2
    thefile2.close()
    return count2

def main():

    num_of_raw_lines = file_len()
    
    #num_of_hosts = true_hosts()
    thefile2 = open('share.txt', 'rb')
    count2 = 0
    counter = 0
    lines = thefile2.readlines()
    for i in range(2,num_of_raw_lines):
        print lines[i]      
        if (lines[i].find('00:00:00:00:00:00') == -1):
            count2 = count2 + 1

            lines[i] = lines[i][6:23]
            print lines[i]
        
            IP_Address_List.append(lines[i])
            counter = counter + 1
        
    print count2
    thefile2.close()
    num_of_hosts = count2
    
main()

    
