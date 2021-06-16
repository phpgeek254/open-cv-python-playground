# Main function -> HoughLines ( thresholded image, accuracy, accuracy, threshold )
import cv2
import numpy as np

image = cv2.imread('images/soduku.png')

black_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
thresh = cv2.Canny(black_image, 127, 255, apertureSize=3)

lines = cv2.HoughLines(thresh, 1, np.pi / 180, 200)
print("Lines found => ", len(lines), lines[0])
# Loop through all the lines
for line in lines:
    rho, theta = line[0]
    a = np.cos(theta)
    b = np.sin(rho)

    x0 = a * rho
    y0 = b * theta

    x1 = int(x0 + 1000 * (-b))
    y1 = int(y0 + 1000 * a)
    x2 = int(x0 - 1000 * (-b))
    y2 = int(y0 - 1000 * a)
    # Draw the line on the image
    cv2.line(image, (x1, y1), (x2, y2), (0, 200, 100), 2)

cv2.imshow("Lines ", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
