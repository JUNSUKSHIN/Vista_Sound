import os
import glob

img_path = "./image"
vid_path = "./video"
files = glob.glob(img_path + '/*')

for f in files:
    os.rename(f, os.path.join(path, 'img_' + os.path.basename(f)))