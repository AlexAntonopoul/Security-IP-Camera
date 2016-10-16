from gpiozero import MotionSensor
from picamera import PiCamera
import time

camera = PiCamera()
pir = MotionSensor(4)

while True:
    time.sleep(1)
    if pir.motion_detected:
        print("Motion detected!")
    else:
        print("NO Motion detected")
