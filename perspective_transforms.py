import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread("paris.png")
# Show the original image
cv2.imshow("Original Image", image)

print("Image shape", image.shape)

points_A = np.float32([
    [320, 15],
    [600, 215],
    [85, 610],
    [350, 620],
])

points_B = np.float32([
    [0, 0],
    [350, 0],
    [0, 594],
    [350, 594],
])

M = cv2.getPerspectiveTransform(points_A, points_B)
warped = cv2.perspectiveTransform(image, M, (350, 600))

# Display the warped image
cv2.imshow("Warped Image", warped)
# House keeping after the process is complete.
cv2.waitKey(0)
cv2.destroyAllWindows()
