import cv2
import matplotlib.pyplot as plt
import numpy as np


FONT_SIZE = 8
COLOR = 'blue'

#read image
img = cv2.imread(r'S08_sample_images/square.jpg', 1)


#create kernel
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (21,21))

#cvt to gray
img_ = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


#binary image
ret, thresh = cv2.threshold(img_, 50,255,0)


#morphological
closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

img_r = cv2.cvtColor(closing, cv2.COLOR_GRAY2RGB)
img_2 = img_r.copy()

#detect contours
contours, hierarchy = cv2.findContours(closing, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)



print(len(contours))


#draw contour
img_c = cv2.drawContours(img_r, contours, -1, (0,255,0), 2)

#calculate area

area = cv2.contourArea(contours[0])
print(area)



position = (20,20)
text = 'Square primeter : '+str(area) + 'pixels'

cv2.putText(img_c, text, position, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,0,255), 2)




#calculate perimeter
perimeter = cv2.arcLength(contours[0], True)
perimeter = '{0:.2f}'.format(perimeter)
position1 = (20,195) #x,y
text1 = 'Square primeter : '+str(perimeter) + ' pixels'

print(perimeter)




#detect center

M = cv2.moments(contours[0])
cX = int(M["m10"] / M["m00"])
cY = int(M["m01"] / M["m00"])


img_d = img_c.copy()

cv2.circle(img_d, (cX, cY), 7, (255, 0, 0), -1)

#show image

plt.subplot(411)
plt.title('original', fontsize = FONT_SIZE, color=COLOR)
plt.imshow(img, 'gray')
plt.axis('off')



plt.subplot(412)
plt.title('remove circle', fontsize = FONT_SIZE, color=COLOR)
plt.imshow(img_2, 'gray')
plt.axis('off')




plt.subplot(413)
plt.text(20,195,text1, fontsize = FONT_SIZE, color=COLOR)
plt.title('Perimeter and area', fontsize = FONT_SIZE, color=COLOR)
plt.imshow(img_c, 'gray')
plt.axis('off')



plt.subplot(414)
plt.text(20,195,text1, fontsize = FONT_SIZE, color=COLOR)
plt.title('center of image', fontsize = FONT_SIZE, color=COLOR)
plt.imshow(img_d, 'gray')
plt.axis('off')
plt.show()



'''
#assngmnet

open cv contours
#cotour fetature moment
'''















