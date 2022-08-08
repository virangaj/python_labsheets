import cv2
import numpy as np
import matplotlib.pyplot as plt


def question_1():
    img  = cv2.imread(r'fire.jpg', cv2.IMREAD_ANYCOLOR)
    img_ = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h,s,v = cv2.split(img_hsv)

    v_ = cv2.equalizeHist(v)

    eq_img = cv2.cvtColor(cv2.merge([h,s,v_]), cv2.COLOR_HSV2RGB)
    

    ret, thresh = cv2.threshold(eq_img, 205, 255, cv2.THRESH_BINARY_INV) 

    mask = cv2.inRange(thresh, (0,0,255), (0,255,255))

    final = cv2.bitwise_and(eq_img, eq_img, mask = mask)

   
    
    plt.subplot(131)
    plt.title('original image')
    plt.imshow(img)
    plt.xticks([])
    plt.yticks([])

    plt.subplot(132)
    plt.title('mask')
    plt.imshow(mask)
    plt.xticks([])
    plt.yticks([])


    plt.subplot(133)
    plt.title('REsult')
    plt.imshow(final)
    plt.xticks([])
    plt.yticks([])

    plt.show()
    






def create_clahe_img(img, value):
    h,s,v = cv2.split(cv2.cvtColor(img, cv2.COLOR_BGR2HSV))
    
    clahe = cv2.createCLAHE(clipLimit = value, tileGridSize = (8,8))
    v_ = clahe.apply(v)

    result = cv2.cvtColor(cv2.merge([h,s,v_]), cv2.COLOR_HSV2RGB)
    
    return result
    
    


def question_2():
    img = cv2.imread(r'1.jpg', cv2.IMREAD_ANYCOLOR)
    


    img_2 = create_clahe_img(img, 2.0)
    img_5 = create_clahe_img(img, 5.0)
    img_10 = create_clahe_img(img, 10.0)
    img_20 = create_clahe_img(img, 20.0)

    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    


    titles = ['original', 'clahe 2.0', 'clahe 5.0', 'clahe 10.0', 'clahe 20.0']
    images = [img, img_2, img_5, img_10, img_20]


    for i in range(len(titles)):
        plt.subplot(2,3,i+1)
        plt.title(titles[i])
        plt.imshow(images[i])
        plt.xticks([])
        plt.yticks([])
        

    plt.show()






question_1()
##question_2()
