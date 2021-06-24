import cv2

pedestrian_classifier = cv2.CascadeClassifier("Haarcascades/haarcascade_fullbody.xml")

# Load some video file
cap = cv2.VideoCapture("images/walking.avi")

while cap.isOpened():
    _, frame = cap.read()

    image_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    bodies = pedestrian_classifier.detectMultiScale(image_gray, 1.2, 3)

    print("Number of bodies detected ", len(bodies))
    for (x, y, w, h) in bodies:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (127, 0, 255), 2)

    cv2.imshow("Walking Video", frame)
    if cv2.waitKey(1) == 13:
        break
cap.release()
cv2.destroyAllWindows()
