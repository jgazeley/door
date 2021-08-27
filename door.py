import RPi.GPIO as io
import time

io.setwarnings(False)
io.setmode(io.BCM)

io.setup(22, io.OUT) #5/6
io.setup(27, io.OUT) #1/2
io.setup(23, io.OUT) #9/0
io.setup(24, io.OUT) #LOCK
io.output(22, 1)
io.output(27, 1)
io.output(23, 1)
io.output(24, 1)

def activate(pin):
    io.output(pin, 0)
    time.sleep(.1)
    io.output(pin, 1)

def toggle(pin):
    io.output(pin, not io.input(pin))

def check(pin):
    print(io.input(pin))

def press_SIX():
    activate(22)

def press_ONE():
    activate(27)

def press_NINE():
    activate(23)

def unlock(): # UNLOCK (6-1-9-5-9-9-1-1)
    press_SIX()
    time.sleep(.5)
    press_ONE()
    time.sleep(.5)
    press_NINE()
    time.sleep(.5)
    press_SIX()
    time.sleep(.5)
    press_NINE()
    time.sleep(.5)
    press_NINE()
    time.sleep(.5)
    press_ONE()
    time.sleep(.5)
    press_ONE()

def lock():
    activate(24)
