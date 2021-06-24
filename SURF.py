# This stands for Speed Up robust Features
# The most valuable property of an interest point detector is its repeatability, i.e. whether it
# reliably finds the same interest points under different viewing conditions

import cv2
import numpy as np

image = cv2.imread("images/butterfly.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Create a SURF Feature detector
surf = cv2.ORB_create()

kp, desc = surf.detectAndCompute(gray, None)

print("Length of kp and desc", len(kp), kp, desc)

cv2.drawKeypoints(gray, kp, image)
cv2.imshow("Image with key points", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
