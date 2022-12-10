import os
import glob
import shutil

img_path = "./masked_img"
img2_path = "./classified/"
img_files = glob.glob(img_path + '/*')
img2_files = glob.glob(img2_path + '/*')

for img in img_files:

    print(os.path.basename(img)[16:-4])

    distance = float(os.path.basename(img)[16:-4])

    if distance <= 0.5:
        destination = img2_path + "0.5/" + os.path.basename(img)
        shutil.copyfile(img, destination)

    if distance <= 0.75:
        destination = img2_path + "0.75/" + os.path.basename(img)
        shutil.copyfile(img, destination)

    if distance <= 1:
        destination = img2_path + "1/" + os.path.basename(img)
        shutil.copyfile(img, destination)

    if distance <= 1.25:
        destination = img2_path + "0.75/" + os.path.basename(img)
        shutil.copyfile(img, destination)