import cv2
import numpy as np
import matplotlib.pyplot as plt

img_read = 'ColorChecker.png'
img_1 = cv2.imread(img_read, cv2.IMREAD_COLOR)
def readImage():
    
    img_1 = cv2.imread(img_read, cv2.IMREAD_COLOR)
    img_2 = cv2.cvtColor(img_1, cv2.COLOR_BGR2RGB)
    img_3 = cv2.cvtColor(img_1, cv2.COLOR_BGR2HSV)
    img_4 = cv2.applyColorMap(img_1, cv2.COLORMAP_BONE)
    cv2.imshow('main', np.hstack((img_1, img_2, img_4)))

    plt.figure(figsize =(6,6), num="test_img")
    plt.subplot(3,1,1)
    plt.imshow(img_1, cmap='Blues')
    plt.xticks([]),plt.yticks([])
    
    plt.subplot(3,1,2)
    plt.imshow(img_2)
    plt.xticks([]),plt.yticks([])
    
    plt.subplot(3,1,3)
    plt.imshow(img_3)
    plt.xticks([]),plt.yticks([])
    plt.savefig('differe_color.png')
    plt.show()
    


def saveImg():
    img_1 = cv2.imread(img_read, cv2.IMREAD_COLOR)
    cv2.imwrite('test_gray.png', img_1)
    
    
                    
def color_array():
    img_2 = cv2.cvtColor(img_1, cv2.COLOR_BGR2RGB)
    print(img_2.shape) #row, col, channel
    print(img_2[:,:,2])
    
    print(img_2.dtype)
    



def gray_scale():
    img_location = 'Tutorial_4\images\meter1.jpg'
    img = cv2.imread(img_location, cv2.IMREAD_GRAYSCALE) #0

    #method 1
    not_ = cv2.bitwise_not(img)

    #method 2
    img4 = img.copy()
    for i in range(img4.shape[0]):
        for j in range(img4.shape[1]):
            img4[i,j] = 255 - img[i,j]


    plt.subplot(231)
    plt.title('original')
    plt.imshow(img, cmap='Greys_r')

    plt.subplot(232)
    plt.title('Gray')
    plt.imshow(not_, cmap='Greys_r')

    plt.subplot(233)
    plt.title('method')
    plt.imshow(img4, cmap='Greys_r')


    plt.show()

def increase_brightness_gray(value):        
    img_location = 'Tutorial_4\images\cameraman.tif'
    img = cv2.imread(img_location, cv2.IMREAD_GRAYSCALE)
    #cv2.imshow('main', img)

    img2 = img.copy()
    img2 = cv2.add(img, value)

    plt.subplot(121)
    plt.title('original')
    plt.imshow(img, cmap='Greys_r')
    
    plt.subplot(122)
    plt.title('brightness')
    plt.imshow(img2, cmap='Greys_r')

    plt.show()


increase_brightness_gray(80)
##gray_scale()
##readImage()
##saveImg()
##color_array()
