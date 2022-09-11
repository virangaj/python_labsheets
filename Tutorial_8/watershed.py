import cv2
import matplotlib.pyplot as plt
import numpy as np
import imutils
COLOR = 'maroon'
FONT_SIZE = 10

######When using different images code have changed, this is shows result for overlap_coins.jpg 


#import images
def get_image(name):
    img = cv2.imread(r'{}'.format(name), 1)
    return img

#show images
def show_images(title, images):

    for i in range(len(title)):
        plt.subplot(3,3,i+1)
        plt.title(title[i], color = COLOR, fontsize = FONT_SIZE)
        if title[i] == 'markers':
            plt.imshow(images[i], 'jet')
        else:
            plt.imshow(images[i], 'gray')
        
        plt.axis('off')

    plt.show()

def show_label(markers, image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    area = 0
    for label in np.unique(markers):
        print(label)
        if label == 0:
            continue
        else:
            mask = np.zeros(gray.shape, dtype='uint8')
            mask[markers == label] = 255
            contours = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            contours = imutils.grab_contours(contours)
            c = max(contours, key=cv2.contourArea)
            ((x, y), r) = cv2.minEnclosingCircle(c)
            cv2.circle(image, (int(x), int(y)), int(r), (0,0,255), 2)
            cv2.putText(image, '#{}'.format(label), (int(x)-10, int(y)), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0),2)    
           
            area = area + cv2.contourArea(c)
    
    return image, area
    
def main():

    ### 01. Bbackground extraction
    img = get_image('WatershedSegmentation.png')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret, thresh = cv2.threshold(gray,100, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    KERNEL_SIZE = 3

    
    
    kernel = np.ones((KERNEL_SIZE, KERNEL_SIZE), np.uint8)
    
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)

    # obtain sure_bg
    sure_bg = cv2.dilate(opening, kernel, iterations=3)

    ### 02. Foreground extraction
    dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
    ret, sure_fg = cv2.threshold(dist_transform, 0.2*dist_transform.max(), 255, 0)
    sure_fg = np.uint8(sure_fg)
       

    ### 03. Find Unknown area
    unknown = np.subtract(sure_bg, sure_fg)
    
    
    ### 04. Apply watershed algorithm
    ret, markers = cv2.connectedComponents(sure_fg)
    print(markers)
    markers = markers+1
    markers[unknown == 255] = 0
    markers = cv2.watershed(img, markers)
    result = img.copy()
    result[markers == -1] = (255, 0, 0)

    ### 05. Mark Contours
    image = img.copy()
    final, area = show_label(markers, image)

    print('Area : {}'.format(area))
    #cv2.putText(image, 'Area : {}'.format(area), (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,0), 2)   
    # images and title arrays
    images = [img,thresh, opening, sure_bg, dist_transform, sure_fg, unknown, markers, final]
    title = ['original','thresh', 'opening', 'sure_bg', 'distance transform','sure_fg','unknown region','markers', 'watershed region']

    # show images
    show_images(title, images)
    
    
    
main()

'''

overlap_coins.jpg ->
    No:of coins = 22
    Area : 467472.0


red_bc.jpg ->
    No:of coins = 53
    Area : 313799.0

cell_segmentation_02.jpg ->
    No:of coins = 27
    Area : 529421.5

bacteria.tiff->
    No:of coins = 22
    Area : 64878.0

WatershedSegmentation.png ->
    No:of coins = 35
    Area : 696395.5
'''
