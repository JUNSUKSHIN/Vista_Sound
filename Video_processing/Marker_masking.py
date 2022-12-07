import cv2
import glob
import numpy as np

img_path = "./merged_img"
img_files = glob.glob(img_path + '/*')

for img in img_files:

    im = cv2.imread("20221208_001741.jpg")

    arucoDict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_5X5_50)
    arucoParams = cv2.aruco.DetectorParameters_create()
    (corners, ids, rejected) = cv2.aruco.detectMarkers(im, arucoDict, parameters=arucoParams)

    print(corners)

    point_1, point_2, point_3, point_4 = str(corners).split("],")
    x1, y1 = point_1.split(".,")
    x2, y2 = point_2.split(".,")
    x3, y3 = point_3.split(".,")
    x4, y4 = point_4.split(".,")



