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
    if key == keyboard.Key.down:
        stop = True


### FilePaths
mainPath = "/home/pi/Desktop/SLAM_Recordings"
cameraPath =  mainPath + "Camera/"
cam1 = cameraPath + "camera1.avi"
cam2 = cameraPath + "camera2.avi"
cam3 = cameraPath + "camera3.avi"
sensorPath = mainPath + "Sensor/"

cam = Camera()
cam.assignVideoCaps(cam1,cam2,cam3)
cam.start()
while start == False:
    pass
sens = Sensor()
sens.assignPath(sensorPath)
sens.start()
while stop == False:
    cam.write()


cam.stop()
sens.stop()
