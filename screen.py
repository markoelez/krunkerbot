import time
import os
import cv2
from mss import mss
import numpy as np
import pyautogui
from Quartz import CGWindowListCopyWindowInfo, kCGNullWindowID, kCGWindowListOptionAll, CGWindowListCreateImage, CGRectMake, CGImageGetWidth, kCGWindowImageDefault, CGRectInfinite, CGImageGetDataProvider, CGImageGetHeight, CGDataProviderCopyData
from pngcanvas import PNGCanvas
import struct

def grabImage():
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
                #region = CGRectInfinite

                # get img data
                img = CGWindowListCreateImage(CGRectInfinite, kCGWindowListOptionAll, window_id, kCGWindowImageDefault)
                prov = CGImageGetDataProvider(img)
                img_data = CGDataProviderCopyData(prov)
                img_width, img_height = CGImageGetWidth(img), CGImageGetHeight(img)

                # create canvas based on image data pixels
                canvas = PNGCanvas(img_width, img_height)
                for x in range(img_width):
                    for y in range(img_height):
                        offset = 4 * ((img_width * int(round(y))) + int(round(x)))
                        b, g, r, a = struct.unpack_from('BBBB', img_data, offset=offset)
                        canvas.point(x, y, color=(r, g, b, a))

                # dump canvas to png
                with open('test.png', 'wb') as f:
                    f.write(canvas.dump())


        except:
            # handle exception
            pass

