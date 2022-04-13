import RPi.GPIO as io
import time
from subprocess import *

io.setwarnings(False)
io.setmode(io.BCM)

io.setup(4, io.IN, io.PUD_UP)

def bash(cmd):
    return Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)

def getTimestamp():
    month = bash('date +%D | cut -f1 -d/').communicate()[0].decode('ascii')[0:2]
    day = bash('date +%D | cut -f2 -d/').communicate()[0].decode('ascii')[0:2]
    year = bash('date +%D | cut -f3 -d/').communicate()[0].decode('ascii')[0:2]
    hour = int(bash('date +%T | cut -f1 -d:').communicate()[0].decode('ascii')[0:2])
    minute = bash('date +%T | cut -f2 -d:').communicate()[0].decode('ascii')[0:2]
    second = bash('date +%T | cut -f3 -d:').communicate()[0].decode('ascii')[0:2]
    ampm = 'am'
    if hour >= 12:
        ampm = 'pm'
        if hour > 12:
            hour -= 12
    if hour == 0:
        hour += 12
    date = month + '/' + day + '/' + year
    timestamp = str(hour) + ':' + minute + ':' + second + ' ' + ampm
    bash('echo ' + date + ' >> log.txt')
    bash('echo ' + timestamp + ' >> log.txt')

while True:

  if io.input(4) == 0:
    print("Door opened")
    bash('echo "Door opened:" >> log.txt')
    getTimestamp()
    time.sleep(.1)
    bash('echo >> log.txt')
    time.sleep(.1)
    bash('cp /home/pi/log.txt /home/Shared')
    doorOpen = not io.input(4)
    count = 0
    timestamp = [0, 0, 0]
    while doorOpen:
        doorOpen = not io.input(4)
        count += 1
        time.sleep(1)
    print("Door closed")
    bash('echo "Door closed:" >> log.txt')
    getTimestamp()
    time.sleep(.1)

    #convert seconds to minutes
    while count > 60:
        timestamp[1] += 1
        count -= 60

    #convert minutes to hours
    while timestamp[1] > 60:
        timestamp[0] += 1
        timestamp[1] -= 60

    #remaining count = seconds    
    timestamp[2] = count
    
    bash('echo "Open for ' + str(timestamp[0]) + ' hours, ' + str(timestamp[1]) + ' minutes, ' + str(timestamp[2]) + ' seconds" >> log.txt')
    time.sleep(.1)
    bash('echo >> log.txt')
    time.sleep(.1)
    bash('cp /home/pi/log.txt /home/Shared')

  time.sleep(1)