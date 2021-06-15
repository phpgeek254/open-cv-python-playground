import cv2


def image_to_gray(i):
    return cv2.cvtColor(i, cv2.COLOR_BGR2GRAY)


image = cv2.imread('images/image.png')
gray_image = image_to_gray(image)
print("Image shape", image.shape)
print("Gray Image shape", gray_image.shape)
# saving the images
# cv2.imwrite("color_copy.jpg", image)
# cv2.imwrite("gray_image.jpg", gray_image)
cv2.imshow("image", image)
cv2.imshow("Gray scale image", gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
