import numpy as np
import cv2

# img = cv2.imread('lena.jpg', 1)
img = np.zeros([512, 512, 3], np.uint8)
# Creating an image using numpy zeros method
# For black image, we have to give a list in the format:
# [height, width, 3]
# np.unit8 -> data type

img = cv2.line(img, (0, 0), (255, 255), (147, 96, 44), 10)
# line(image, starting coordinate of line in tuple form, ending coordinate of line in tuple form,
# colour in BGR format, thickness of line)
img = cv2.arrowedLine(img, (0, 255), (255, 255), (255, 0, 0), 10)

img = cv2.rectangle(img, (384, 0), (510, 128), (0, 0, 255), 10)
# rectangle(image, top left coordinate of rectangle, bottom right coordinate of rectangle,
# colour in BGR, thickness)
# If we give -1 as thickness, it will fill the rectangle with the colour specified
img = cv2.circle(img, (447, 63), 63, (0, 255, 0), -1)
# circle(image, coordinate of centre, radius, colour in BGR, thickness)
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, 'OpenCV', (10, 500), font, 4, (0, 255, 255), 10, cv2.LINE_AA)
# putText(image, text, starting coordinate for text, font, font size, colour in BGR, thickness, line type)

cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()