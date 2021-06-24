import cv2

video = cv2.VideoCapture("images/cars.avi")

# load the cars classifier
cars_classifier = cv2.CascadeClassifier("Haarcascades/haarcascade_car.xml")

while video.isOpened():
    _, frame = video.read()

    # Convert the colors
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cars = cars_classifier.detectMultiScale(gray, 1.3, 3)

    print("Number of cars detected ", len(cars))
    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (127, 0, 200), 2)
    cv2.imshow("Cars video", frame)
    if cv2.waitKey(1) == 13:
        break

video.release()
cv2.destroyAllWindows()
