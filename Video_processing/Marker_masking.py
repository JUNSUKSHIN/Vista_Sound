import cv2
import glob
import re
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

    x1n = re.sub(r'[^0-9]', '', x1)
    x2n = re.sub(r'[^0-9]', '', x2)
    x3n = re.sub(r'[^0-9]', '', x3)
    x4n = re.sub(r'[^0-9]', '', x4)
    y1n = re.sub(r'[^0-9]', '', y1)
    y2n = re.sub(r'[^0-9]', '', y2)
    y3n = re.sub(r'[^0-9]', '', y3)
    y4n = re.sub(r'[^0-9]', '', y4)




