import time
import os
import cv2
from mss import mss
import numpy as np
import pyautogui
from Quartz import CGWindowListCopyWindowInfo, kCGNullWindowID, kCGWindowListOptionAll


bbox = {'top': 100, 'left': 20, 'width': 500, 'height': 500}

windows = CGWindowListCopyWindowInfo(kCGWindowListOptionAll, kCGNullWindowID)

for window in windows:
    #print(window)
    try:
        name = window['kCGWindowName']
        if name == 'Krunker':
            print('Krunker window found!')
            # get window dimensions
            x = int(window['kCGWindowBounds']['X'])
            y = int(window['kCGWindowBounds']['Y'])
            width = int(window['kCGWindowBounds']['Width'])
            height = int(window['kCGWindowBounds']['Height'])

            center = (width//2, height//2)
            print(center)


    except:
        # handle exception
        pass


# main loop
while 1:
    break


cv2.destroyAllWindows()
