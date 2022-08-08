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
    img_location = 'sample_images\meter1.jpg'
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

def change_brightness_gray(value):
    img_location = 'sample_images\cameraman.tif'


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


def change_brightness_color(value):
    img_location = 'sample_images\messi5.jpg'
    img = cv2.imread(img_location, cv2.IMREAD_COLOR)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    h,s,v = cv2.split(hsv)
    #increase britghtness

    print(h)
    print(s)
    print(v)

    lim = 255 - value
    v[v > lim] = 255
    plt.subplot(131)
    plt.title('original')
    plt.imshow(img)

    plt.subplot(132)
    plt.title('hsv')
    plt.imshow(hsv)

    plt.subplot(133)
    plt.title('brightness')
    plt.imshow(hsv)

    plt.show()



def log_transformation():
    img_location = r'sample_images\meter1.jpg'
    img = cv2.imread(img_location, cv2.IMREAD_GRAYSCALE)
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    c = 255 / np.log(1+np.max(img))
    log_img = c * (np.log(img+1))

    log_img_ = np.log(img + 1)

    log_image1 = np.array(log_img, dtype = np.uint8)
    log_image2 = np.array(log_img_, dtype = np.uint8)
    print(255 / np.log(1+np.max(img_hsv)))

    plt.subplot(131)
    plt.title('img')
    plt.imshow(img, cmap='Greys_r')

    plt.subplot(132)
    plt.title('log_img')
    plt.imshow(log_image1, cmap='Greys_r')

    plt.subplot(133)
    plt.title('log_img with scaling constant')
    plt.imshow(log_image2, cmap='Greys_r')

    plt.show()



def constrast():
    img_location = r'sample_images\contrast_str.png'
    img = cv2.imread(img_location, cv2.IMREAD_GRAYSCALE)

    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    ##img_ = img.cpoy()


    input_max = np.max(img)
    input_min = np.min(img)

    output_max = 255  ##np.iinfo('uint8').max
    output_min = 0 ##np.iinfo('uint8').min

    output_img = (img - input_min)*((output_max - output_min)/(input_max - input_min))
    output_img = np.array(output_img , dtype=np.uint8)


    plt.subplot(231)
    plt.title('img')
    plt.imshow(img,cmap='Greys_r')

    plt.subplot(232)
    plt.title('Original grayscale image histogram')
    plt.hist(img.ravel(), bins=256, range=[0,256])

    plt.subplot(233)
    plt.title('output_img')
    plt.imshow(output_img,cmap='Greys_r')

    plt.subplot(235)
    plt.title('constrast grayscale image histogram')
    plt.hist(output_img.ravel(), bins=256, range=[0,256])

    plt.show()





def gray_level_slicing():
    img_location = r'sample_images\cameraman.tif'
    img = cv2.imread(img_location, cv2.IMREAD_GRAYSCALE)
    img_ = img.copy()

    t1 = 100
    t2 = 180

    img_new = np.zeros((img.shape[0], img.shape[1]), dtype='uint8')

    print(img)
    print(img_new)


    for i in range(img.shape[0]):
        for j in range(img.shape[1]):

            if t1 < img[i][j] and t2 > img[i][j]:
                img_new[i][j]= 255
            else:
                img_new[i][j] = img[i][j]

    x = np.arange(0,256,1)
    print(x)

    x1 = np.array(x)

    y3 = np.zeros_like(x1)

    for i in range(0, len(x1)):
        if x1[i] < t2 and x1[i] > t1:
            y3[i] = 255
        else:
            y3[i] = x1[i]
    

    
    plt.subplot(221)
    plt.title('original image')
    plt.imshow(img, cmap='Greys_r')

    plt.subplot(222)
    plt.title('sliced image')
    plt.imshow(img_new, cmap='Greys_r')

    plt.subplot(223)
    
    plt.plot(x,y3)


    plt.show()


def tresholding():
    img_location = r'sample_images\cameraman.tif'
    img = cv2.imread(img_location, cv2.IMREAD_GRAYSCALE)

    t1 = 100
    img_new = np.zeros((img.shape[0], img.shape[1]), dtype='uint8')


    for i in range(img.shape[0]):
        for j in range(img.shape[1]):

            if t1 < img[i][j]:
                img_new[i][j]= 255
            else:
                img_new[i][j] = 0

    x = np.arange(0,256,1)
    x1 = np.array(x)

    y3 = np.zeros_like(x1)

    for i in range(0, len(x1)):
        if x1[i] > t1:
            y3[i] = 255
        else:
            y3[i] = 0

    plt.subplot(221)
    plt.title('original image')
    plt.imshow(img, cmap='Greys_r')

    plt.subplot(222)
    plt.title('Treshed image')
    plt.imshow(img_new, cmap='Greys_r')

    plt.subplot(223)
    
    plt.plot(x,y3)


    plt.show()


