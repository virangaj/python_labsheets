import cv2

img_read = 'ColorCheck.png'
img = cv2.imread(img_read, cv2.IMREAD_COLOR)
cv2.imshow(img)
cv2.destroyAllWindow()