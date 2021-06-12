import cv2

image = cv2.imread("paris.png")
scaled_image = cv2.resize(image, None, fx=.75, fy=.75)  # Maintaining the aspect ratio

doubled_size = cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
cv2.imshow("Or Image", image)
cv2.imshow("Scaled Image", scaled_image)
cv2.imshow("Doubled Size", doubled_size)
# House keeping
cv2.waitKey(0)
cv2.destroyAllWindows()
