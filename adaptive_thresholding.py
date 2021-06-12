import cv2
import numpy as np

# Load the image
image = cv2.imread("paris.png")
# Original Image
cv2.imshow("Original Image", image)

_, thresh_1 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
cv2.imshow("Binary Image", thresh_1)

# Blur the Image
blurred_image = cv2.GaussianBlur(image, (7, 7), 0)

# Using adaptive thresholding
threshold = cv2.adaptiveThreshold(blurred_image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 21, 10)
cv2.imshow("Adaptive mean threshold", threshold)

cv2.waitKey(0)
cv2.destroyAllWindows()
