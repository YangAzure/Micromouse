#!/usr/bin/env python3
import time
from ev3dev.ev3 import *
motorR = LargeMotor('outC')
motorL = LargeMotor('outB')
def turn_right():
	motorL.run_timed(time_sp = 1580, speed_sp = 100)
	motorR.run_timed(time_sp = 1580, speed_sp = -100)
	time.sleep(2.5)
def turn_left():
        motorL.run_timed(time_sp = 1580, speed_sp = -100)
        motorR.run_timed(time_sp = 1580, speed_sp = 100)
        time.sleep(2.5)

for x in range(8):
	turn_right()


 
