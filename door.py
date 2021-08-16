##### SETUP #####

import RPi.GPIO as io
import time
io.setmode(io.BCM)
io.setwarnings(False)

io.setup(22, io.OUT) #5/6
io.setup(27, io.OUT) #1/2
io.setup(24, io.OUT) #9/0
io.setup(23, io.OUT) #LOCK
io.output(22, 1)
io.output(27, 1)
io.output(24, 1)
io.output(23, 1)

##### MENU #####

while True:
    print("----------------")
    print("Door Lock:")
    print("(u) Unlock")
    print("(l) Lock")
    print("(x) Exit" )
    print("----------------")
    key = input('Enter command: ')


##### UNLOCK (6-1-9-5-9-9-1-1) #####

    if key == 'u':

        io.output(22, 0)
        time.sleep(.1)
        io.output(22, 1)
        time.sleep(.5)

        io.output(27, 0)
        time.sleep(.1)
        io.output(27, 1)
        time.sleep(.5)

        io.output(23, 0)
        time.sleep(.1)
        io.output(23, 1)
        time.sleep(.5)

        io.output(22, 0)
        time.sleep(.1)
        io.output(22, 1)
        time.sleep(.5)

        io.output(23, 0)
        time.sleep(.1)
        io.output(23, 1)
        time.sleep(.5)

        io.output(24, 0)
        time.sleep(.1)
        io.output(24, 1)
        time.sleep(.5)

        io.output(27, 0)
        time.sleep(.1)
        io.output(27, 1)
        time.sleep(.5)

        io.output(27, 0)
        time.sleep(.1)
        io.output(27, 1)
        time.sleep(.5)

##### LOCK #####

    if key == 'l':

        io.output(24, 0)
        time.sleep(.1)
        io.output(24, 1)

##### EXIT #####

    if key == 'x':
        exit()
    if key == 'exit':
        exit()
