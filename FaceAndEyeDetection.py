import cv2
import numpy as np

face_classifier = cv2.CascadeClassifier('./Haarcascades/haarcascade_frontalface_default.xml')
eye_classifier = cv2.CascadeClassifier('./Haarcascades/haarcascade_eye.xml')

image = cv2.imread("images/faces.png")
print("Image", image, face_classifier, eye_classifier)

# cv2.imshow("Face and Eye detection", image)
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# faces = face_classifier.detectMultiScale(gray, 1.3, 5)
#
# print("Faces count detected", len(faces))
#
# for (x, y, width, height) in faces:
#     # Draw a rectangle around the faces
#     cv2.rectangle(image, (x, y), (x + width, y + height), (127, 0, 255), 2)

# cv2.imshow("Face and Eye detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
