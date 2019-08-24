import time
import pyautogui
from Quartz.CoreGraphics import CGEventCreateMouseEvent
from Quartz.CoreGraphics import CGEventPost
from Quartz.CoreGraphics import kCGEventMouseMoved
from Quartz.CoreGraphics import kCGEventLeftMouseDown
from Quartz.CoreGraphics import kCGEventLeftMouseUp
from Quartz.CoreGraphics import kCGMouseButtonLeft
from Quartz.CoreGraphics import kCGHIDEventTap


class Mouse:

    def __init__(self, duration):
        self.duration= duration

    def moveTo(self, x, y):
        pyautogui.moveTo(x, y, self.duration)

    def click(self, x, y):
        pyautogui.click(x=x, y=y, clicks=1, interval=0.05, button='left')

def mouseEvent(type, posx, posy):
    event = CGEventCreateMouseEvent(None, type, (posx, posy), kCGMouseButtonLeft)
    CGEventPost(kCGHIDEventTap, event)

def mousemove(posx, posy):
    mouseEvent(kCGEventMouseMoved, posx, posy)

def mouse(x, y):
    pyautogui.moveTo(x, y, 0.0001)

if __name__ == '__main__':
    mouse = Mouse(0.08)

    mouse.moveTo(200, 200)
    mouse.moveTo(300, 300)
    mouse.moveTo(4, 4)
