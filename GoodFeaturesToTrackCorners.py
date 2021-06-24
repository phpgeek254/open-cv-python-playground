import cv2
import numpy as np

image = cv2.imread("images/chess.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply the algorithm
corners = cv2.goodFeaturesToTrack(gray, 100, .01, 150)

print("Corners found => ", corners[0], len(corners))

# Loop through all the corners
for (index, corner) in enumerate(corners):
    x, y = corner[0].astype(int)
    print("Index, X, Y", index, x, y)
    cv2.rectangle(image, (x - 10, y - 10), (x + 10, y + 10), 255, 10)

cv2.imshow("Using all good features", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
