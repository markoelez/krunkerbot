import time
import os
import cv2
from mss import mss
import numpy as np


def process_feed(bbox):
    sct = mss()
    while 1:
        screen = np.array(sct.grab(bbox))
        cv2.imshow('screen', screen)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

if __name__ == '__main__':
    #box = input('Enter dimens: ').split(',')
    #bbox = {'top': int(box[0]), 'left': int(box[1]), 'width': int(box[2]),
            #'height': int(box[3])}

    bbox={'top':100, 'left':20, 'width':500, 'height': 500}
    process_feed(bbox)
