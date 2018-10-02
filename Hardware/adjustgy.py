#!/usr/bin/env python3
# so that script can be run from Brickman

from ev3dev.ev3 import *
import time
gy = GyroSensor()

motorR = Motor('outC')
motorL = Motor('outB')

while(True):
	if gy.value() < -90:
		motorR.stop()
		motorL.stop()
		motorR.run_forever(speed_sp=-100)
		motorL.run_forever(speed_sp=100)
	if gy.value() > -90:
		motorR.stop()
		motorL.stop()
		motorR.run_forever(speed_sp=100)
		motorL.run_forever(speed_sp=-100)
	if gy.value() == -90:
		motorR.stop()
		motorL.stop()
		break
	time.sleep(0.3)
