import cv2
import glob
import re
import numpy as np
import os

img_path = "./merged_img"
masked_path = "./masked_img/"
img_files = glob.glob(img_path + '/*')

for img_path in img_files:

    img = cv2.imread(img_path)

    color = map(int, input().split("/"))

    arucoDict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_5X5_50)
    arucoParams = cv2.aruco.DetectorParameters_create()
    (corners, ids, rejected) = cv2.aruco.detectMarkers(img, arucoDict, parameters=arucoParams)

    print(corners)

    try:

        point_1, point_2, point_3, point_4, dummy = str(corners).split("],")

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

        dimensions = img.shape
        img_height = dimensions[0]
        img_width = dimensions[1]

        sum_x = int(x1n) + int(x2n) + int(x3n) + int(x4n)
        x_avg = int(sum_x / 4)
        sum_y = int(y1n) + int(y2n) + int(y3n) + int(y4n)
        y_avg = int(sum_y / 4)

        p1 = [int(x1n), int(y1n)]
        p2 = [int(x2n), int(y2n)]
        p3 = [int(x3n), int(y3n)]
        p4 = [int(x4n), int(y4n)]

        points = [p1, p2, p3, p4]

        for i in points:

            print(i)

        margin = int(input())

        for i in points:

            if i[0] > x_avg:

                i[0] = i[0] + margin

            else:

                i[0] = i[0] - margin

            if i[1] > y_avg:

                i[1] = i[1] - margin

            else:

                i[1] = i[1] + margin




        mask = np.zeros((img_height, img_width, 3), np.uint8)
        background = np.zeros((img_height, img_width, 3), np.uint8)
        #pt1 = np.array([[x1n, y1n], [x2n, y2n], [x3n, y3n], [x4n, y4n]], np.int32)
        pt1 = np.array(p1, p2, p3, p4, np.int32)

        red = color[0]
        green = color[1]
        blue = color[2]
        
        mask = cv2.fillConvexPoly(mask, pt1, (red,green,blue))

        cv2.fillConvexPoly(mask, np.array([p1, p2, p3, p4]), (255, 255, 255))
        cv2.copyTo(img, mask, background)

        resize_img = cv2.resize(background, (0, 0), fx=0.15, fy=0.15, interpolation=cv2.INTER_AREA)
        resize_img1 = cv2.resize(mask, (0, 0), fx=0.15, fy=0.15, interpolation=cv2.INTER_AREA)
        resize_img2 = cv2.resize(img, (0, 0), fx=0.15, fy=0.15, interpolation=cv2.INTER_AREA)

        #cv2.imshow('rgb_image', resize_img)
        #cv2.imshow('rgb_image1', resize_img1)
        #cv2.imshow('rgb_image2', resize_img2)
        #cv2.waitKey(0)

        cv2.imwrite(masked_path + os.path.basename(img_path), background)

    except:

        print("couldn't find marker")









