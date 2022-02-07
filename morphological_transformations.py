# Morphological transformations are simple operations based on the image shape
# They are normally performed on binary images
# To perform morphological transformations, there are 2 things that are required:
# 1. Original image
# 2. Structuring element/kernel which decides the natures of the operation

import cv2
import numpy as np
from matplotlib import pyplot as plt

# Reading image in grayscale mode
img = cv2.imread('j.jpg', cv2.IMREAD_GRAYSCALE)
mask = img
# _, mask = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV)

# kernel of size 5X5
kernel = np.ones((5, 5), np.uint8)

# To remove black spots from white ball areas in mask image
# (source, kernel, no. of iterations (default = 1))
# kernel -> It is a square/ shape which we want to apply on the image
dilation = cv2.dilate(mask, kernel, iterations=2)
# Erosion erodes away the boundary of the foreground object
erosion = cv2.erode(mask, kernel, iterations=1)
# (source, type of morphological operation, kernel)
# Opening is basically erosion followed by dilation
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
# Closing is dilation followed by erosion
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
# mg -> morphological gradient: It is difference between the dilation & erosion of an image
mg = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernel)
# th -> top hat: Difference between the image & the opening of the image
th = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernel)

titles = ['image', 'mask', 'dilation', 'erosion', 'opening', 'closing', 'mg', 'th']
images = [img, mask, dilation, erosion, opening, closing, mg, th]

for i in range(8):
    plt.subplot(2, 4, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
