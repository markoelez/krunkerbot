import cv2
import numpy as np


class Processor():
    def __init__(self):
        # add something later maybe
        pass

    def start(self, img):
        if img.shape[1]>500:
            img = self.resize(img)
        (x, y, w, h) = self.get_health_rect(img)
        cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 1)
        return img

    def resize(self, img):
        height, width, _ = img.shape
        w = width//2
        h = height//2
        img = cv2.resize(img, (w, h))
        return img

    def get_health_rect(self, img):

        # (235, 86, 86)
        lower = np.array([50, 50, 210], dtype='uint8')
        upper = np.array([100, 100, 255], dtype='uint8')

        mask = cv2.inRange(img, lower, upper)
        #output = cv2.bitwise_and(img, img, mask=mask)

        contours = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]

        if len(contours) > 0:
            area = max(contours, key=cv2.contourArea)
            return(cv2.boundingRect(area))
