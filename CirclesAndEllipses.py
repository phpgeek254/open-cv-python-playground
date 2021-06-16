import cv2
import numpy as np

image = cv2.imread("images/blobs.jpg", 0)

detector = cv2.SimpleBlobDetector_create()
key_points = detector.detect(image)

blank = np.zeros((1, 1))
blobs = cv2.drawKeypoints(image, key_points, blank, (0, 255, 0), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

blob_count = len(key_points)

print("Blobs created = ", blob_count)

params = cv2.SimpleBlobDetector_Params()
params.filterByArea = True
params.minArea = 100

# Circularity Parameters.
params.filterByCircularity = True
params.minCircularity = .9

# Convexity Parameters
params.filterByConvexity = False
params.minConvexity = .2

# Inertia Parameters
params.filterByInertia = True
params.minInertiaRatio = .01

# Detector with parameters
detector_1 = cv2.SimpleBlobDetector_create(params)
key_points_1 = detector_1.detect(image)
circular_blobs_count = len(key_points_1)

blank_2 = np.zeros((1, 1))
blobs_2 = cv2.drawKeypoints(image, key_points_1, blank_2, 255, cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# Add Text
cv2.putText(blobs, "All Blobs {}".format(blob_count), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, 255, 1)
cv2.putText(blobs_2, "Circular Blobs {}".format(circular_blobs_count), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, 255, 1)
all_blobs = np.concatenate([blobs, blobs_2], axis=1)
# Display image with blob key points
cv2.imshow("Blobs using default parameters", all_blobs)
cv2.waitKey(0)
