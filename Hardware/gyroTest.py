#!/usr/bin/env python3
from ev3dev.ev3 import *
import time
gy=GyroSensor()
#Caliberate the gyro sensor
gy.mode = 'GYRO-RATE'
gy.mode = 'GYRO-G&A'
motorR = Motor('outC')
motorL = Motor('outB')

motorR.run_forever(speed_sp=-100)
motorL.run_forever(speed_sp=100)
while(True):
    #print(gy.value())
    r,a = gy.rate_and_angle
    print(str(r)+str(a))
    #time.sleep(5)
    #gy.mode = 'GYRO-RATE'
    #gy.mode = 'GYRO-G&A'
    #print(gy.value())
    #break
    if gy.value() <= -1080:
        motorR.stop()
        motorL.stop()
        time.sleep(0.3)
        print(True)
        print(gy.value())
        
