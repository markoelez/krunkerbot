import cv2
import mss
import numpy as np
from display import Display


class Feed():

    def __init__(self, startOffset, width, height):
        self.sct = mss.mss()
        mon = self.sct.monitors[1]
        self.width, self.height = width, height
        self.offsetX, self.offsetY = startOffset
        self.startY = mon['top']
        self.startX = mon['left']

    def get_feed(self):
        top = self.startY+self.offsetY
        left = self.startX+self.offsetX
        img = np.array(self.sct.grab((top, left, left+self.width, top+self.height)))
        img = cv2.resize(img, (img.shape[1]//2, img.shape[0]//2))
        return img

if __name__ == '__main__':

    top = 20
    left = 20
    width = 400
    height = 400

    feed = Feed((top, left), width, height)
    disp = Display((200, 200), 400, 400)

    while 1:
        img = feed.get_feed()
        disp.paint(img)

        cv2.waitKey(0)
