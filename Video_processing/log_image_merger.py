import os
import glob

img_path = "./image"

img_files = glob.glob(img_path + '/*')
f= open('matrix_quotes.txt','r')