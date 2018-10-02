#!/usr/bin/env python3
import time
import math
from ev3dev.ev3 import *
ir = InfraredSensor('in4')
left = UltrasonicSensor('in2')
right = UltrasonicSensor('in3')
motorR = Motor('outC')
motorL = Motor('outB')
gy = GyroSensor('in1')
orilist = ['left','up','right','down']
ori = 0
movelog = open('mlog.txt','w')
#sensorlog = open('slog.txt','w')
visited = [[0 for i in range(8)] for j in range(8)]
xaxis = 7
yaxis = 7
#visited[xaxis][yaxis] = 1
def calcgrid(inputnum):
    if inputnum > 6:
        return(5)
    elif inputnum < 1.7:
        return(1)
    else:
        return(math.floor((inputnum-0.2)/1.2))

def gyreset():
    gy.mode = 'GYRO-RATE'
    gy.mode = 'GYRO-G&A'
    while(True):
        ang,rt = gy.rate_and_angle
        if(ang == 0 and rt == 0):
            break
    direc = gy.value()
    return(direc)

direc = gyreset()
backturnp = 0
movelist = []

def direchange(lold, rold, direc):
    l = left.value()
    r = right.value()
    #if l - lold > 0 and r - rold < 0 and l + r > 140 and l + r < 180:
    if (l < 75 and l + r > 130 and l <= lold + 1) or (l > 2400):
        direc = direc - 0.2
        lold = l
        rold = r
    #if l - lold < 0 and r - rold > 0 and l + r > 140 and l + r < 180:
    if (r < 75 and l + r > 130 and r <= rold + 1) or (r > 2400):
        direc = direc + 0.2
        lold = l
        rold = r
    return lold, rold, direc
def adjust_stable(direc):
    while(True):
        ang,rt = gy.rate_and_angle
        #print(str(r) + ' ' + str(a) + ' ' + str(direc))
        if gy.value() > direc + 1:
            if rt == 0:
                motorR.run_direct(duty_cycle_sp=-25)
                motorL.run_direct(duty_cycle_sp=25)
            else:
                motorR.run_direct(duty_cycle_sp=-15)
                motorL.run_direct(duty_cycle_sp=15)
        elif gy.value() < direc - 1:
            if rt == 0:
                motorR.run_direct(duty_cycle_sp=25)
                motorL.run_direct(duty_cycle_sp=-25)
            else:
                motorR.run_direct(duty_cycle_sp=15)
                motorL.run_direct(duty_cycle_sp=-15)
        elif gy.value() >= direc - 1.6 and gy.value() <= direc + 1.6:
            time.sleep(0.1)
            if rt <= 15 and rt >= -15:
                motorR.stop()
                motorL.stop()
                break
            continue
            #else:
                #pass
        #time.sleep(0.1)

def turn_right(direc,ori):
    direc = direc - 88
    ori = ori + 1
    motorL.run_direct(duty_cycle_sp=30)
    motorR.run_direct(duty_cycle_sp=-30)
    while(True):
        ang,rt = gy.rate_and_angle
        if gy.value() <= direc + 15 and gy.value() > direc:
            motorL.run_direct(duty_cycle_sp=20)
            motorR.run_direct(duty_cycle_sp=-20)
        if gy.value() <= direc:
            #motorR.stop()
            #motorL.stop()
            break
        if ang > direc and rt == 0:
            motorL.run_direct(duty_cycle_sp=25)
            motorR.run_direct(duty_cycle_sp=-25)
    adjust_stable(direc)

    #motorL.run_timed(time_sp=50, speed_sp=300)
    #motorR.run_timed(time_sp=50, speed_sp=300)
    return(direc,ori)

def turn_left(direc,ori):
    ori = ori - 1
    direc = direc + 88.15
    motorL.run_direct(duty_cycle_sp=-30)
    motorR.run_direct(duty_cycle_sp=30)
    while(True):
        ang,rt = gy.rate_and_angle
        if gy.value() >= direc - 15 and gy.value() < direc:
            motorL.run_direct(duty_cycle_sp=-20)
            motorR.run_direct(duty_cycle_sp=20)
        if ang < direc and rt == 0:
            motorL.run_direct(duty_cycle_sp=-25)
            motorR.run_direct(duty_cycle_sp=25) 
        if gy.value() >= direc:
            #motorR.stop()
            #motorL.stop()
            break
    adjust_stable(direc)
    #motorL.run_timed(time_sp=50, speed_sp=300)
    #motorR.run_timed(time_sp=50, speed_sp=300)
    return(direc,ori)
