import cv2

face_classifier = cv2.CascadeClassifier('./Haarcascades/haarcascade_frontalface_default.xml')
eye_classifier = cv2.CascadeClassifier('./Haarcascades/haarcascade_eye.xml')

image = cv2.imread("images/faces.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = face_classifier.detectMultiScale(gray, 1.3, 5)

print("Number of images detected", len(faces))
eyes_count = 0
for (x, y, width, height) in faces:
    cv2.rectangle(image, (x, y), (x + width, y + height), (127, 0, 255), 2)

    # Detect eyes -> Define the region of interest
    roi_gray = gray[y: y + height, x:x + width]
    roi_color = image[y:y + height, x:x + width]

    eyes = eye_classifier.detectMultiScale(roi_gray)
    eyes_count += len(eyes)

    # Draw the eyes
    for (ex, ey, e_width, e_height) in eyes:
        cv2.rectangle(roi_color, (ex, ey), (ex + e_width, ey + e_height), (100, 100, 255), 2)

print("Eye count", eyes_count)
cv2.imshow("Faces Image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