def global_tresholding():
    img_location = r'sample_images\numbers.jpg'
    img = cv2.imread(img_location, cv2.IMREAD_GRAYSCALE)

    t1 = 150

    ret,binary = cv2.threshold(img, t1, 255, cv2.THRESH_BINARY)
    ret,binary_inv = cv2.threshold(img, t1, 255, cv2.THRESH_BINARY_INV)
    ret,trunc = cv2.threshold(img, t1, 255, cv2.THRESH_TRUNC)
    ret,tozero = cv2.threshold(img, t1, 255, cv2.THRESH_TOZERO)
    ret,tozero_inv = cv2.threshold(img, t1, 255, cv2.THRESH_TOZERO_INV)
    
    titles = ['img', 'binary', 'binary_inv', 'thrunc', 'tozero', 'tozero_inv']
    images = [img, binary, binary_inv, trunc, tozero, tozero_inv]
    

    print(ret) #t1
    for i in range(len(images)):
        plt.subplot(2,3,i+1)
        plt.title(titles[i])
        plt.imshow(images[i], cmap='Greys_r')
        plt.xticks([])
        plt.yticks([])
        


    plt.show()




def adaptive_tresholding():
    img_location = r'sample_images\sudoku-original.jpg'
    img = cv2.imread(img_location, cv2.IMREAD_GRAYSCALE)

    img = cv2.medianBlur(img, 5)
    ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

    th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 15, 10)
    th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 15, 10)

    titles = ['img', 'global', 'THRESH_MEAN', 'THRESH_GUSSAIN']
    images = [img, th1, th2, th3]

    for i in range(len(images)):
        plt.subplot(2,2,i+1)
        plt.title(titles[i])
        plt.imshow(images[i], cmap='Greys_r')
        plt.xticks([])
        plt.yticks([])
        


    plt.show()

    
def otzu_tresholding():
    img_location = r'sample_images\noisy2.png'
    img = cv2.imread(img_location, cv2.IMREAD_GRAYSCALE)


    noise_less = cv2.medianBlur(img, 5)
    
    ret1, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    ret2, th2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    ret2, th3 = cv2.threshold(noise_less, 127, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    titles = ['original','histogram','global',
             'original','histogram','with noise',
             'noise_less','histogram','without noise']
    images = [img, 0 ,th1,
              img, 0 ,th2,
              noise_less, 0 ,th3]
        
    for i in range(3):
        plt.subplot(3,3,i*3+1)
        plt.title(titles[i*3])
        plt.imshow(images[i*3], cmap='Greys_r')
        plt.xticks([]), plt.yticks([])

        plt.subplot(3,3,i*3+2)
        plt.title(titles[i*3+1])
        plt.hist(images[i*3].ravel(), 256)
        plt.xticks([]), plt.yticks([])

        plt.subplot(3,3,i*3+3)
        plt.title(titles[i*3+2])
        plt.imshow(images[i*3+2], cmap='Greys_r')
        plt.xticks([]), plt.yticks([])
        

    plt.show()

def histogram_image():
    img_location = r'sample_images\Aerial.tif'
    img = cv2.imread(img_location, cv2.IMREAD_GRAYSCALE)  


    plt.subplot(131)
    plt.title('original')
    plt.imshow(img, cmap='Greys_r')

    plt.subplot(132)
    plt.title('plt hist')
    plt.hist(img.ravel(), 256, [0,256])

    plt.subplot(133)
    plt.title('cv2 hist')
    histr = cv2.calcHist([img], [0], None, [256], [0, 256])
    plt.plot(histr)

    plt.show()
    



##histogram equalization for color images

def histogram_equalization_grey():
    img_location = r'sample_images\Aerial.tif'
    img = cv2.imread(img_location, cv2.IMREAD_GRAYSCALE)  
    hist_eq = cv2.equalizeHist(img)


    plt.subplot(221)
    plt.title('original image')
    plt.imshow(img, cmap='Greys_r')

    plt.subplot(222)
    plt.title('original hsit')
    plt.hist(img.ravel(), bins=256, range=[0,256]) 
    
    plt.subplot(223)
    plt.title('equalized image')
    plt.imshow(hist_eq, cmap='Greys_r')

    plt.subplot(224)
    plt.title('equalized hist')
    plt.hist(hist_eq.ravel(), bins=256, range=[0,256]) 

    plt.show()
    

    




def equalize_hist_color_hsv(img):
    h,s,v = cv2.split(cv2.cvtColor(img, cv2.COLOR_BGR2HSV))
    eq_v = cv2.equalizeHist(v)
    eq_image = cv2.cvtColor(cv2.merge([h,s,eq_v]),cv2.COLOR_HSV2BGR)
    #cv2.imshow('show',eq_image)
    return eq_image


def histogram_for_colorImg(img):
    hists = []
    
    for i in range(img.shape[2]):
        hist = cv2.calcHist([img], [i], None, [256], [0,256])
        hists.append(hist)

    return hists

    


def histogram_equalization_color():
    img_location = r'sample_images\1.jpg'
    img = cv2.imread(img_location, cv2.IMREAD_COLOR)
    

    eq_image = equalize_hist_color_hsv(img)
   
    
    hists_ = histogram_for_colorImg(img)

    hists_eq = histogram_for_colorImg(eq_image)

    eq_image_1 = cv2.cvtColor(eq_image, cv2.COLOR_BGR2RGB)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)



    plt.subplot(221)
    plt.title('original image')
    plt.imshow(img)

    plt.subplot(222)
    plt.title('original hsit')
    #plt.hist(img.ravel(), 255, [0,256])
    plt.plot(hists_[0], c='r')
    plt.plot(hists_[1], c='g')
    plt.plot(hists_[2], c='b')
    
    plt.subplot(223)
    plt.title('equalized image')
    plt.imshow(eq_image_1)

    plt.subplot(224)
    plt.title('equalized hist')
    plt.hist(eq_image[0].ravel(), 255, [0,256], color='r')
    plt.hist(eq_image[1].ravel(), 255, [0,256], color='g')
    plt.hist(eq_image[2].ravel(), 255, [0,256], color='b')
    #plt.plot(hists_eq[0], c='r')
    #plt.plot(hists_eq[1], c='g')
    #plt.plot(hists_eq[2], c='b')

    plt.show()
    




