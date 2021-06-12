import cv2
import numpy
from matplotlib import pyplot as plt

cap = cv2.VideoCapture(0)
image = cv2.imread('paris.png')
hist = cv2.calcHist([image], [0], None, [256], [0, 256])
plt.hist(image.ravel(), 256, [0, 256])
plt.show()

color = ('b', 'g', 'r')
for i, col in enumerate(color):
    print("Index and color", i, col)
    hist1 = cv2.calcHist([image], [i], None, [256], [0, 256])
    plt.plot(hist1, color=col)
    plt.xlim([0, 256])

plt.show()
# while True:
#     _, frame = cap.read()
#     cv2.imshow("Video Image", frame)
#     # hist = cv2.calcHist([frame], [0], None, [256], [0, 256])
#     # plt.hist(frame.ravel(), 256, [0, 256]); plt.show()
#
#     if cv2.waitKey(1) == 3:
#         break
#
# cv2.destroyAllWindows()
