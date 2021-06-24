import cv2

fc = cv2.CascadeClassifier("./Haarcascades/haarcascade_frontalface_default.xml")

image = cv2.imread("images/faces.png")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = fc.detectMultiScale(gray, 1.3, 5)

print("Found faces", len(faces))

cap = cv2.VideoCapture(0)

for (x, y, width, height) in faces:
    cv2.rectangle(image, (x, y), (x + width, y + height), (127, 0, 255), 2)

while True:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _faces = fc.detectMultiScale(gray, 1.3, 5)
    print("Faces on Video Cam", len(_faces))

    # Draw the faces on the frame
    for (x, y, width, height) in _faces:
        cv2.rectangle(frame, (x, y), (x + width, y + height), (127, 0, 255), 2)
    cv2.imshow("Video", frame)

    if cv2.waitKey(1) == 13:
        break

cap.release()
cv2.destroyAllWindows()
