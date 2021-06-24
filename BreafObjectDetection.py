import cv2
import numpy as np

image = cv2.imread("images/butterfly.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

detector = cv2.FastFeatureDetector_create(threshold=500)

print("Check out the detector", detector)

cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
#
# detector = cv2.FastFeatureDetector("BRIEF")
#
# kp = detector.detect(gray)
# kps, desc = detector.compute(gray, keypoints=kp)
#
# print("Number of key points detected", kps)
