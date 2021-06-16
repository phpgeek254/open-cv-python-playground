import cv2
import numpy as np

image = cv2.imread("images/soduku.png")
black = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(black, 127, 255, apertureSize=3)

lines = cv2.HoughLinesP(canny, 1, np.pi / 180, 200)
print("Lines found", len(lines))

for (index, line) in enumerate(lines):
    for x1, y1, x2, y2 in line:
        cv2.line(image, (x1, y1), (x2, y2), (100, 100, 100), 3)

cv2.imshow("Probabilistic Hough Lines", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
