# door
Raspberry Pi spliced into keypad door. Simulates button presses by using relays to connect the door wiring in different combinations to enter the user selected access code. Combined with adafruit fingerprint module and script so my fingerprint can unlock the door.

door.py contains lock() and unlock() functions

monitor.py creates a timestamp every time the door is opened or closed and adds each occurance to a log file
