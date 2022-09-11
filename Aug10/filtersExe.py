import numpy as np
import matplotlib.pyplot as plt
import cv2



def custom_filters():
    location = r'Sample_images/test_pattern_blurring_orig.tif'
    img = cv2.imread(location, cv2.IMREAD_GRAYSCALE)

    kerne1 = np.ones((5,5), np.float32)/25
    kerne1_2 = np.ones((9,9), np.float32)/81
    kerne1_3 = np.array([[1,1,1],
                         [1,1,1],
                         [1,1,1]])/9

    kerne1_4 = np.array([[-1/9, -1/9, -1/9],
                         [-1/9, 8/9, -1/9],
                         [-1/9, -1/9, -1/9]])

    kerne1_5 = np.array([[-1, -1, -1],
                         [-1, 8, -1],
                         [-1, -1, -1]])

    #res_img = cv2.filter(scr, depth, kernel)
    dst = cv2.filter2D(img, -1, kerne1)
    dst_2 = cv2.filter2D(img, -1, kerne1_2)
    dst_3 = cv2.filter2D(img, -1, kerne1_3)
    dst_4 = cv2.filter2D(img, -1, kerne1_4)
    dst_5 = cv2.filter2D(img, -1, kerne1_5)
    

    images = (img, dst, dst_2, dst_3, dst_4, dst_5)
    title = ('original', 'filter 1', 'filter 2', 'filter 3', 'filter 4', 'filter 5')

    for i in range(len(title)):
        plt.subplot(2,3,i+1)
        plt.title(title[i])
        plt.imshow(images[i], cmap='Greys_r')
        #plt.xticks([])
        #plt.yticks([])
        plt.axis('off')

    plt.show()

###### Low pass filtering
    
def averaging_filter():
    location = r'Sample_images/test_pattern_blurring_orig.tif'
    img = cv2.imread(location, cv2.IMREAD_GRAYSCALE)

    blur = cv2.blur(img, (9,9))

    blur_ = cv2.boxFilter(img, -1, (13,13))
    blur_21 = cv2.boxFilter(img, -1, (21,21))

    plt.subplot(1,4,1)
    plt.title('original')
    plt.imshow(img, cmap='Greys_r')
    plt.axis('off')

        
    plt.subplot(1,4,2)
    plt.title('blur 9x9')
    plt.imshow(blur, cmap='Greys_r')
    plt.axis('off')
        
    plt.subplot(1,4,3)
    plt.title('blur 13x13')
    plt.imshow(blur_, cmap='Greys_r')
    plt.axis('off')

    plt.subplot(1,4,4)
    plt.title('blur 21x21')
    plt.imshow(blur_21, cmap='Greys_r')
    plt.axis('off')
        
    plt.show()    




def gaussian_filter():
    location = r'Sample_images/test_pattern_blurring_orig.tif'
    img = cv2.imread(location, cv2.IMREAD_GRAYSCALE)

    blur = cv2.GaussianBlur(img, (5,5), 0)
    blur_2 = cv2.GaussianBlur(img, (17,17), 0)
    blur_3 = cv2.GaussianBlur(img, (23,23), 0)

    plt.subplot(1,4,1)
    plt.title('original')
    plt.imshow(img, cmap='Greys_r')
    plt.axis('off')

        
    plt.subplot(1,4,2)
    plt.title('blur 5x5')
    plt.imshow(blur, cmap='Greys_r')
    plt.axis('off')
        
    plt.subplot(1,4,3)
    plt.title('blur 17x17')
    plt.imshow(blur_2, cmap='Greys_r')
    plt.axis('off')

    plt.subplot(1,4,4)
    plt.title('blur 23x23')
    plt.imshow(blur_3, cmap='Greys_r')
    plt.axis('off')
    plt.show()    


# remove salt and paper noise
def median_filter():
    location = r'Sample_images/test_pattern_blurring_orig.tif'
    location_ = r'Sample_images/ckt_board_saltpep.tif'
    img = cv2.imread(location, cv2.IMREAD_GRAYSCALE)
    img_ = cv2.imread(location_, cv2.IMREAD_GRAYSCALE)

    blur = cv2.medianBlur(img, 5)
    blur_2 = cv2.medianBlur(img, 9)

    blur_3 = cv2.medianBlur(img_, 5)
    blur_4 = cv2.medianBlur(img_, 9)

    images = (img, blur, blur_2, img_, blur_3, blur_4)
    title = ('original', 'blur 5', 'blur 9', 'original', 'blur 5', 'blur 9')
    
    for i in range(len(title)):
        plt.subplot(2,3,i+1)
        plt.title(title[i])
        plt.imshow(images[i], cmap='Greys_r')
        #plt.xticks([])
        #plt.yticks([])
        plt.axis('off')

    plt.show()                        
       
    

