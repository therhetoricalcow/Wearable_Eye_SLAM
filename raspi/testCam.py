import cv2
import numpy as np
from Camera import Camera
from Sensor import Sensor

cam = Camera()
sens = Sensor()
cam.start()
sens.start()
while(True):
	frame1,frame2,frame3 = cam.read()
	data = sens.totalData
	cv2.imshow("Frame1",frame1)
	cv2.imshow("Frame2",frame2)
	cv2.imshow("Frame3",frame3)
