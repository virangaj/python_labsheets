import cv2
import numpy as np
import matplotlib.pyplot as plt

def masking():
    inputColor = input("Enter color to mask : ")
    img = cv2.imread('ColorChecker.png')
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    colorsRange =[
        {"key":"blue" , "l1":80 , "u1":100 , "l2":100 , "u2":130},
        {"key":"red" , "l1":0 , "u1":5 , "l2":175 , "u2":180},
        {"key":"green" , "l1":35 , "u1":50 , "l2":50 , "u2":70},
        {"key":"yellow" , "l1":20 , "u1":30 , "l2":30 , "u2":35},
        {"key":"orange" , "l1":12 , "u1":15 , "l2":15 , "u2":20},
        {"key":"purple" , "l1":130 , "u1":150 , "l2":150 , "u2":160},
        {"key":"gray" , "l1":0 , "u1":0 , "l2":0 , "u2":0}
        ]



    for color in colorsRange:
        mask1 = None
        mask2 = None
        if inputColor.casefold() == color['key']:
            if color['key'] != 'gray':
                mask1=cv2.inRange(img_hsv, (color['l1'],50,20), (color['u1'],255,255))
                mask2=cv2.inRange(img_hsv, (color['l2'],50,20), (color['u2'],255,255))
            else:
                mask1=cv2.inRange(img_hsv, (0,0,40), (0,0,100))
                mask2=cv2.inRange(img_hsv, (0,0,100), (0,0,240))
            print(color)
            mask = cv2.bitwise_or(mask1, mask2)
            cropped = cv2.bitwise_and(img, img, mask = mask)  
            cv2.imshow('mask',mask)
            cv2.imshow('cropped',cropped)
            cv2.imwrite('{}.png'.format(inputColor), cropped)
            cv2.waitKey(2000)
            cv2.destroyAllWindows()
            break
       

masking()

