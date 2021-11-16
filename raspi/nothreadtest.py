import cv2
import numpy as np

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
src3 = src2 + 1
stream3 = cv2.VideoCapture(src3)
while stream3 is None or not stream3.isOpened():
    src3 = src3 + 1
    stream3 = cv2.VideoCapture(src3)

stream1.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))
stream2.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))
stream3.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))


#
# videocap1 = cv2.VideoWriter(src1, cv2.VideoWriter_fourcc(*'XVID'), 10,
#                                          (self.frame1.shape[1], self.frame1.shape[0]))
# videocap2 = cv2.VideoWriter(src2, cv2.VideoWriter_fourcc(*'XVID'), 10,
#                                          (self.frame1.shape[1], self.frame1.shape[0]))
# videocap3 = cv2.VideoWriter(src3, cv2.VideoWriter_fourcc(*'XVID'), 10,
#                                          (self.frame1.shape[1], self.frame1.shape[0]))

stopped = False
updateThread = None
start_ = 0
toWrite = False

while stopped == False:
    (grabbed1, frame1) = stream1.read()
    (grabbed2, frame2) = stream2.read()
    (grabbed3, frame3) = stream3.read()
    while (grabbed1 == False or grabbed2 == False or grabbed3 == False):
        (grabbed1, frame1) = stream1.read()
        (grabbed2, frame2) = stream2.read()
        (grabbed3, frame3) = stream3.read()

    cv2.imshow("Frame1", frame1)
    cv2.imshow("Frame2", frame2)
    cv2.imshow("Frame3", frame3)
    cv2.waitKey(1)

