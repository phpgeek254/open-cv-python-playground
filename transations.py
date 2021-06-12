import cv2
import numpy as np

image = cv2.imread("paris.png")

cv2.imshow("Original Image", image)

# get image width and height
height, width = image.shape[:2]

q_height, q_width = height * .25, width * .25

# create the translation matrix
#       |1 0 Tx|
# T =   |0 1 Ty|
TranslationMatrix = np.float32([
    [1, 0, q_width],
    [0, 1, q_height]
])

translated_image = cv2.warpAffine(image, TranslationMatrix, (width, height))
# Show the Image
cv2.imshow("Translated Image", translated_image)

# House keeping
cv2.waitKey(0)
cv2.destroyAllWindows()
