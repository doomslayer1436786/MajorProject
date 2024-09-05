from ultralytics import YOLO
import cv2


model = YOLO('.//model//drdetectionmodel.pt')

img = './/images//mild//16.jpg'
img2 = cv2.imread(img)

results = model('.//images//mild//15_left.jpeg',show=True)
cv2.waitKey(0)
