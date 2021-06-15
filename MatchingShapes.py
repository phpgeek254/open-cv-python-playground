import cv2
import numpy as np

# Define the template and the target
template = cv2.imread("shapes_3.png.png")
target = cv2.imread("images/shapes.png")

cv2.imshow("Template and target", template)

cv2.waitKey(0)
cv2.destroyAllWindows()
