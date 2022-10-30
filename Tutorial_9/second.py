import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread(r'D:\3_1\python\assignment_9\noiseball.png',0)

ft_img = np.fft.fft2(img)
fshift_img = np.fft.fftshift(ft_img)
ft_shift_img_abs = np.abs(fshift_img)

# log transform for better visibility
magnitude_spectrum_shifted = 20*np.log(np.abs(fshift_img))

# band reject - a mask containing 4 black circles
rows, cols = img.shape
mask = np.ones((rows, cols), np.uint8)
r = 15

center_1, center_2, center_3, center_4 = [78,135], [78,169], [179,150], [180,185]

x, y = np.ogrid[:rows, :cols]
mask_area_1 = (x - center_1[0]) ** 2 + (y - center_1[1]) ** 2 <= r*r
mask[mask_area_1] = 0
mask_area_2 = (x - center_2[0]) ** 2 + (y - center_2[1]) ** 2 <= r*r
mask[mask_area_2] = 0
mask_area_3 = (x - center_3[0]) ** 2 + (y - center_3[1]) ** 2 <= r*r
mask[mask_area_3] = 0
mask_area_4 = (x - center_4[0]) ** 2 + (y - center_4[1]) ** 2 <= r*r
mask[mask_area_4] = 0


fshift_and_mask = fshift_img*mask
ft_shift_with_mask = np.abs(fshift_and_mask)

f_ishift = np.fft.ifftshift(fshift_and_mask)
img_back = np.fft.ifft2(f_ishift)
img_back = np.abs(img_back)


plt.subplot(411)
plt.title('Gray Image')
plt.axis('off')
plt.imshow(img,'gray')

plt.subplot(412)
plt.title('FT Magnitude Spectrum\nShifted to centre')
plt.axis('off')
plt.imshow(magnitude_spectrum_shifted,'gray')

plt.subplot(413)
plt.title('mask')
plt.axis('off')
plt.imshow(mask[:,:],'gray')


plt.subplot(414)
plt.title('Image back to spatial domain')
plt.axis('off')
plt.imshow(img_back,'gray')

plt.show()


plt.subplot(121)
plt.title('original image')
plt.axis('off')
plt.imshow(img,'gray')

plt.subplot(122)
plt.title('img - patterned noise removed')
plt.axis('off')
plt.imshow(img_back,'gray')
plt.show()
