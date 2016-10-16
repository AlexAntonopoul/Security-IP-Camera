#!/usr/bin/env python
# -*- coding: utf-8 -*-

''' Useful Libraries '''
from picamera import PiCamera
from datetime import datetime
import RPi.GPIO as GPIO
import time

# ~~~~ Setup sensors ~~~~

# Setup camera module.
camera = PiCamera()

# Setup motion sensor. 
GPIO.setmode(GPIO.BCM)
PIR_PIN = 4   # Motion sensor's output is connected at GPIO4 pin of Raspberry.
GPIO.setup(PIR_PIN, GPIO.IN)

# Variable to know how many videos we recorded (for log files maybe).
recvid = 0

timeToRec = 10  # The 10 here stands for 10 seconds (of recording)

'''
    timeout variable will be the flag to stop recording.
    It holds the current time + the seconds that we would
    like to record video.
'''
timeout = time.time()
    
# Variable to let us know if we record something.
rec = 0

#Wait 5 second for sensors to be stabillized.
time.sleep(5)
print 'Everything is ready\n'

# Main loop
while True:

    if GPIO.input(PIR_PIN):

        '''
            If we just start the program or even if we already recording if
            motion sensor detect movement set the timeout timemake the timeout
            time the curent time + timeToRec
        '''
        timeout = time.time()+timeToRec  

        '''
            Start recording and save what you recorded to a file
            named after the date and time that it created.
        '''
        if(rec == 0):
            # Set the record flag to 1
            rec = 1
            #camera.start_preview()
            filename = datetime.now().strftime("%Y-%m-%d_%H.%M.%S.h264")
            camera.start_recording(filename)
            print'Start recording\n~~~~~~~~~~~~~~~'
    
    if (rec == 1 and time.time() > timeout):
        recvid += 1
        #camera.stop_preview()
        camera.stop_recording()
        rec = 0
        print 'Stop recording', recvid
        print '~~~~~~~~~~~~~~~~\n'
        
    #Check for movement every second.
    time.sleep(1)
