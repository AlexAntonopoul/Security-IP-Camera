from picamera import PiCamera
import time

camera = PiCamera()

camera.resolution=(1280,720)
camera.rotation=180
camera.framerate=60
camera.start_recording('video2.h264')
time.sleep(60)
camera.stop_recording()
