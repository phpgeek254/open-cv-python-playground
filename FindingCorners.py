import cv2
import numpy as np

image = cv2.imread("images/chess.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# cornerHarris uses float32 data type
gray = np.float32(gray)

corners = cv2.cornerHarris(gray, 3, 3, .05)

# use a kernel for dilation
kernel = np.ones((7, 7))
corners = cv2.dilate(corners, kernel, iterations=2)
image_copy = image.copy()
image[corners > .025 * corners.max()] = [255, 127, 127]

# Combining the image
result = np.concatenate([image, image_copy], axis=1)
cv2.imshow("Corners ", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
