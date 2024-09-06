from ultralytics import YOLO
import cv2
import copyanddelete
import numpy as np



def processImage(image_path):
    model = YOLO('.//model//drdetectionmodel.pt')
    results = model(image_path,save=True)
    names = results[0].names
    probs = results[0].probs
    stageofdr = names[probs.top1]
    
    path = copyanddelete.copy_and_delete_folder()
    
    return path
    
    
  

    
    


# model = YOLO('.//model//drdetectionmodel.pt')

#img_path = './/images//mild//16.jpg'
#img2 = cv2.imread(img)

#results = model('.//images//mild//15_left.jpeg',save=True)


#copyanddelete.copy_and_delete_folder()

#processImage(img_path)