import cv2
import numpy as np

image = np.zeros((512, 512, 3), np.uint8)
# Draw line
cv2.line(image, (0, 0), (511, 511), (255, 127, 0), 5)

# Draw a rectangle
cv2.rectangle(image, (20, 20), (400, 200), (0, 0, 255), 3)
cv2.rectangle(image, (300, 200), (200, 400), (0, 225, 255), -1)
cv2.circle(image, (200, 200), 100, (255, 245, 0), 1)

# Adding poly lines
points = np.array([[10, 10], [10, 400], [300, 400]])
cv2.polylines(image, [points], True, (0, 200, 200), 4)

# Add Text
cv2.putText(image, "Hello World", (75, 300), cv2.FONT_HERSHEY_TRIPLEX, 2, (255, 255, 255), 5)
cv2.imshow("Color image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
