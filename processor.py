import cv2
import numpy as np
from Quartz import kCGEventMouseMoved


class Processor():
    def __init__(self, mouse):
        # add something later maybe
        self.mouse = mouse
        self.width = 0
        self.height = 0
        self.offset = 50
        self.centerx = 0
        self.centery = 0

    def start(self, img):
        self.height, self.width, _ = img.shape
        if img.shape[1]>500:
            img = self.resize(img)
        self.centerx, self.centery = self.width//2, self.height//2
        img = self.draw_crosshair(img)
        img = self.get_health_rects(img)
        img = self.get_health_centers(img)
        return img

    def draw_crosshair(self, img):
        cv2.circle(img, (self.centerx, self.centery+self.offset//2), 2, (255, 255, 0), -1)
        return img

    def resize(self, img):
        height, width, _ = img.shape
        self.width = width//2
        self.height = height//2
        img = cv2.resize(img, (self.width, self.height))
        return img

    def get_mask(self, img):
        # (235, 86, 86)
        lower = np.array([70, 70, 180], dtype='uint8')
        upper = np.array([130, 130, 250], dtype='uint8')

        mask = cv2.inRange(img, lower, upper)
        #output = cv2.bitwise_and(img, img, mask=mask)

        return mask

    def get_health_rects(self, img):

        mask = self.get_mask(img)
        contours = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]

        if len(contours) > 0:
            for contour in contours:
                if cv2.contourArea(contour)>30:
                    x, y, w, h = cv2.boundingRect(contour)
                    cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 1)
        return img

    def get_health_centers(self, img):
        mask = self.get_mask(img)
        contours = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
        centers = []

        if len(contours) > 0:
            for contour in contours:
                if cv2.contourArea(contour)>10:
                    x, y, w, h = cv2.boundingRect(contour)
                    targetx, targety = x+w//2, y+h
                    cv2.circle(img, (targetx, targety), 2, (0, 255, 0), -1)
                    self.mouse.moveTo(targetx, targety+self.offset)


        return img

