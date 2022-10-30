import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread(r'97.jpg', 0)
cv2.imshow("97", img)
img = cv2.imread(r'97_1.jpg', 0)
cv2.imshow("97_1", img)
img = cv2.imread(r'97_2.jpg', 0)
cv2.imshow("97_2", img)


ft_img = np.fft.fft2(img)
fshift_img = np.fft.fftshift(ft_img)
ft_shift_img_abs = np.abs(fshift_img)

# log transform for better visibility
magnitude_spectrum_shifted = 20*np.log(np.abs(fshift_img))

# high pass - a circled mask
rows, cols = img.shape
crow, ccol = int(rows / 2), int(cols / 2)
mask = np.zeros((rows, cols), np.uint8)
r = 25
center = [crow, ccol]
x, y = np.ogrid[:rows, :cols]
mask_area = (x - center[0]) ** 2 + (y - center[1]) ** 2 <= r*r
mask[mask_area] = 1

fshift_and_mask = fshift_img*mask
ft_shift_with_mask = np.abs(fshift_and_mask)

f_ishift = np.fft.ifftshift(fshift_and_mask)
img_back = np.fft.ifft2(f_ishift)
img_back = np.abs(img_back)


plt.subplot(411)
plt.title('Gray Image')
plt.axis('off')
plt.imshow(img, 'gray')

plt.subplot(412)
plt.title('FT Magnitude Spectrum\nShifted to centre')
plt.axis('off')
plt.imshow(magnitude_spectrum_shifted, 'gray')

plt.subplot(413)
plt.title('mask')
plt.axis('off')
plt.imshow(mask[:, :], 'gray')


plt.subplot(414)
plt.title('Image back to spatial domain')
plt.axis('off')
plt.imshow(img_back, cmap='gray')

plt.show()

cv2.waitKey(-1)
cv2.destroyAllWindows()
