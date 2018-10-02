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

motorL.run_forever(speed_sp=300)
motorR.run_forever(speed_sp=300)
time.sleep(1)

motorL.run_forever(speed_sp=20)
motorR.run_forever(speed_sp=20)
time.sleep(2)

motorL.stop()
motorR.stop()

#motorL.run_timed(time_sp=5000,speed_sp=200)
#motorR.run_timed(time_sp=5000,speed_sp=200)
#time.sleep(0.1)

