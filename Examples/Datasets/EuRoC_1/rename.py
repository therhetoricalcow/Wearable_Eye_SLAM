import os

path = 'MH01/mav0/cam0/data/'
img_files = os.listdir(path)
timestamps = open('timestamps.txt', 'r').read().split('\n')

# sort images according to creation time
img_files.sort(key=lambda x: os.stat(path + x).st_birthtime)

img_files.remove('.DS_Store')

for i, f in enumerate(img_files):
    #os.rename(path + f, path + '{:04d}.png'.format(i))
    os.rename(path + f, path + timestamps[i] + '.png')
    pass
