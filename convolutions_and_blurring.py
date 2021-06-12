import cv2
import numpy as np

image = cv2.imread("paris.png")

kernel = np.ones((3, 3,), np.float32) / 9
blurred_image = cv2.filter2D(image, -2, kernel)
cv2.putText(blurred_image, "Blurred 3X3 Kernel", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, 255)

kernel_7x7 = np.ones((7, 7,), np.float32) / 7**2
blurred_7 = cv2.filter2D(image, -1, kernel_7x7)
cv2.putText(blurred_7, "7X7 Kernel", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, 255, 1)

# Combine all the images
combined = np.concatenate((image, blurred_image, blurred_7), axis=1)
cv2.imshow("Blurring", combined)
# House keeping
cv2.waitKey(0)
cv2.destroyAllWindows()