def contast_limited_ahe():
    img_location = r'sample_images\clahe_1.jpg'
    img = cv2.imread(img_location, cv2.IMREAD_GRAYSCALE)

    #global
    img_global = cv2.equalizeHist(img)

    #creating clahe object
    clahe  = cv2.createCLAHE(clipLimit = 2.0, tileGridSize = (8,8))
    gray_image_clahe = clahe.apply(img)

    plt.subplot(131)
    plt.title('original image')
    plt.imshow(img, cmap='Greys_r')

    plt.subplot(132)
    plt.title('global image')
    plt.imshow(img_global, cmap='Greys_r')
    
    plt.subplot(133)
    plt.title('clahe')
    plt.imshow(gray_image_clahe, cmap='Greys_r')

    plt.show()




def gamma_correction(img, gamma):
    result = np.zeros(img.shape, dtype=img.dtype)

    if len(img.shape) == 3:
        for c in range(img.shape[2]):
            result[:,:,c] = 255*((img[:,:,c]/255)**gamma)
    else:
        result = 255*((img/255)**gamma)
    return result
    
def gamma_correction_driver():
    img_location = r'sample_images\fire.jpg'
    img = cv2.imread(img_location, cv2.IMREAD_ANYCOLOR)

    gm_1 = gamma_correction(img, 0.1)
    gm_2 = gamma_correction(img, 3.0)

    if len(img.shape) == 3:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        gm_1 = cv2.cvtColor(gm_1, cv2.COLOR_BGR2RGB)
        gm_2 = cv2.cvtColor(gm_2, cv2.COLOR_BGR2RGB)


    
    plt.subplot(131)
    plt.title('original image')
    plt.imshow(img)

    plt.subplot(132)
    plt.title('brighter')
    plt.imshow(gm_1)
    
    plt.subplot(133)
    plt.title('darker')
    plt.imshow(gm_2)

    plt.show()


##gamma_correction_driver()
##contast_limited_ahe()
##histogram_equalization_color()
##histogram_image()
##histogram_equalization_grey()
##otzu_tresholding()
adaptive_tresholding()   
##global_tresholding()
##tresholding()
##gray_level_slicing()
##constrast()
##log_transformation()
##change_brightness_color(90)
##change_brightness_gray(-90)
##gray_scale()
##readImage()
##saveImg()
##color_array()
