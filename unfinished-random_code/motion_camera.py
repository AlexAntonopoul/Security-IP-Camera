#!/usr/bin/env python

''' Useful Libraries '''
from gpiozero import MotionSensor
from picamera import PiCamera
from datetime import datetime

# Time library
import time

# Setup sensors.
# Setup camera module.
camera = PiCamera()
# Motion sensor's output is connected at GPIO4 pin of Raspberry.
pir = MotionSensor(4)

#Wait 5 second for sensors to be stabillized.
time.sleep(5)  

while True:

    #Chech for movement every second.
    time.sleep(1)
    
    pir.wait_for_motion()
    print 'fsdfs'
    camera.start_preview()
    filename = datetime.now().strftime("%Y-%m-%d_%H.%M.%S.h264")
    camera.start_recording(filename)

    pir.wait_for_no_motion()
    camera.stop_preview()
    camera.stop_recording()
