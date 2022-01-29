import numpy as np
import cv2 as cv

img = cv.imread('smarties.png')
output = img.copy()
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Creating a blur image as Hough circle transform works better with a blur image
# medianBlur(image, kernel size)
gray = cv.medianBlur(gray, 5)

# HoughCircles(image, method, dp, minDist, param1, param2, minRadius, maxRadius)
# method -> Detection method, currently only HOUGH_GRADIENT is available as the option
# dp -> Inverse ratio of accumulator resolution to the image resolution
# minDist -> Minimum distance between the centers of the detected circles
# param1 -> Higher threshold of the 2 passed to the Canny edge detector
# param2 -> Accumulator threshold for the circle centers at the detection stage
# minRadius -> Minimum circle radius
# maxRadius -> Maximum circle radius. If it is <= 0, it uses the max image dimension. If it is < 0, it returns centers without finding the radius
circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=0, maxRadius=0)
# It will return a circle vector
# We need to convert the circle parameters into an integer first
detected_circles = np.uint16(np.around(circles))
for (x, y, r) in detected_circles[0, :]:
    cv.circle(output, (x, y), r, (0, 255, 0), 3)
    cv.circle(output, (x, y), 2, (0, 255, 255), 3)

cv.imshow('output', output)
cv.waitKey(0)
cv.destroyAllWindows()

# Representation of a circle using an equation:
# (x-x_center)^2+(y-y_center)^2 = r^2
# (x_center, y_center) -> center of the circle
# r -> radius of the circle