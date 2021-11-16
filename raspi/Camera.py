from threading import Thread
import cv2
import numpy as np
import PIL
import time


class Camera:
    def __init__(self):
        src1 = -1
        self.stream1 = cv2.VideoCapture(src1)
        while self.stream1 is None or not self.stream1.isOpened():
            src1 = src1 + 1
            self.stream1 = cv2.VideoCapture(src1)
        src2 = src1 + 1
        self.stream2 = cv2.VideoCapture(src2)
        while self.stream2 is None or not self.stream2.isOpened():
            src2 = src2 + 1
            self.stream2 = cv2.VideoCapture(src2)
        src3 = src2 + 1
        self.stream3 = cv2.VideoCapture(src3)
        while self.stream3 is None or not self.stream3.isOpened():
            src3 = src3 + 1
            self.stream3 = cv2.VideoCapture(src3)

        self.stream1.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))
        self.stream2.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))
        self.stream3.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))

        (self.grabbed1, self.frame1) = self.stream1.read()
        (self.grabbed2, self.frame2) = self.stream2.read()
        (self.grabbed3, self.frame3) = self.stream3.read()

        self.videocap1 = None
        self.videocap2 = None
        self.videocap3 = None

        self.stopped = False
        self.updateThread = None
        self.start_ = 0
        self.toWrite = False
        while (self.grabbed1 == False or self.grabbed2 == False or self.grabbed3 == False):
            (self.grabbed1, self.frame1) = self.stream1.read()
            (self.grabbed2, self.frame2) = self.stream2.read()
            (self.grabbed3, self.frame3) = self.stream3.read()


    def read(self):
        return self.frame1, self.frame2, self.frame3

    def assignVideoCaps(self, src1, src2, src3):
        print(self.frame1.shape)
        self.toWrite = True
        self.videocap1 = cv2.VideoWriter(src1, cv2.VideoWriter_fourcc(*'XVID'), 10,
                                         (self.frame1.shape[1], self.frame1.shape[0]))
        self.videocap2 = cv2.VideoWriter(src2, cv2.VideoWriter_fourcc(*'XVID'), 10,
                                         (self.frame2.shape[1], self.frame2.shape[0]))
        self.videocap3 = cv2.VideoWriter(src3, cv2.VideoWriter_fourcc(*'XVID'), 10,
                                         (self.frame3.shape[1], self.frame3.shape[0]))

    def start(self):
        self.stopped = False
        self.updateThread1 = Thread(target=self.update, args=(1))
        self.updateThread2 = Thread(target=self.update, args=(2))
        self.updateThread3 = Thread(target=self.update, args=(3))

        self.start_ = time.time()
        self.j = 1
        self.updateThread1.start()
        self.updateThread1.start()
        self.updateThread3.start()
        return self

    def update(self,num):

        while (self.stopped == False):
            if num == 1:
                (self.grabbed1, self.frame1) = self.stream1.read()
                while(self.grabbed1==False):
                    (self.grabbed1, self.frame1) = self.stream1.read()
                if self.toWrite:
                    self.write(num)
            if num == 2:
                (self.grabbed2, self.frame2) = self.stream2.read()
                while(self.grabbed2==False):
                    (self.grabbed2, self.frame2) = self.stream2.read()
                if self.toWrite:
                    self.write(num)
            if num == 3:
               (self.grabbed3, self.frame3) = self.stream3.read()
               while (self.grabbed3 == False):
                   (self.grabbed3, self.frame3) = self.stream3.read()
               if self.toWrite:
                   self.write(num)



    def write(self,num):
        print(self.j / (time.time() - self.start_))
        if num == 1:
            self.videocap1.write(self.frame1)
        if num == 2:
            self.videocap2.write(self.frame2)
        if num == 3:
            self.videocap3.write(self.frame3)
        self.j = self.j + 1

    def stop(self):
        self.videocap1.release()
        self.videocap2.release()
        self.videocap3.release()
        self.stopped = True
        self.updateThread1.join()
        self.updateThread2.join()
        self.updateThread3.join()

