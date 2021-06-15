import cv2
import numpy as np

image = cv2.imread("images/shapes.png")

# Convert to gray scale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray_image, 30, 200)

# Find the contours
contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

cv2.drawContours(image, contours, -1, (0, 255, 0), 3)

cv2.imshow("Contours", image)

# House keeping
cv2.waitKey(0)
cv2.destroyAllWindows()
