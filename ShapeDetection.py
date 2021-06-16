import cv2

image = cv2.imread("images/shapes_d.png")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Get the thresholds
thresh = cv2.Canny(gray_image, 200, 255)

# Get the contours
contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
print("Contours found", len(contours))

# Get approximate polygons -> in a loop
for (index, contour) in enumerate(contours):
    # The cv2 function used to approximate the number of sides in a contour
    poly_count = cv2.approxPolyDP(contour, .01 * cv2.arcLength(contour, True), True)
    # Compute the centers of the contour
    x, y, h, w = cv2.boundingRect(contour)
    center = cv2.moments(contour)
    cx = int(center['m10'] / center['m00']) - int(w / 4)
    cy = int(center['m01'] / center['m00']) - int(w / 4)
    print("Index {} -> polygon count -> {}", index, len(poly_count))

    # Calculate the dimensions

    cv2.putText(image, "{}".format(index), (cx, cy + 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0))

    if len(poly_count) == 3:
        shape_name = "Triangle"
        cv2.putText(image, shape_name, (cx, cy), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0))
    if len(poly_count) == 4:
        if w / h == 1:
            shape_name = "Square"
            cv2.putText(image, shape_name, (cx, cy), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 1, 0), 1)
        else:
            shape_name = "Rectangle"
            cv2.putText(image, shape_name, (cx, cy), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 100, 0), 1)
    if len(poly_count) > 20:
        shape_name = "Circle"
        cv2.putText(image, shape_name, (cx, cy), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 100, 0), 1)

cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
