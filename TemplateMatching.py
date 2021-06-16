import cv2
import numpy as np

image = cv2.imread("images/WaldoBeach.jpg")
# Grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

template = cv2.imread("images/waldo.jpg", 0)  # Loaded in gray scale
width, height = template.shape

print("template image shape", template.shape)
result = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF)

min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
print("MinVAL, MaxVAL, MinLOC, MaxLOC", min_val, max_val, min_loc, max_loc)

top_left = max_loc
bottom_right = (top_left[0] + width, top_left[1] + height)

# Draw the rectangle to show the position of the matched image
cv2.rectangle(image, top_left, bottom_right, 255, 6)
cv2.imshow("Woldos position", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
