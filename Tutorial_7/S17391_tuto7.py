import numpy as np
import matplotlib.pyplot as plt
import cv2


#get image
def getImage():
    return cv2.imread(r'overlap_coins.jpg', cv2.IMREAD_COLOR)


def show_img(img, title):

    #convert all images to gray scale
    plt.style.use('grayscale')
    #to remove background gray
    plt.figure().patch.set_facecolor('white')

    for i in range(len(img)):
        plt.subplot(1,len(img),i+1)
        plt.title(title[i])
        plt.imshow(img[i])
        plt.axis('off')

    plt.show()


def return_index(arr):
    max_value = cv2.contourArea(arr[0])
    max_index = 0
    second_max_index = 0
    for i in range(len(arr)):
        if max_value < cv2.contourArea(arr[i]):
            max_value = cv2.contourArea(arr[i])
            second_max_index = max_index
            max_index = i

    return second_max_index
            
            

def question_1():
    img = getImage()
    img_1 = img.copy()
    
    
    #create kernel
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (21,21))
    
    #convert in to gray image
    img_ = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    
    #binary image
    ret,binary_inv = cv2.threshold(img_, 100, 255, cv2.THRESH_BINARY_INV)

    #erosion
    erosion = cv2.erode(binary_inv, kernel, iterations=1)
    
    erosion_ = cv2.cvtColor(erosion, cv2.COLOR_GRAY2RGB)

    #find contours
    contours, hierarchy = cv2.findContours(erosion.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 

    #draw contours
    result = cv2.drawContours(erosion_, contours, -1, (0,255,0), 2)

    #calcultae area
    total_area = 0
    area = np.zeros(len(contours))
    for i in range(len(contours)):
        area[i] = cv2.contourArea(contours[i])
        total_area += cv2.contourArea(contours[i])
    
    #get second largest index
    index = return_index(contours)
    
    perimeter = cv2.arcLength(contours[index], True)
    perimeter = "{0:.2f}".format(perimeter)
    
    print('No: of coins : {}'.format(len(contours)))
    print('Area covered by coins : {} pixels(sqr)'.format(total_area))
    print('Second largest perimeter of coins : {} pixels'.format(perimeter))

    
    #show images

    images = [img, binary_inv, erosion, result ]
    titles = ['original', 'thresh','eroded', 'final']

    show_img(images, titles)




question_1()
