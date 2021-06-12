import cv2
import numpy as np

image = cv2.imread("paris.png")

# 1. Average Blurring
average_image = cv2.blur(image, (1, 3))
cv2.putText(average_image, "Average Blur (1 X 3", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, 255, 1)

# 2. Add A Gaussian Blur
g_image = cv2.GaussianBlur(image, (7, 7), 0)
cv2.putText(g_image, "gaussian Blur", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, 255, 1)

# 3. Median Blur
median_image = cv2.medianBlur(image, 5)
cv2.putText(median_image, "Median Blur", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, 255, 1)

# 4. Bilateral Blurring
bilateral_blur = cv2.bilateralFilter(image, 9, 75, 75)
cv2.putText(bilateral_blur, "Bilateral Blur", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, 255, 1)

# Combine the images here
combined_image = np.concatenate((image, g_image, median_image, bilateral_blur), axis=1)
# Show all the images
# Save the image
cv2.imwrite("blurring.png", combined_image)
cv2.imshow("Blurring Images", combined_image)
# House keeping
cv2.waitKey(0)
cv2.destroyAllWindows()
