import cv2
import numpy as np
import matplotlib.pyplot as plt



# Q1
img_1 = cv2.imread(r'circle.png', cv2.IMREAD_GRAYSCALE)

h = np.ones((5,5), np.float32)/25

plt.title('Original')
plt.imshow(img_1, cmap='Greys_r')
plt.axis('off')

#plt.show()


# Q2

mean_img_1 = cv2.filter2D(img_1, -1, h)

plt.subplot(231)
plt.title('Original')
plt.imshow(img_1, cmap='Greys_r')
plt.axis('off')

plt.subplot(232)
plt.title('Filtered')
plt.imshow(mean_img_1, cmap='Greys_r')
plt.axis('off')

plt.subplot(233)
plt.title('jet')
plt.imshow(mean_img_1, 'jet')
plt.axis('off')



plt.subplot(234)
plt.title('pink')
plt.imshow(mean_img_1, 'pink')
plt.axis('off')


plt.subplot(235)
plt.title('hot')
plt.imshow(mean_img_1, 'hot')
plt.axis('off')

#plt.show()


# Q3
h_15 = np.ones((15,15), np.float32)/(15*15)

mean_img_2 = cv2.filter2D(img_1, -1, h_15)


plt.subplot(131)
plt.title('Original')
plt.imshow(img_1, cmap='Greys_r')
plt.axis('off')

plt.subplot(132)
plt.title('Filtered 5')
plt.imshow(mean_img_1, cmap='Greys_r')
plt.axis('off')

plt.subplot(133)
plt.title('Filtered 15')
plt.imshow(mean_img_2, cmap='Greys_r')
plt.axis('off')

#plt.show()



# Q4

median_img = cv2.medianBlur(img_1, 5)



plt.subplot(131)
plt.title('Original')
plt.imshow(img_1, cmap='Greys_r')
plt.axis('off')

plt.subplot(132)
plt.title('Mean')
plt.imshow(mean_img_1, cmap='Greys_r')
plt.axis('off')

plt.subplot(133)
plt.title('Median')
plt.imshow(median_img, cmap='Greys_r')
plt.axis('off')

#plt.show()


# Q5

median_img_1 = cv2.medianBlur(img_1, 7)
median_img_2 = cv2.medianBlur(img_1, 13)
median_img_3 = cv2.medianBlur(img_1, 15)
median_img_4 = cv2.medianBlur(img_1, 21)


images = [img_1, median_img, median_img_1, median_img_2, median_img_3, median_img_4]
title = ['original', 'median 5', 'median 7', 'median 13', 'median 15', 'median 21']


for i in range(len(images)):
    plt.subplot(2,3,i+1)
    plt.title(title[i])
    plt.imshow(images[i],cmap='Greys_r')
    plt.axis('off')

plt.show()
















