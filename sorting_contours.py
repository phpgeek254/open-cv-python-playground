import cv2
import numpy as np

image = cv2.imread("images/shapes2.png")

# Create a blank image
blank_image = np.zeros((image.shape[0], image.shape[1], 3))

# Convert to Gray scale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Edge Detection
edges = cv2.Canny(gray_image, 50, 200)

# Find the contours
contours, hierarchy = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
# Draw the contours
# cons_image = cv2.drawContours(blank_image, contours, -1, (0, 255, 0), 1)

print("No. of contours detected", len(contours))
c_images = []
for (i, c) in enumerate(contours):
    cs = []
    area = cv2.contourArea(c)
    # get the centers for all the contours
    center = cv2.moments(c)
    (x, y, w, h) = cv2.boundingRect(c)
    cx = int(center['m10'] / center['m00'])
    cy = int(center['m01'] / center['m00'])
    image = cv2.drawContours(blank_image, [c], -1, (0, 255, 0), 1)
    cv2.putText(image, "Contour- {}".format(i), (int(cx - (w/4)), cy), cv2.FONT_HERSHEY_SIMPLEX, 1, 255, 1)
    cv2.putText(image, "Area - {}".format(area), (int(cx - (w/4)), cy + 40), cv2.FONT_HERSHEY_SIMPLEX, 1, 255, 1)
    print("=========================\n"
          "adding contour {} of {} \n"
          "center => ({}, {}) \n"
          "area => {}\n"
          "Width and height ({}, {}) \n"
          "========================== \n"
          "".format(i, len(contours), cx, cy, area, w, h)
          )
    c_images.append(image)

images = np.concatenate(c_images, axis=1)
# Show the image
cv2.imshow("Contours on a blank Image", blank_image)
# House keeping
cv2.waitKey(0)
cv2.destroyAllWindows()
