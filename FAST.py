import cv2
import numpy as np

image = cv2.imread("images/butterfly.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Create the fast detector
fast = cv2.FastFeatureDetector()
kp = fast.detect(gray, None)
print("Number of key points", len(kp))

cv2.drawKeypoints(gray, kp, image)

cv2.imshow("Image with key points", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
