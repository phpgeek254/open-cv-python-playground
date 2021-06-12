import cv2
image = cv2.imread("paris.png")

small_image = cv2.pyrDown(image)
larger_image = cv2.pyrUp(image)

print("Image sizes or {}, small image {}, large image {}".format(image.shape, small_image.shape, larger_image.shape))

cv2.imshow("OR Image", image)
cv2.imshow("Smaller Image", small_image)
cv2.imshow("Larger Image -> PyrUp", larger_image)

cv2.waitKey(0)
cv2.destroyAllWindows()