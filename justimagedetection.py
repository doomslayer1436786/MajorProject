from ultralytics import YOLO
import cv2
import copyanddelete
import numpy as np

# Example usage:





model = YOLO('.//model//drdetectionmodel.pt')

img = './/images//mild//16.jpg'
img2 = cv2.imread(img)

results = model('.//images//mild//15_left.jpeg')

names = results[0].names
probs = results[0].probs

stageofdr = names[probs.top1]



#copyanddelete.copy_and_delete_folder()

cv2.waitKey(0)
