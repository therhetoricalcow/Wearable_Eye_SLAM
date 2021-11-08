from Camera import  Camera
from Sensor import Sensor

### FilePaths
mainPath = "/home/pi/Desktop/SLAM_Recordings"
cameraPath =  mainPath + "Camera/"
cam1 = cameraPath + "camera1.avi"
cam2 = cameraPath + "camera2.avi"
cam3 = cameraPath + "camera3.avi"
sensorPath = mainPath + "Sensor/"

cam = Camera()
cam.assignVideoCaps(cam1,cam2,cam3)
sens = Sensor(sensorPath)
sens.start()
cam.start()
k  = input("Press p to Stop")
if (k == "p"):
    cam.stop()
    sens.stop()
