import cv2
import glob

img_path = "./merged_img"
img_files = glob.glob(img_path + '/*')

for img in img_files:

    arucoDict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_6X6_50)
    arucoParams = cv2.aruco.DetectorParameters_create()
    (corners, ids, rejected) = cv2.aruco.detectMarkers(img, arucoDict, parameters=arucoParams)

    print(corners)