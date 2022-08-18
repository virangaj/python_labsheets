import numpy as np
import cv2
import matplotlib.pyplot as plt

#Q1
img_1 = cv2.imread(r'circle.png',1)
plt.imshow(img_1)
plt.axis('off')
plt.show()

h = np.ones((5,5), np.float32)/25

#Q2
mean_img_1 = cv2.filter2D(img_1,-1,h)

plt.subplot(121)
plt.axis('off')
plt.title('Original')
plt.imshow(img_1)
plt.subplot(122)
plt.axis('off')
plt.title('Mean')
plt.imshow(mean_img_1)
plt.show()

#Q3
h2 = np.ones((15,15), np.float32)/225

mean_img_2 = cv2.filter2D(img_1,-1,h2)

plt.subplot(131)
plt.axis('off')
plt.title('Original')
plt.imshow(img_1)
plt.subplot(132)
plt.axis('off')
plt.title('Mean 5')
plt.imshow(mean_img_1)
plt.subplot(133)
plt.axis('off')
plt.title('Mean 15')
plt.imshow(mean_img_2)
plt.show()

#Q4
m_blur = cv2.medianBlur(img_1,5)

plt.subplot(131)
plt.axis('off')
plt.title('Original')
plt.imshow(img_1)
plt.subplot(132)
plt.axis('off')
plt.title('Mean 5')
plt.imshow(mean_img_1)
plt.subplot(133)
plt.axis('off')
plt.title('Median 5')
plt.imshow(m_blur)
plt.show()

#Q5
m_blur2 = cv2.medianBlur(img_1,11)

plt.subplot(131)
plt.axis('off')
plt.title('Original')
plt.imshow(img_1)
plt.subplot(132)
plt.axis('off')
plt.title('Median 5')
plt.imshow(m_blur)
plt.subplot(133)
plt.axis('off')
plt.title('Median 11')
plt.imshow(m_blur2)
plt.show()
