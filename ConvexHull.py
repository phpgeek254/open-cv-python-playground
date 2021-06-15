import numpy as np
import cv2

image = cv2.imread("images/shapes2.png")
convex_hull_image = np.zeros(image.shape)
contours_blank = np.zeros(image.shape)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray, 50, 200)

# Threshold the image
# ret, thresh = cv2.threshold(gray.copy(), 200, 255, 0)

contours, _ = cv2.findContours(edges.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
length = len(contours) - 1
sorted_contours = sorted(contours, key=cv2.contourArea, reverse=False)[: length]
print("Contours Found and sorted contours", len(contours), len(sorted_contours))

for (index, contour) in enumerate(sorted_contours):
    area = cv2.contourArea(contour)
    hull = cv2.convexHull(contour)
    cv2.drawContours(contours_blank, [contour], 0, (100, 100, 255), 2)
    cv2.drawContours(convex_hull_image, [hull], 0, 255, 2)
    print("Contour Area = ", area)

result = np.concatenate([contours_blank, convex_hull_image], axis=1)
# cv2.imshow("Gray Image", thresh)
cv2.imshow("Resultant images", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
