import os
import glob
import re
import shutil
import math

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
    time_m2 = time_dn + "_" +  str(int(time_hn[0:2]) + 12) + time_hn[2:4] + time_hn[4:6]

    #print(time_m + ", " + time_m2)

    for img in img_files:

        if (time_m == os.path.basename(img)[0:-4]) or (time_m2 == os.path.basename(img)[0:-4]):

            #print(os.path.basename(img)[0:-4])

            ca_x, ca_y, ca_z = map(float, camera.split(", "))
            ma_x, ma_y, ma_z = map(float, marker.split(", "))

            fix_x = ca_x - ma_x
            fix_y = ca_y - ma_y
            fix_z = ca_z - ma_z

            distance = math.sqrt(fix_x ** 2 + fix_z ** 2)

            destination = "./merged_img/"+ os.path.basename(img)[0:-4] + "_" + str(round(distance, 2)) + ".png"
            shutil.copyfile(img, destination)


