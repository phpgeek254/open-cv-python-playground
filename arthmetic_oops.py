import numpy as np
import cv2

# Adding matrices to an image has an effect on its brightness values
image = cv2.imread("paris.png")

M = np.ones(image.shape, dtype="uint8") * 100

added_image = cv2.add(image, M)
subtracted = cv2.subtract(image, M)

# Output all the images
cv2.imshow("OR Image", image)
cv2.imshow("Added Image", added_image)
cv2.imshow('Subtracted Image', subtracted)

# House keeping
cv2.waitKey(0)
cv2.destroyAllWindows()
