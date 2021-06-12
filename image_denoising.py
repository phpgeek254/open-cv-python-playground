import cv2
import numpy as np

image = cv2.imread("paris.png")

# We have the following types of image denoising as provided by open cv
# 1. fastNlMeansDenoising -> works with gray scale images
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.putText(gray_image, "Gray scaled image", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, 255, 1)

fast_nl_means_denoised = cv2.fastNlMeansDenoising(gray_image, None, 5)
cv2.putText(fast_nl_means_denoised, "Fast NL Denoised", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, 255, 1)
# 2. fastNlMeansDenoisingMulti
# fastNlMeansDenoisingMulti = cv2.fastNlMeansDenoisingMulti((gray_image, fast_nl_means_denoised), 1, 501)
# cv2.putText(fastNlMeansDenoisingMulti, "fastNlMeansDenoisingMulti Denoised", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, 255,
#             1)
# Combining all the images


combined_image = np.concatenate((gray_image, fast_nl_means_denoised))

# Show the images
cv2.imshow("Denoising Images", combined_image)
# Save the image
cv2.imwrite("images/Denoising/1.png", combined_image)

# House keeping
cv2.waitKey(0)
cv2.destroyAllWindows()
