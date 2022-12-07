import os
import glob
import re
import shutil

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

            ca_x, ca_y, ca_z = map(float, camera.split(", "))
            ma_x, ma_y, ma_z = map(float, marker.split(", "))
            
            fix_x = ca_x - ma_x
            fix_y = ca_y - ma_y
            fix_z = ca_z - ma_z




