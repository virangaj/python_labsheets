import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread(r'D:\3_1\python\assignment_9\halftone.png',0)

ft_img = np.fft.fft2(img)
fshift_img = np.fft.fftshift(ft_img)
ft_shift_img_abs = np.abs(fshift_img)

# log transform for better visibility
magnitude_spectrum_shifted = 20*np.log(np.abs(fshift_img))

# band reject - a mask containing 4 black circles
rows, cols = img.shape
mask = np.ones((rows, cols), np.uint8)
r = 25

center_1, center_2, center_3, center_4,center_5,center_6,center_7,center_8,center_9,center_10,center_11,center_12,center_13,center_14,center_15,center_16,center_17,center_18,center_19,center_20,center_21,center_22 = [65,94],[69,297],[65,487],[65,698],[132,191],[136,402],[132,601],[195,301],[200,500],[191,698],[263,191],[259,394],[271,592],[271,803],[330,310],[335,702],[398,200],[394,398],[398,605],[402,795],[461,293],[465,508]

x, y = np.ogrid[:rows, :cols]
mask_area_1 = (x - center_1[0]) ** 2 + (y - center_1[1]) ** 2 <= r*r
mask[mask_area_1] = 0
mask_area_2 = (x - center_2[0]) ** 2 + (y - center_2[1]) ** 2 <= r*r
mask[mask_area_2] = 0
mask_area_3 = (x - center_3[0]) ** 2 + (y - center_3[1]) ** 2 <= r*r
mask[mask_area_3] = 0
mask_area_4 = (x - center_4[0]) ** 2 + (y - center_4[1]) ** 2 <= r*r
mask[mask_area_4] = 0
mask_area_5 = (x - center_5[0]) ** 2 + (y - center_5[1]) ** 2 <= r*r
mask[mask_area_5] = 0
mask_area_6 = (x - center_6[0]) ** 2 + (y - center_6[1]) ** 2 <= r*r
mask[mask_area_6] = 0
mask_area_7 = (x - center_7[0]) ** 2 + (y - center_7[1]) ** 2 <= r*r
mask[mask_area_7] = 0
mask_area_8 = (x - center_8[0]) ** 2 + (y - center_8[1]) ** 2 <= r*r
mask[mask_area_8] = 0
mask_area_9 = (x - center_9[0]) ** 2 + (y - center_9[1]) ** 2 <= r*r
mask[mask_area_9] = 0
mask_area_10 = (x - center_10[0]) ** 2 + (y - center_10[1]) ** 2 <= r*r
mask[mask_area_10] = 0
mask_area_11 = (x - center_11[0]) ** 2 + (y - center_11[1]) ** 2 <= r*r
mask[mask_area_11] = 0
mask_area_12 = (x - center_12[0]) ** 2 + (y - center_12[1]) ** 2 <= r*r
mask[mask_area_12] = 0
mask_area_13 = (x - center_13[0]) ** 2 + (y - center_13[1]) ** 2 <= r*r
mask[mask_area_13] = 0
mask_area_14 = (x - center_14[0]) ** 2 + (y - center_14[1]) ** 2 <= r*r
mask[mask_area_14] = 0
mask_area_15 = (x - center_15[0]) ** 2 + (y - center_15[1]) ** 2 <= r*r
mask[mask_area_15] = 0
mask_area_16 = (x - center_16[0]) ** 2 + (y - center_16[1]) ** 2 <= r*r
mask[mask_area_16] = 0
mask_area_17 = (x - center_17[0]) ** 2 + (y - center_17[1]) ** 2 <= r*r
mask[mask_area_17] = 0
mask_area_18 = (x - center_18[0]) ** 2 + (y - center_18[1]) ** 2 <= r*r
mask[mask_area_18] = 0
mask_area_19 = (x - center_19[0]) ** 2 + (y - center_19[1]) ** 2 <= r*r
mask[mask_area_19] = 0
mask_area_20 = (x - center_20[0]) ** 2 + (y - center_20[1]) ** 2 <= r*r
mask[mask_area_20] = 0
mask_area_21 = (x - center_21[0]) ** 2 + (y - center_21[1]) ** 2 <= r*r
mask[mask_area_21] = 0
mask_area_22 = (x - center_22[0]) ** 2 + (y - center_22[1]) ** 2 <= r*r
mask[mask_area_22] = 0


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
