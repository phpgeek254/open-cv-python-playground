import cv2

image = cv2.imread("paris.png")

height, width = image.shape[:2]

# We need a start row and column and End row and end column
start_row, start_col = int(height * .25), int(width * .25)
end_row, end_col = int(height * .75), int(width * .75)

cropped_image = image[start_row:end_row, start_col:end_col]

# show original image
cv2.imshow("OR Image", image)
# Show cropped image
cv2.imshow("Cropped image", cropped_image)

# House keeping
cv2.waitKey(0)
cv2.destroyAllWindows()
