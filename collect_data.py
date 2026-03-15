import cv2
import os

label = "F"   # change this to B or C later
dataset_path = f"dataset/{label}"

cap = cv2.VideoCapture(0)

count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow("Collecting Data", frame)

    key = cv2.waitKey(1)

    if key == ord('s'):   # press S to save image
        img_name = f"{dataset_path}/{count}.jpg"
        cv2.imwrite(img_name, frame)
        print("Saved", img_name)
        count += 1

    if key == ord('q'):   # press Q to quit
        break

cap.release()
cv2.destroyAllWindows()