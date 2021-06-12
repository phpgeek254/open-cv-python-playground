import numpy as np

import cv2

cap = cv2.VideoCapture(0)


def blur_image(image):
    return cv2.GaussianBlur(image, (5, 5), 0)


def grayed_image(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def hsv_image(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2HSV)


def x_ray_image(image):
    gray_image = image.astype(np.float)/255
    # calculate the K Channel.
    k_channel = 1 - np.max(gray_image, axis=2)


def sketch_image(image):
    # image to gray
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
    edges = cv2.Canny(blurred_image, 30, 20)
    _, inverted_image = cv2.threshold(edges, 70, 255, cv2.THRESH_BINARY_INV)
    return inverted_image


while True:
    ret, frame = cap.read()
    cv2.imshow("Live Video", hsv_image(frame))
    if cv2.waitKey(1) == 13:
        break

cap.release()
cv2.destroyAllWindows()
