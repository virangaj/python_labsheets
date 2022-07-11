import cv2
import numpy as np

def readImage():
    img_read = 'ColorChecker.png'
    img_1 = cv2.imread(img_read, cv2.IMREAD_COLOR)
    img_2 = cv2.imread(img_read, cv2.IMREAD_ANYCOLOR)
    img_3 = cv2.imread(img_read, cv2.IMREAD_GRAYSCALE)
    cv2.imshow('main', np.vstack((img_1, img_2, img_3)))
    

readImage()
# cv2.destroyAllWindows()