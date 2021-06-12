import cv2
import numpy as np

# Making a square
square = np.zeros((300, 300), dtype='uint8')
cv2.rectangle(square, (50, 50), (250, 250), 255, -2)
# ellipse
ellipse = np.zeros((300, 300), dtype='uint8')
cv2.ellipse(ellipse, (150, 150), (150, 150), 45, 0, 180, 255, -1)
# AND OPERATION
and_image = cv2.bitwise_and(square, ellipse)
cv2.putText(and_image, "BITWISE AND", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, 255, 2)
# Bitwise OR Image
or_image = cv2.bitwise_or(square, ellipse)
cv2.putText(or_image, "BITWISE OR", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, 255, 2)
# Bitwise XOR
xor_image = cv2.bitwise_xor(square, ellipse)
cv2.putText(xor_image, "BITWISE XOR", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, 255, 2)
# Bitwise not image
not_image = cv2.bitwise_not(square, ellipse)
cv2.putText(not_image, "BITWISE NOT", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

# Concatenate all the figures to one image
all_images = np.concatenate((square, ellipse, and_image, or_image, xor_image, not_image), axis=1)
# Show all the images
cv2.imshow("All Images", all_images)
# House keeping
cv2.waitKey(0)
cv2.destroyAllWindows()