import cv2
import numpy
import numpy as np

image = cv2.imread("images/blobs2.jpeg")

detector = cv2.SimpleBlobDetector_create()
key_points = detector.detect(image)

print("Key points detected = ", len(key_points), key_points)

blank = np.zeros((10, 10))
blobs = cv2.drawKeypoints(image, key_points, blank, (255, 0, 0), cv2.DRAW_MATCHES_FLAGS_DEFAULT)

cv2.imshow("Blobs", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
