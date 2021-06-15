import cv2
import numpy as np

# Define the template and the target
target = cv2.imread("images/shape_detection.png", 0)
template = cv2.imread("images/shapes2.png", 0)

blank_target = np.zeros(target.shape)

target_thresh = cv2.Canny(target, 50, 255)
template_thresh = cv2.Canny(template, 127, 255)

template_contours, _ = cv2.findContours(template_thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

print("Template contours found", len(template_contours))

search_shape = template_contours[1]
cv2.imshow("Template", template)

target_contours, _ = cv2.findContours(target_thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
# Draw the contours on the blank image

print("Target contours found", len(target_contours))
# Loop the target contours
match = None
for (index, contour) in enumerate(target_contours):
    match = cv2.matchShapes(search_shape, contour, 3, 0.0)
    print("match for contour => ", match)
    if match > 1:
        cv2.drawContours(blank_target, [contour], -1, (100, 100, 244), 1)

cv2.imshow("Target Image", blank_target)
cv2.waitKey(0)
cv2.destroyAllWindows()
