import cv2
import numpy
import os
from pynput import keyboard

numPoints = 40
vidFold = "/home/eyeRecord/"
os.mkdir(vidFold)
print("Video Folder at: " + vidFold)

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
        stop = False
    if key == keyboard.Key.down:
        stop = True
        start = False

listener = keyboard.Listener(on_press=on_press)
listener.start()


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

while (grabbed1==False or grabbed2== False):
    (grabbed1, frame1) = stream1.read()
    (grabbed2, frame2) = stream2.read()

print("Cameras Working")

for j in range(numPoints + 1):
    recFolder = vidFold + str(j) + "/"
    os.mkdir(recFolder)
    print("Created: " + recFolder)
    cam1 = recFolder + "cam1.avi"
    cam2 = recFolder + "cam2.avi"
    videocap1 = cv2.VideoWriter(cam1, cv2.VideoWriter_fourcc(*'XVID'), 30,
                                (frame1.shape[1], frame1.shape[0]))
    videocap2 = cv2.VideoWriter(cam2, cv2.VideoWriter_fourcc(*'XVID'), 30,
                                (frame1.shape[1], frame1.shape[0]))
    print("Press UP to start Recording")
    while(start == False):
        pass

    print("Starting to Record, Press DOWN to Stop")

    while(stop == False):
        (grabbed1, frame1) = stream1.read()
        (grabbed2, frame2) = stream2.read()

        while (grabbed1 == False or grabbed2 == False):
            (grabbed1, frame1) = stream1.read()
            (grabbed2, frame2) = stream2.read()

        videocap1.imwrite(frame1)
        videocap2.imwrite(frame2)

    videocap1.release()
    videocap2.release()

