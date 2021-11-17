import numpy as np
import cv2
import os
import time
### FilePaths
mainPath = "/home/pi/Desktop/SLAM_Recordings"
cameraPath =  mainPath + "Camera/"
cam2 = cameraPath + "camera2.avi"
cam3 = cameraPath + "camera3.avi"

sensorPath = mainPath + "Sensor/"
files = os.listdir(sensorPath)
sorted = files.sort()
arr = np.loadtxt(sensorPath + str(sorted[-1]))
tot_time = arr[-1,0]
print("Total Time to record")
src1 = -1
stream1 = cv2.VideoCapture(src1)
while stream1 is None or not stream1.isOpened():
    src1 = src1 + 1
    stream1 = cv2.VideoCapture(src1)
src2 = src1 + 1
stream2 = cv2.VideoCapture(src2)
while stream2 is None or not stream2.isOpened():
    src2 = src2 + 1
    stream2 = cv2.VideoCapture(src2)

stream1.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))
stream2.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))

(grabbed1, frame1) = stream1.read()
(grabbed2, frame2) = stream2.read()
while (grabbed1==False or grabbed2==False):
    (grabbed1, frame1) = stream1.read()
    (grabbed2, frame2) = stream2.read()


videocap1 = cv2.VideoWriter(cam2, cv2.VideoWriter_fourcc(*'XVID'), 10,
                                 (frame1.shape[1], frame1.shape[0]))
videocap2 = cv2.VideoWriter(cam3, cv2.VideoWriter_fourcc(*'XVID'), 10,
                                 (frame1.shape[1], frame1.shape[0]))

start_ = time.time()
while time.time() - start_ < tot_time:
    (grabbed1, frame1) = stream1.read()
    (grabbed2, frame2) = stream2.read()
    while (grabbed1 == False or grabbed2 == False):
        (grabbed1, frame1) = stream1.read()
        (grabbed2, frame2) = stream2.read()

    videocap1.write(frame1)
    videocap2.write(frame2)


videocap1.release()
videocap2.release()