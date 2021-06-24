import cv2
import numpy as np

image = cv2.imread("images/input.JPG")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

sift = cv2.SIFT_create()
key_points = sift.detect(gray, None)
print("Number of key points", len(key_points))

image = cv2.drawKeypoints(gray, key_points, outImage=image, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imshow("OR Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
