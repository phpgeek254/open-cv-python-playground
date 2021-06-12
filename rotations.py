import cv2
import numpy as np

image = cv2.imread("paris.png")

height, width = image.shape[:2]

# Method 1 -> create a rotation matrix
rotation_matrix = cv2.getRotationMatrix2D((width / 2, height / 2), 90, 1)


# Method 2 -> transpose the image
transposed_image = cv2.transpose(image)
rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))

# One could also flit the image
flipped_image = cv2.flip(image, 0)
# Show Image
cv2.imshow("Original Image", image)
cv2.imshow("Rotated Image", rotated_image)
cv2.imshow("Transposed Image", transposed_image)
cv2.imshow("Flipped Image", flipped_image)

# House Keeping
cv2.waitKey(0)
cv2.destroyAllWindows()
