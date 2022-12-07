import os
import glob
import re

img_path = "./image"

img_files = glob.glob(img_path + '/*')
f= open('matrix_quotes.txt','r')

lines = f.read().splitlines()

for line in lines:
    time_t, camera, marker = line.split("/")
    time_d, time_h = time_t.split(" ")

    time_dn = re.sub(r'[^0-9]', '', time_d)
    time_hn = re.sub(r'[^0-9]', '', time_h)

    time_m = time_dn + "_" + time_hn

    for img in img_files:

        if time_m == os.path.basename(img)[0:-4]:
            