#blur image while preserve edges
def bilateral_filter():
    location = r'Sample_images/img_mri_brain_tumor.jpg'
    img = cv2.imread(location, cv2.IMREAD_GRAYSCALE)

    #cv2.bilateralFilter(image, neighborhood, sigmacolor, sigmaspace)

    blur = cv2.bilateralFilter(img, 9, 75, 75)
    blur_ = cv2.bilateralFilter(img, 17, 75, 75)

    images = (img, blur, blur_)
    title = ('original', 'blur 9', 'blur 17')

  
    for i in range(len(title)):
        plt.subplot(1,3,i+1)
        plt.title(title[i])
        plt.imshow(images[i], cmap='Greys_r')
        #plt.xticks([])
        #plt.yticks([])
        plt.axis('off')

    plt.show()
    


###### High pass filtering

#can be used in edge detection
def sobel_filter():
    location = r'Sample_images/sudoku-original_clahe.jpg'
    img = cv2.imread(location, cv2.IMREAD_GRAYSCALE)

    grad_x = cv2.Sobel(img, cv2.CV_8U, 1, 0, ksize=3)
    grad_x2 = cv2.Sobel(img, cv2.CV_32F, 1, 0, ksize=3)
    grad_x3 = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
        
    grad_y = cv2.Sobel(img, cv2.CV_8U, 0, 1, ksize=3)
    grad_y2 = cv2.Sobel(img, cv2.CV_32F, 0, 1, ksize=3)
    grad_y3 = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)

    grad_xy = cv2.Sobel(img, cv2.CV_8U, 1, 1, ksize=3)


    sum_xy = cv2.add(grad_x, grad_y)
    sum_xy2 = cv2.add(grad_x2, grad_y2)
    sum_xy3 = cv2.add(grad_x3, grad_y3)    

    images = (img, grad_x, grad_x2, grad_x3, img, grad_y, grad_y2, grad_y3, grad_xy, sum_xy, sum_xy2, sum_xy3)
    title = ('original', 'grad CV_8U', 'grad CV_32F', 'grad CV_64F', 'original', 'grad CV_8U', 'grad CV_32F', 'grad CV_64F', 'add xy', 'add CV_8U', 'add CV_32F', 'add CV_64F' )
    
    for i in range(len(images)):
        plt.subplot(3,4,i+1)
        plt.title(title[i])
        plt.imshow(images[i], cmap='Greys_r')
        #plt.xticks([])
        #plt.yticks([])
        plt.axis('off')

    plt.show()           


#dirrefent between sobel and laplacian is that sobel can choose a axis, 

def laplacian_flter():
    
    location = r'Sample_images/sudoku-original_clahe.jpg'
    img = cv2.imread(location, cv2.IMREAD_GRAYSCALE)

    laplacian = cv2.Laplacian(img, cv2.CV_8U, ksize=3)
    laplacian_ = cv2.Laplacian(img, cv2.CV_16U, ksize=3)

    images = (img, laplacian, laplacian_)
    title = ('original', 'laplacian CV_8U', 'laplacian CV_16U')

  
    for i in range(len(title)):
        plt.subplot(1,3,i+1)
        plt.title(title[i])
        plt.imshow(images[i], cmap='Greys_r')
        #plt.xticks([])
        #plt.yticks([])
        plt.axis('off')

    plt.show()
    


def unsharp_mask():
    location = r'Sample_images/blurry_moon.tif'
    img = cv2.imread(location, cv2.IMREAD_GRAYSCALE)

    #method 1
    gauss = cv2.GaussianBlur(img, (11,11), 0)

    sharpend_image = cv2.addWeighted(img, 2, gauss, -1, 0)

    #method 2
    #blur the image
    gauss_ = cv2.GaussianBlur(img, (13,13), 0)
    #create mask
    mask = cv2.subtract(img, gauss)
    
    #add mast to original -> if you want to perform normal mask insert 1, or highr boost filtering inter value heigher than 1
    sharpend_image_ = cv2.add(img, cv2.multiply(mask, 1))
    sharpend_image_2 = cv2.add(img, cv2.multiply(mask, 2))
    sharpend_image_3 = cv2.add(img, cv2.multiply(mask, 3))

    
    images = (img, gauss, sharpend_image, img, img, gauss_, mask, sharpend_image_)
    title = ('original', 'gauss', 'sharpend image', 'img', 'original', 'gauss_', 'mask','sharpend_image_')


    s_images = (img, sharpend_image_, sharpend_image_2, sharpend_image_3)
    s_title = ('original', 'sharpend_image_', 'sharpend_image_2', 'sharpend_image_3')
    
    for i in range(len(title)):
       
        plt.subplot(2,4,i+1)
        plt.title(title[i])
        plt.imshow(images[i], cmap='Greys_r')
        plt.axis('off')

    for i in range(len(s_images)):
       
        plt.subplot(1,4,i+1)
        plt.title(s_title[i])
        plt.imshow(s_images[i], cmap='Greys_r')
        plt.axis('off')

    plt.show()




###### High pass filtering
#sobel_filter()
#laplacian_flter()
unsharp_mask()
    
###### Low pass filtering
#bilateral_filter()
#median_filter()
#gaussian_filter()
#averaging_filter()
#custom_filters()
