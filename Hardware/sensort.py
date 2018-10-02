#!/usr/bin/env python3
import time
from ev3dev.ev3 import *
ir = InfraredSensor()
left = UltrasonicSensor('in2')
right = UltrasonicSensor('in3')
#left.mode = 'US-DIST-CM'
#right.mode = 'US-DIST-CM'
while True:
	print(str(left.value())+' '+str(right.value()))
	#print(ir.value())
	time.sleep(0.3)