def turn_back(direc, backturnp , ori):
    ori = ori + 2
    if backturnp % 2:
        direc = direc + 177.4
        motorL.run_direct(duty_cycle_sp=-30)
        motorR.run_direct(duty_cycle_sp=30)
        while(True):
            ang,rt = gy.rate_and_angle
            if gy.value() >= direc - 15 and gy.value() < direc:
                motorL.run_direct(duty_cycle_sp=-20)
                motorR.run_direct(duty_cycle_sp=20)
            if ang < direc and rt == 0:
                motorL.run_direct(duty_cycle_sp=-25)
                motorR.run_direct(duty_cycle_sp=25)
            if gy.value() >= direc:
                motorR.stop()
                motorL.stop()
                break
        adjust_stable(direc)
        #motorL.run_timed(time_sp=50, speed_sp=300)
        #motorR.run_timed(time_sp=50, speed_sp=300)
    else:
        direc = direc - 177.4
        motorL.run_direct(duty_cycle_sp=30)
        motorR.run_direct(duty_cycle_sp=-30)
        while(True):
            ang,rt = gy.rate_and_angle
            if gy.value() <= direc + 15 and gy.value() > direc:
                motorL.run_direct(duty_cycle_sp=20)
                motorR.run_direct(duty_cycle_sp=-20)
            if ang > direc and rt == 0:
                motorL.run_direct(duty_cycle_sp=25)
                motorR.run_direct(duty_cycle_sp=-25)
            if gy.value() <= direc:
                motorR.stop()
                motorL.stop()
                break
        adjust_stable(direc)
        #motorL.run_timed(time_sp=50, speed_sp=300)
        #motorR.run_timed(time_sp=50, speed_sp=300)
    backturnp = backturnp + 1
    if backturnp % 2 == 0:
        time.sleep(2.8)
        direc = gyreset()
    return(direc, backturnp, ori)

def go_straight(direc,xaxis,yaxis):
    startT = time.time()
    refT = startT
    lold = left.value()
    rold = right.value()
    #blocks = 0
    while(True):
        #print(direc)
        #if l <= 50 and r >= 75 and l + r < 140 and l + r > 120:
            #direc = direc + 1
        #if r <= 50 and l >= 75 and l + r < 140 and l + r > 120:
            #direc = direc - 1
        if gy.value() > direc:
            motorR.run_direct(duty_cycle_sp=66)
            motorL.run_direct(duty_cycle_sp=74)
        if gy.value() < direc:
            motorR.run_direct(duty_cycle_sp=74)
            motorL.run_direct(duty_cycle_sp=66)
        if gy.value() == direc:
            motorR.run_direct(duty_cycle_sp=70)
            motorL.run_direct(duty_cycle_sp=70)
        if ((time.time() - startT < 2) and ((time.time() - refT) - 0.15) > 1.1) or ((time.time() - startT >= 2) and time.time() - refT >= 1.4):
            refT = time.time()
            #blocks = blocks + 1
            if ori % 4 == 0:
                xaxis = xaxis - 1
                visited[yaxis][xaxis] = 1
            if ori % 4 == 1:
                yaxis = yaxis - 1
                visited[yaxis][xaxis] = 1
            if ori % 4 == 2:
                xaxis = xaxis + 1
                visited[yaxis][xaxis] = 1
            if ori % 4 == 3:
                yaxis = yaxis + 1
                visited[yaxis][xaxis] = 1
        lold, rold, direc = direchange(lold, rold, direc)
        if right.value() > 180 and right.value() < 1650 and time.time()- startT > 1.3:
            time.sleep(0.1)
            movelist.append([orilist[ori % 4],time.time()-startT, calcgrid(time.time()- startT),xaxis,yaxis,visited])     
            motorR.stop()
            motorL.stop()
            movelog.write('%s\n' % movelist[len(movelist)-1])
            #movelog.write('%d\n' % xaxis)
            #movelog.write('%d\n' % yaxis)
            #sensorlog.write('%d ' % right.value())
            #sensorlog.write('%d ' % left.value())
            #sensorlog.write('%d ' % ir.value())
            #sensorlog.write('%d\n' % gy.value())
            return(direc,xaxis,yaxis)
        if ir.value() <= 30:
            #print('went to '+str(direc)+'for '+str(time.time()- startT)+'seconds')
            movelist.append([orilist[ori % 4],time.time()-startT, calcgrid(time.time()- startT),xaxis,yaxis,visited])
            motorR.stop()
            motorL.stop()
            movelog.write('%s\n' % movelist[len(movelist)-1])
            #movelog.write('%d\n' % xaxis)
            #movelog.write('%d\n' % yaxis)
            #sensorlog.write('%d ' % right.value())
            #sensorlog.write('%d ' % left.value())
            #sensorlog.write('%d ' % ir.value())
            #sensorlog.write('%d\n' % gy.value())
            return(direc,xaxis,yaxis)

while True:
    if visited[7][7] == 1:
        motorL.stop()
        motorR.stop()
        break
    a = ir.value()
    l = left.value()
    r = right.value()
    if r > 180 and r < 1650:
        if right.value() > 180 and right.value() < 1650:
            direc,ori = turn_right(direc,ori)
            direc,xaxis,yaxis = go_straight(direc,xaxis,yaxis)
        else:
            continue
    else:
        if a > 0.1:
            if a > 30:
                direc,xaxis,yaxis = go_straight(direc,xaxis,yaxis)
            elif right.value() > 180 and right.value() < 1650:
                if right.value() > 180 and right.value() < 1650:
                    direc,ori = turn_right(direc,ori)
                    direc,xaxis,yaxis = go_straight(direc,xaxis,yaxis)
                else:
                    continue
            elif l > 180 and l < 1650:
                if left.value() > 180 and left.value() < 1650:
                    direc,ori = turn_left(direc,ori)
                    direc,xaxis,yaxis = go_straight(direc,xaxis,yaxis)
                else: 
                    continue
            else:
                direc, backturnp, ori = turn_back(direc, backturnp, ori)
                direc,xaxis,yaxis = go_straight(direc,xaxis,yaxis)
    
    #if visited[7][0] == 1:
        #motorL.stop()
        #motorR.stop()
        #break


