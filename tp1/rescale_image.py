import pandas as pd
import cv2

def getImage(src, scaleRatio):
    image = cv2.imread(src)

    width = int(image.shape[1] * scaleRatio)
    height = int(image.shape[0] * scaleRatio)
    imageResized = cv2.resize(image, (width, height))
    
    return imageResized 
