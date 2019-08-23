import time
import os
import cv2
from mss import mss
import numpy as np
import pyautogui
from Quartz import CGWindowListCopyWindowInfo, kCGNullWindowID, kCGWindowListOptionAll, CGWindowListCreateImage, CGRectMake, CGImageGetWidth, kCGWindowImageDefault, CGRectInfinite


windows = CGWindowListCopyWindowInfo(kCGWindowListOptionAll, kCGNullWindowID)

for window in windows:
    #print(window)
    try:
        if window['kCGWindowName'] == 'Krunker':
            print('Krunker window found!')
            print(window)

            # get window dimensions
            x = int(window['kCGWindowBounds']['X'])
            y = int(window['kCGWindowBounds']['Y'])
            width = int(window['kCGWindowBounds']['Width'])
            height = int(window['kCGWindowBounds']['Height'])
            print('Dimensions: {}'.format((x, y, width, height)))

            center = (width//2, height//2)
            print('Center: {}'.format(center))

            window_id = int(window['kCGWindowNumber'])
            print('Window ID: {}'.format(window_id))

            #region = CGRectMake(x, y, width, height)
            region = CGRectInfinite
            print('Region: {}'.format(region))

            img = CGWindowListCreateImage(region, kCGWindowListOptionAll, window_id, kCGWindowImageDefault)
            print('Test image width: {}'.format(CGImageGetWidth(img)))

            np_img = np.array(img)


            print(np_img)


    except:
        # handle exception
        pass


# main loop
while 1:
    break


cv2.destroyAllWindows()
