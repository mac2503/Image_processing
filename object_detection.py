import cv2
import numpy as np

def nothing(x):
    pass

cap = cv2.VideoCapture(0)

cv2.namedWindow("Tracking")
# Trackbar for Lower Hue (LH)
# (trackbar name, window name, starting value, ending value, callback function)
cv2.createTrackbar("LH", "Tracking", 0, 255, nothing)
# LS -> Lower Saturation
cv2.createTrackbar("LS", "Tracking", 0, 255, nothing)
# LV -> Lower Value
cv2.createTrackbar("LV", "Tracking", 0, 255, nothing)
# UH -> Upper Hue
cv2.createTrackbar("UH", "Tracking", 255, 255, nothing)
# US -> Upper Saturation
cv2.createTrackbar("US", "Tracking", 255, 255, nothing)
# UV -> Upper Value
cv2.createTrackbar("UV", "Tracking", 255, 255, nothing)

while True:
    # frame = cv2.imread('smarties.png')
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    l_h = cv2.getTrackbarPos("LH", "Tracking")
    l_s = cv2.getTrackbarPos("LS", "Tracking")
    l_v = cv2.getTrackbarPos("LV", "Tracking")

    u_h = cv2.getTrackbarPos("UH", "Tracking")
    u_s = cv2.getTrackbarPos("US", "Tracking")
    u_v = cv2.getTrackbarPos("UV", "Tracking")

    # Lower limit for blue color for hsv image
    # For blue, l_b -> 80, 50, 50, u_b -> 130, 255, 255
    l_b = np.array([l_h, l_s, l_v])
    u_b = np.array([u_h, u_s, u_v])
    mask = cv2.inRange(hsv, l_b, u_b)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("res", res)
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()