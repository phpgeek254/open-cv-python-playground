# Essentially, this is opposite of blurring.

import cv2
import numpy as np

image = cv2.imread("paris.png")

# Create a kernel -> make sure the sum of the elements in the kernel add up to 1
kernel = np.array([
    [-1, -1, -1],
    [-1, 9, -1],
    [-1, -1, -1]
])
# The 9 in the middle reduces the sum to 1

sharpened_image = cv2.filter2D(image, -1, kernel)
cv2.putText(sharpened_image, "Sharpened Image", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, 255, 1)

# Combine the images
combined_image = np.concatenate((image, sharpened_image))

# Show the images
cv2.imshow("Image Sharpening", combined_image)
cv2.imwrite("images/sharpening/sharpening.png", combined_image)

# House keeping
cv2.waitKey()
cv2.destroyAllWindows()
