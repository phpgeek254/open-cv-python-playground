import cv2

# Import the cascade classifiers
face_classifier = cv2.CascadeClassifier("./Haarcascades/haarcascade_frontalface_default.xml")
eye_classifier = cv2.CascadeClassifier("./Haarcascades/haarcascade_eye.xml")


def detect_faces_and_eyes(frame):
    face_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(face_gray, 1.3, 5)

    # Draw a rectangle on the face
    for (x, y, f_width, f_height) in faces:
        cv2.rectangle(frame, (x, y), (x + f_width, y + f_height), (127, 0, 100), 2)

        # Detect the eyes
        roi_gray = face_gray[y: y + f_height, x: x + f_width]
        roi_color = frame[y: y + f_height, x: x + f_width]

        eyes = eye_classifier.detectMultiScale(roi_gray, 1.3, 5)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (127, 0, 255), 2)
    return frame


cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    cv2.imshow("Face Detection", detect_faces_and_eyes(frame))
    if cv2.waitKey(1) == 13:
        break

cap.release()
cv2.destroyAllWindows()
