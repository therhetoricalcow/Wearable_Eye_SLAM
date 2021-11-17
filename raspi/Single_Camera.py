from Sensor import Sensor
from pynput import keyboard
import cv2

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
sensorPath = mainPath + "Sensor/"
src1 = -1
stream1 = cv2.VideoCapture(src1)
while stream1 is None or not stream1.isOpened():
    src1 = src1 + 1
    stream1 = cv2.VideoCapture(src1)

stream1.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))
(grabbed1, frame1) = stream1.read()
while (grabbed1==False):
    (grabbed1, frame1) = stream1.read()

videocap1 = cv2.VideoWriter(cam1, cv2.VideoWriter_fourcc(*'XVID'), 10,
                                 (frame1.shape[1], frame1.shape[0]))
sens = Sensor()
print("press up to start")
while start == False:
    pass
sens.assignPath(sensorPath)
sens.start()
print("press down to stop")
while stop == False:
        (grabbed1, frame1) = stream1.read()
        while (grabbed1 == False):
            (grabbed1, frame1) = stream1.read()

        videocap1.write(frame1)

videocap1.release()
sens.stop()
