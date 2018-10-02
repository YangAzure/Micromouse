#!/usr/bin/env python3
import time
from ev3dev.ev3 import *
ir = InfraredSensor('in4')
#ut = ev3.UltrasonicSensor()
left = UltrasonicSensor('in2')
right = UltrasonicSensor('in3') 
#touch = ev3.TouchSensor()
motorR = Motor('outC')
motorL = Motor('outB')
#Mmotor = ev3.MediumMotor('outA')
#color = ev3.ColorSensor()
def turn_right():
    motorL.run_timed(time_sp=1585, speed_sp=100)
    motorR.run_timed(time_sp=1585, speed_sp=-100)
    time.sleep(3)
    #motorL.run_timed(time_sp=50, speed_sp=300)
    #motorR.run_timed(time_sp=50, speed_sp=300)

def turn_left():
    motorL.run_timed(time_sp=1585, speed_sp=-100)
    motorR.run_timed(time_sp=1585, speed_sp=100)
    time.sleep(3)
    #motorL.run_timed(time_sp=50, speed_sp=300)
    #motorR.run_timed(time_sp=50, speed_sp=300)

def go_straight():
    motorL.run_forever(speed_sp=200) 
    motorR.run_forever(speed_sp=200)
#    time.sleep(0.1)
def adjust_left():
    motorL.run_forever(speed_sp=175)
    motorR.run_forever(speed_sp=225)
    #motorL.run_forever(speed_sp=300)
    #motorR.run_forever(speed_sp=300)
def adjust_right():
    motorL.run_forever(speed_sp=225)
    motorR.run_forever(speed_sp=175)
    #motorL.run_forever(speed_sp=300)
    #motorR.run_forever(speed_sp=300)

lold = left.value()
rold = right.value() 
go_straight()
while True:
    a = ir.value()
    l = left.value()
    r = right.value()
    #a = ut.distance_centimeters()
    if a > 26:
        if l < 59 and r > 65 and l + r > 120:
            if l < lold:
                motorR.stop()
                motorL.stop()
                adjust_right()
                time.sleep(0.2)
                go_straight()
            lold = l
        elif r < 60 and l > 65 and l + r > 120:
            if r < rold:
                motorL.stop()
                motorR.stop()
                adjust_left()
                time.sleep(0.2)
                go_straight()
            rold = r
        else:
            #motorL.stop()
            #motorR.stop()
            go_straight()
        time.sleep(0.4)
    else:
        if a > 8:
            if r > 200:
                motorL.stop()
                motorR.stop()
                turn_right()
                go_straight()
            else:
                motorL.stop()
                motorR.stop()
                turn_left()
                go_straight()
        else:
            motorL.stop()
            motorR.stop()
            break
# ev3.Sound.speak('Touch sensor pressed, I quit now!').wait()
