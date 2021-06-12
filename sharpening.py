import cv2
import numpy as np

image = cv2.imread("paris.png")
cv2.imshow("Original Image", image)
kernel = np.array([
    [-1, -1, -1],
    [-1, 12, -1],
    [-1, -1, -1]
])
sharpened_image = cv2.filter2D(image, -1, kernel)
cv2.imshow("Sharpened Image", sharpened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
