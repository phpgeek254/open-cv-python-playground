# It approximates a contour shape to another shape with less number of vertices depending
# upon the precision we specify.
import cv2
import numpy
import numpy as np

image = cv2.imread("images/house.png")
blank_image = np.zeros(image.shape)
image_2 = np.zeros(image.shape)
approx_contours = np.zeros(image.shape)
approx_contours_area = np.zeros(image.shape)
print("Image shapes => ", image.shape[0], image.shape[1], image.shape)
# Turn the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray, 50, 200)

# Find the contours
contours, _ = cv2.findContours(edges.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
print("Number of contours => ", len(contours))

# Loop through all the contours
for (i, contour) in enumerate(contours):
    area = cv2.contourArea(contour)
    # Get Contour Dimensions
    x, y, h, w = cv2.boundingRect(contour)
    # Get the centers
    # Draw the rects on the image
    cv2.rectangle(blank_image, (x, y), (w + w, h + y), 255, 2)
    if area > 1e4:
        print("Contour", i, area)
        cv2.rectangle(image_2, (x, y), (w + w, h + y), 255, 2)
        cv2.drawContours(image_2, contour, -1, (100, 100, 100), 1)

    # Approximating the contours
    accuracy = 0.03 * cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, accuracy, True)
    # Draw approximations on the image
    cv2.drawContours(approx_contours, [approx], 0, (0, 0, 255), 2)

    # Filter
    approx_area = cv2.contourArea(approx)
    if approx_area > 1e4:
        cv2.drawContours(approx_contours_area, [approx], 0, (0, 0, 255), 2)
    print("Approx Area", approx_area)

cv2.drawContours(blank_image, contours, -1, (0, 255, 0), 1)
result = np.concatenate([blank_image, image_2, approx_contours, approx_contours_area], axis=1)
cv2.imshow("Threshold image", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
