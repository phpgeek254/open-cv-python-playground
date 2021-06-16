# Circle Detection - Hough circles
#
# **cv2.HoughCircles**(image, method, dp, MinDist, param1, param2, minRadius, MaxRadius)
#
#
# - Method - currently only cv2.HOUGH_GRADIENT available - dp - Inverse ratio of accumulator resolution - MinDist -
# the minimum distance between the center of detected circles - param1 - Gradient value used in the edge detection -
# param2 - Accumulator threshold for the HOUGH_GRADIENT method (lower allows more circles to be detected (false
# positives)) - minRadius - limits the smallest circle to this size (via radius)
# - MaxRadius - similarly sets the limit for the largest circles
import cv2
import cv2 as cv
import numpy as np

image = cv.imread("images/circles4.png")
black = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
k_size = 7  # this number has to be odd and less than 5
canny = cv.GaussianBlur(black, (k_size, k_size), 0)

# get the circles
circles = cv.HoughCircles(image=canny, method=cv.HOUGH_GRADIENT, dp=1.5, minDist=10, param1=100, param2=100,
                          minRadius=25)

circles = np.uint16(np.around(circles))
print("number of circles found =", len(circles[0]))

for circle in circles[0, :]:
    cx = circle[0]
    cy = circle[1]
    radius = circle[2]
    cv2.circle(image, (cx, cy), 2, (255, 0, 100), 5)
    cv2.circle(image, (circle[0], circle[1]), circle[2], 255, 2)
    print("Radius = ", radius)

cv2.imshow("Circles Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
