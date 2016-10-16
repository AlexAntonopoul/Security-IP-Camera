from picamera import PiCamera
from datetime import datetime
import RPi.GPIO as GPIO
import time

camera = PiCamera()
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)
GPIO.setup(27, GPIO.IN)
GPIO.setup(22, GPIO.IN)

while True:
    if (GPIO.input(27)==GPIO.HIGH):
        print("Sound detected!")
    else:
        print("NO sound detectedNO sound detectedNO sound detectedNO sound detected")
    time.sleep(0.1)
