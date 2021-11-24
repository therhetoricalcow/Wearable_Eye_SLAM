'''
Workflow:
  1. Extract frames from video
     a. Get FPS: `ffmpeg -i <video_name>`
     b. Run `ffmpeg -i video_name -r <FPS>/1 ./MH01/mav0/cam0/%d.png
  2. Get timestamps
     a. Run this file
  3. Rename images according to timestamps
     a. Run rename.py
  4. Update camera calibration at Examples/Monocular/EuRoC_1.yaml
'''

import numpy as np
import os

# get file content, IMU data already downsampled -- just need to extract first column
data = np.genfromtxt('./MH01/mav0/imu0/data.csv', delimiter=',')
timestamps = data[:,0]

# get # of images
image_files = os.listdir('./MH01/mav0/cam0/data')
num_images = len(image_files) - 1 # exclude .DS_Store

if num_images < len(timestamps):
    timestamps = timestamps[:num_images]

np.savetxt("timestamps.txt", timestamps)
