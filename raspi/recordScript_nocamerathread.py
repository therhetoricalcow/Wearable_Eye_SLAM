import cv2
import numpy as np
from Camera import  Camera
from Sensor import Sensor
from pynput import keyboard

start = False
stop = False
def on_press(key):
    global i
    global start
    global stop
    if key == keyboard.Key.esc:
            return False
    if key == keyboard.Key.up:
        start = True
        print("PRESSED UP")
    if key == keyboard.Key.down:
        stop = True
        print("PRESSED DOWN")

listener = keyboard.Listener(on_press=on_press)
listener.start()
### FilePaths
mainPath = "/home/pi/Desktop/SLAM_Recordings"
cameraPath =  mainPath + "Camera/"
cam1 = cameraPath + "camera1.avi"
cam2 = cameraPath + "camera2.avi"
cam3 = cameraPath + "camera3.avi"
sensorPath = mainPath + "Sensor/"
cam = Camera()
stream1,stream2,stream3 = cam.getStreams()
cam.assignVideoCaps(cam1,cam2,cam3)
print("press up to start")
while start == False:
    pass
sens = Sensor()
sens.assignPath(sensorPath)
sens.start()
print("press down to stop")
while stop == False:
        (grabbed1, frame1) = stream1.read()
        (grabbed2, frame2) = stream2.read()
        (grabbed3, frame3) = stream3.read()
        while (grabbed1 == False or grabbed2 == False or grabbed3 == False):
            (grabbed1, frame1) = stream1.read()
            (grabbed2, frame2) = stream2.read()
            (grabbed3, frame3) = stream3.read()

        cam.writeFrames(frame1,frame2,frame3)

cam.videocap1.release()
cam.videocap2.release()
cam.videocap3.release()

sens.stop()
