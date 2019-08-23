import time
import os
import cv2
from mss import mss
import numpy as np
import pyautogui
from Quartz import CGWindowListCopyWindowInfo, kCGNullWindowID, kCGWindowListOptionAll


bbox = {'top': 100, 'left': 20, 'width': 500, 'height': 500}


while 1:

    # main loop

    windows = CGWindowListCopyWindowInfo(kCGWindowListOptionAll, kCGNullWindowID)

    time.sleep(0.2)

    for window in windows:
        try:
            name = window['kCGWindowName']
            if name == 'Krunker':
                print('success!')
                print(str(int(window.valueForKey_('kCGWindowBounds'))))
            print(window['Krunker'])
        except:
            # handle exception
            pass
    break


cv2.destroyAllWindows()
