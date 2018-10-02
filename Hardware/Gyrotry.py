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
gy = GyroSensor('in1')
gy.mode = 'GYRO-RATE'
gy.mode = 'GYRO-G&A'
while(True):
    a,r = gy.rate_and_angle
    if(a == 0 and r == 0):
        break
direc = gy.value()
backturnp = 0


def adjust_stable(direc):
    while(True):
        a,r = gy.rate_and_angle
        print(str(r) + ' ' + str(a) + ' ' + str(direc))
        if gy.value() > direc + 1:
            motorR.run_direct(duty_cycle_sp=-15)
            motorL.run_direct(duty_cycle_sp=15)
        elif gy.value() < direc - 1:
            motorR.run_direct(duty_cycle_sp=15)
            motorL.run_direct(duty_cycle_sp=-15)
        elif gy.value() >= direc - 1 and gy.value() <= direc +1:
            time.sleep(0.1)
            if r <= 10 and r >= -10:
                break
            continue
            #else:
                #pass
        #time.sleep(0.1)

def turn_right(direc):
    direc = direc - 89
    motorL.run_direct(duty_cycle_sp=30)
    motorR.run_direct(duty_cycle_sp=-30)
    while(True):
        if gy.value() <= direc + 15 and gy.value() > direc:
            motorL.run_direct(duty_cycle_sp=17)
            motorR.run_direct(duty_cycle_sp=-17)
        if gy.value() <= direc:
            motorR.stop()
            motorL.stop()
            break
    adjust_stable(direc)
        
    #motorL.run_timed(time_sp=50, speed_sp=300)
    #motorR.run_timed(time_sp=50, speed_sp=300)
    return(direc)

def turn_left(direc):
    direc = direc + 89
    motorL.run_direct(duty_cycle_sp=-30)
    motorR.run_direct(duty_cycle_sp=30)
    while(True):
        if gy.value() >= direc - 15 and gy.value() < direc:
            motorL.run_direct(duty_cycle_sp=-17)
            motorR.run_direct(duty_cycle_sp=17)
        if gy.value() >= direc:
            motorR.stop()
            motorL.stop()
            break
    adjust_stable(direc)
    #motorL.run_timed(time_sp=50, speed_sp=300)
    #motorR.run_timed(time_sp=50, speed_sp=300)
    return(direc)

def turn_back(direc, backturnp):
    if backturnp % 2:
        direc = direc + 177
        motorL.run_direct(duty_cycle_sp=-30)
        motorR.run_direct(duty_cycle_sp=30)
        while(True):
            if gy.value() >= direc - 15 and gy.value() < direc:
                motorL.run_direct(duty_cycle_sp=-17)
                motorR.run_direct(duty_cycle_sp=17)
            if gy.value() >= direc:
                motorR.stop()
                motorL.stop()
                break
        adjust_stable(direc)
        #motorL.run_timed(time_sp=50, speed_sp=300)
        #motorR.run_timed(time_sp=50, speed_sp=300)
    else:
        direc = direc - 177
        motorL.run_direct(duty_cycle_sp=30)
        motorR.run_direct(duty_cycle_sp=-30)
        while(True):
            if gy.value() <= direc + 15 and gy.value() > direc:
                motorL.run_direct(duty_cycle_sp=17)
                motorR.run_direct(duty_cycle_sp=-17)
            if gy.value() <= direc:
                motorR.stop()
                motorL.stop()
                break
        adjust_stable(direc)
        #motorL.run_timed(time_sp=50, speed_sp=300)
        #motorR.run_timed(time_sp=50, speed_sp=300)
    backturnp = backturnp + 1
    return(direc, backturnp)

def go_straight(direc):
    while(True):
        print(direc)
        #if l <= 50 and r >= 75 and l + r < 140 and l + r > 120:
            #direc = direc + 1
        #if r <= 50 and l >= 75 and l + r < 140 and l + r > 120:
            #direc = direc - 1
        if gy.value() > direc:
            motorR.run_direct(duty_cycle_sp=58)
            motorL.run_direct(duty_cycle_sp=62)
        if gy.value() < direc:
            motorR.run_direct(duty_cycle_sp=62)
            motorL.run_direct(duty_cycle_sp=58)
        if gy.value() == direc:
            motorR.run_direct(duty_cycle_sp=60)
            motorL.run_direct(duty_cycle_sp=60)
        if ir.value() < 25:
            motorR.stop()
            motorL.stop()
            return(direc)
           
while True:
    a = ir.value()
    l = left.value()
    r = right.value()
    #a = ut.distance_centimeters()
    if a > 25:
        direc = go_straight(direc)
    else:
        if a > 8:
            if l > 200:
                direc = turn_left(direc)
                direc = go_straight(direc)
            elif r > 200:
                direc = turn_right(direc)
                direc = go_straight(direc)
            else:
                direc, backturnp = turn_back(direc, backturnp)
                direc = go_straight(direc)
        else:
            motorL.stop()
            motorR.stop()
            break
# ev3.Sound.speak('Touch sensor pressed, I quit now!').wait()


