import cv2
import matplotlib.pyplot as plt
import numpy as np


kernel_1 = np.ones((5,5), np.uint8)

#rectangular kernel
kernel_2 = cv2.getStructuringElement(cv2.MORPH_RECT, (9,9))

#ellipse kernel
kernel_3 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9,9))

#cross kernel
kernel_4 = cv2.getStructuringElement(cv2.MORPH_CROSS, (9,9))

FONT_SIZE = 8
COLOR = 'maroon'


'''
print('normal kernel:')
print(kernel_1)


print('rectangular kernel:')
print(kernel_2)


print('ellipse kernel:')
print(kernel_3)



print('cross kernel:')
print(kernel_4)
'''

#show the images on plt
def show_plot(images, titles):
    #convert all images to gray scale
    plt.style.use('grayscale')
    #to remove background gray
    plt.figure().patch.set_facecolor('white')
    for i in range(len(images)):
        #plt.subplot(len(titles),1,i+1)
        plt.subplot(1,len(titles),i+1)
        plt.title(titles[i], size = FONT_SIZE, color=COLOR)
        plt.imshow(images[i])
        plt.axis('off')

    plt.show()


#remove white pixels
def morhp_erosion():
    img = cv2.imread(r'S08_sample_images/j.png', 0)
    erosion_1 = cv2.erode(img, kernel_1, iterations = 1)
    erosion_2 = cv2.erode(img, kernel_2, iterations = 1)
    erosion_3 = cv2.erode(img, kernel_3, iterations = 1)
    erosion_4 = cv2.erode(img, kernel_4, iterations = 1)

    images = [img, erosion_1, erosion_2, erosion_3, erosion_4]
    titles = ['original', 'erosion 5x5', 'erosion rectangle', 'erosion eclipse', 'erosion cross']

    show_plot(images, titles)
        

#add white pixels
def morph_dilation():
    img = cv2.imread(r'S08_sample_images/j.png', 0)
    dilation_1 = cv2.dilate(img, kernel_1, iterations = 1)
    dilation_2 = cv2.dilate(img, kernel_2, iterations = 1)
    dilation_3 = cv2.dilate(img, kernel_3, iterations = 1)
    dilation_4 = cv2.dilate(img, kernel_4, iterations = 1)

    images = [img, dilation_1, dilation_2, dilation_3, dilation_4]
    titles = ['original', 'dilation 5x5', 'dilation rectangle', 'dilation eclipse', 'dilation cross']

    show_plot(images, titles)



#first do erosion then dialitaion
def morph_opening():
    img = cv2.imread(r'S08_sample_images/opening.png', 0)
    
    opening_2 = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel_2)
    opening_3 = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel_3)
    opening_4 = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel_4)

    images = [img, opening_2, opening_3, opening_4]
    titles = ['original', 'opening rectangle', 'opening eclipse', 'opening cross']

   
    show_plot(images, titles)

#first do dialation then erosion
def morph_closing():
    img = cv2.imread(r'S08_sample_images/closing.png', 0)
    
    opening_2 = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel_2)
    opening_3 = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel_3)
    opening_4 = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel_4)

    images = [img, opening_2, opening_3, opening_4]
    titles = ['original', 'closing rectangle', 'closing eclipse', 'closing cross']

   
    show_plot(images, titles)

'''
first perfom dialation and erosion ->
take different between dilation image and erosion image
'''
def morph_gradient():
    img = cv2.imread(r'S08_sample_images/j.png', 0)
    
    opening_2 = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel_2)
    opening_3 = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel_3)
    opening_4 = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel_4)

    images = [img, opening_2, opening_3, opening_4]
    titles = ['original', 'gradient rectangle', 'gradient eclipse', 'gradient cross']

   
    show_plot(images, titles)



#dirretn between original image and opening image
def morph_tophat():
    img = cv2.imread(r'S08_sample_images/testing2.png', 0)
    
    opening_2 = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel_2)
    opening_3 = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel_3)
    opening_4 = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel_4)

    images = [img, opening_2, opening_3, opening_4]
    titles = ['original', 'tophat rectangle', 'tophat eclipse', 'tophat cross']

   
    show_plot(images, titles)


#dirretn between original image and closing image
def morph_blackhat():
    img = cv2.imread(r'S08_sample_images/testing1.jpg', 0)
    
    opening_2 = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel_2)
    opening_3 = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel_3)
    opening_4 = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel_4)

    images = [img, opening_2, opening_3, opening_4]
    titles = ['original', 'blackhat rectangle', 'blackhat eclipse', 'blackhat cross']

   
    show_plot(images, titles)





def detect_contours():
    img = cv2.imread(r'S08_sample_images/plus.jpg', 1)
    img_ = img.copy()
    img__ = img.copy()
    img_org = img.copy()
    
    img_g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(img_g, 50,255,0)

    #find contours
    #open cv2 doent return image
    #image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
                                               #RGB
    img_1 = cv2.drawContours(img, contours, -1, (0,255,0), 2)
    img_2 = cv2.drawContours(img_, contours, 3, (255,0,0), 2)

    cnt = contours[5]
    cnt_1 = contours[6]
    
    img_3 = cv2.drawContours(img__, [cnt, cnt_1], -1, (0,0,255), 2)

    images = [img_org, img_1, img_2, img_3]
    titles = ['original', 'all Contours', '3rd Contours', '6th and 7th Contours']

    show_plot(images, titles)

    #for i in range(len(contours)):
        #img_4 = cv2.drawContours(img__, contours, i, (i+50,i+50,i+50), 2)
        

    



#detect_contours()

#morph_blackhat()
#morph_tophat()
#morph_gradient()
#morph_closing()    
#morph_opening()   
#morph_dilation()   
#morhp_erosion()
