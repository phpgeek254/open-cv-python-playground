import cv2
import numpy as np

# Original Image
image = cv2.imread('paris.png')
cv2.imshow('Original Image', image)

# Define a kernel
kernel = np.ones((5, 5), np.uint8)

# Apply the erosion
erosion = cv2.erode(image, kernel, iterations=1)
cv2.imshow("Eroded Image", erosion)

# Dilation
dilated_image = cv2.dilate(image, kernel, iterations=30)
cv2.imshow("Dilated Image", dilated_image)

# Opening -> Good for reducing noise in the image
opened_image = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
cv2.imshow("Morph Open", opened_image)

# Morph Closing the images -> Good for noise reduction on images.
morph_closed = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
cv2.imshow("Morph Closed", morph_closed)

cv2.waitKey(0)
cv2.destroyAllWindows()
