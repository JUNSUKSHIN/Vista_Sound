import os
import glob

img_path = "./image"
vid_path = "./video"
img_files = glob.glob(img_path + '/*')
vid_file = glob.glob(vid_path + '/*')

for f in img_files:
    for j in vid_file:
        hh = "00"
        if int(int(os.path.basename(j)[9:11]) + int(int(os.path.basename(f)[3:7])/3600)) < 10:
            hh = "0" + str(int(os.path.basename(j)[9:11]) + int(int(os.path.basename(f)[3:7])/3600))
        else:
            hh = str(int(os.path.basename(j)[9:11]) + int(int(os.path.basename(f)[3:7])/3600))

        mm = "00"
        if int(int(os.path.basename(j)[11:13]) + int(int(os.path.basename(f)[3:7])/60)) < 10:
            mm = "0" + str(int(os.path.basename(j)[11:13]) + int(int(os.path.basename(f)[3:7])/60))
        else:
            mm = str(int(os.path.basename(j)[11:13]) + int(int(os.path.basename(f)[3:7])/60))
        ss = "00"

        if int(int(os.path.basename(j)[13:15]) + int(os.path.basename(f)[3:7]) - 1) < 10:
            ss = "0" + str(int(os.path.basename(j)[13:15]) + int(os.path.basename(f)[3:7]) - 1)
        else:
            ss = str(int(os.path.basename(j)[13:15]) + (int(os.path.basename(f)[3:7]) % 60) - 1)

        os.rename(f, os.path.join(img_path,os.path.basename(j)[0:8] + "_" + hh + mm + ss +".png"))