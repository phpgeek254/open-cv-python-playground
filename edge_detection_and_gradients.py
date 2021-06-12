import cv2
import numpy as np

# Load the Image
image = cv2.imread("paris.png")
# Showing the original image
cv2.imshow("Original Image", image)

# Get image width and height
print("Image shape", image.shape)
# height, width = image.shape

# Extract sobel Edges
sobel_x = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=5)
sobel_y = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=5)

cv2.imshow("Sobel X Image", sobel_x)
cv2.imshow("Sobel Y Image", sobel_y)

# Sobel combination
sobel_combination = cv2.bitwise_or(sobel_x, sobel_y)
cv2.imshow("Sobel Combined Image", sobel_combination)

# Using laplacian method
laplacian = cv2.Laplacian(image, cv2.CV_64F)
cv2.imshow("Using laplacian Method", laplacian)

# Using canny Edge detection and gradient threshold
canny_image = cv2.Canny(image, 50, 120)
cv2.imshow("Using Canny", canny_image)


cv2.waitKey(0)
cv2.destroyAllWindows()
