import os
import glob

img_path = "./masked_img"
img2_path = "./classified"
img_files = glob.glob(img_path + '/*')
img2_files = glob.glob(img2_path + '/*')