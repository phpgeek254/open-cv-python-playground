import cv2
import numpy as np

image = cv2.imread('image.png')
cap = cv2.VideoCapture(0)
print("Image details shape", image.shape, image[20, 30].shape)


# The HSV Color space
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Getting the individual color spaces.
while True:
    _, frame = cap.read()
    mask = np.zeros(frame.shape[:2], dtype="uint8")
    B, G, R = cv2.split(frame)
    print("Frame shape", frame.shape)
    red_image = cv2.merge([mask, mask, R])
    green_image = cv2.merge([mask, G, mask])
    blue_image = cv2.merge([B, mask, mask])
    cv2.imshow("Color spaces", frame)
    cv2.imshow("red space", blue_image)
    # cv2.imshow("green spaces", cv2.merge(mask?))
    if cv2.waitKey(1) == 13:

        break
cv2.destroyAllWindows()
