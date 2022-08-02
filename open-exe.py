import cv2
import numpy as np
import matplotlib.pyplot as plt

img_read = 'ColorChecker.png'
img_1 = cv2.imread(img_read, cv2.IMREAD_COLOR)


def readimage():
    img_1 = cv2.imread(img_read, cv2.IMREAD_COLOR)
    img_2 = cv2.cvtColor(img_1, cv2.COLOR_BGR2RGB)
    img_3 = cv2.cvtColor(img_1, cv2.COLOR_BGR2HSV)
    img_4 = cv2.applyColorMap(img_1, cv2.COLORMAP_BONE)
    cv2.imshow('main', np.hstack((img_1, img_2, img_4)))

    plt.figure(figsize=(6, 6), num="test_img")
    plt.subplot(3, 1, 1)
    plt.imshow(img_1, cmap='Blues')
    plt.xticks([]), plt.yticks([])

    plt.subplot(3, 1, 2)
    plt.imshow(img_2)
    plt.xticks([]), plt.yticks([])

    plt.subplot(3, 1, 3)
    plt.imshow(img_3)
    plt.xticks([]), plt.yticks([])
    plt.savefig('differe_color.png')
    plt.show()


def saveimg():
    img_1 = cv2.imread(img_read, cv2.IMREAD_COLOR)
    cv2.imwrite('test_gray.png', img_1)


def color_array():
    img_2 = cv2.cvtColor(img_1, cv2.COLOR_BGR2RGB)
    print(img_2.shape)  # row, col, channel
    print(img_2[:, :, 2])

    print(img_2.dtype)


readimage()
##saveimg()
##color_array()
