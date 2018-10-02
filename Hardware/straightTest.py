#!/usr/bin/env python3
# so that script can be run from Brickman

from ev3dev.ev3 import *
from time import sleep

gy = GyroSensor('in1')
motorR = Motor('outC')
motorL = Motor('outB')
a = InfraredSensor('in4')
k = gy.value()
while(True):
    if gy.value() < k:
        motorR.run_direct(duty_cycle_sp=28)
        motorL.run_direct(duty_cycle_sp=32)
    if gy.value() > k:
        motorR.run_direct(duty_cycle_sp=32)
        motorL.run_direct(duty_cycle_sp=28)
    if gy.value() == k:
        motorR.run_direct(duty_cycle_sp=30)
        motorL.run_direct(duty_cycle_sp=30)
    if a.value() < 20:
        motorR.stop()
        motorL.stop()
        break


