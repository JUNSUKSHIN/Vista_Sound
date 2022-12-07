import cv2
import glob
import numpy as np

img_path = "./merged_img"
img_files = glob.glob(img_path + '/*')

for img in img_files:

    im = cv2.imread(img)

    arucoDict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_5X5_50)
    arucoParams = cv2.aruco.DetectorParameters_create()
    (corners, ids, rejected) = cv2.aruco.detectMarkers(im, arucoDict, parameters=arucoParams)

    print(corners)