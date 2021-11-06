import serial
import pickle
import numpy as np
import board
import busio
import adafruit_bno055
import os
##from gps import *
import time
from threading import Thread


class sensorData:
    def __init__(self,path):
        i2c = busio.I2C(board.SCL, board.SDA)
        self.sensor = adafruit_bno055.BNO055_I2C(i2c)
        self.updateThread = None
        self.totalData = None
        self.path = path
        self.timestamp = 0
        self.j = 1


    def start(self):
        self.stopped = False
        self.updateThread = Thread(target=self.update, args=())
        self.start_ = time.time()
        self.updateThread.start()
        return self

    def update(self):
        while(self.stopped == False):
            a1,a2,a3 = self.sensor.acceleration
            g1,g2,g3 = self.sensor.gyro
            self.timestamp = time.time() - self.start_
            data = np.array([self.timestamp,a1,a2,a3,g1,g2,g3])

            if self.totalData is None:
                self.totalData = data
            elif self.totalData.shape[0] == 1000:
                self.write()
                self.totalData = data
            else:
                self.totalData = np.vstack((self.totalData,data))

    def write(self):
       recPath = self.path + str(self.j) + ".csv"
       print("Saved csv {0:2d} at Ending Timestamp:{1}".format(self.j,self.timestamp))
       np.savetxt(recPath, self.totalData, delimiter=",")
       self.j = self.j + 1

    def stop(self):
        self.write()
        self.stopped = True
        self.updateThread.join()
