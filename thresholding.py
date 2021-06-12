import cv2
import numpy as np

image = cv2.imread("paris.png")
# Show the original image
cv2.imshow("Ori Image", image)
ret, thresh_bin = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
cv2.imshow("Binary thresh 1", thresh_bin)

# Inverse threshold
_, thresh_inv = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("Binary threshold 2 inverse", thresh_inv)

# Thresh trunc -> TODO: Find out what this means.
_, thresh_trunc = cv2.threshold(image, 127, 255, cv2.THRESH_TRUNC)
cv2.imshow("Thresh trunc image", thresh_trunc)

# Thresh to zero
_, thresh_to_zero = cv2.threshold(image, 127, 255, cv2.THRESH_TOZERO)
cv2.imshow('Thresh to zero', thresh_to_zero)

# Thresh to zero inverse -> TODO: Find out what this means
_, thresh_to_zero_inv = cv2.threshold(image, 127, 255, cv2.THRESH_TOZERO_INV)
cv2.imshow("Thresh to zero inverse", thresh_to_zero_inv)


cv2.waitKey(0)
cv2.destroyAllWindows()
