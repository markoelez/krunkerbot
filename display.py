import time
import cv2
import sdl2
import sdl2.ext


class Display():

    def __init__(self, position, width, height):
        sdl2.ext.init()
        self.window = sdl2.ext.Window('demo', size=(width, height), position=position)
        self.window.show()
        self.W, self.H = width, height

    def paint(self, img):
        events = sdl2.ext.get_events()
        for event in events:
            if event.type == sdl2.SDL_QUIT:
                exit(0)
        surf = sdl2.ext.pixels3d(self.window.get_surface())
        surf[:, :, 0:4] = img.swapaxes(0,1)
        self.window.refresh()

    def start(self, path, processor):
        if path.endswith(('.png', '.jpg')):
            img = cv2.imread(path)
            img = processor.start(img)
            cv2.imshow('img', img)

            cv2.waitKey(0)
            cv2.destroyAllWindows()

        elif path.endswith('.mp4'):
            cap = cv2.VideoCapture(path)
            while 1:
                ret, img = cap.read()
                img = processor.start(img)
                self.paint(img)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            cap.release()
            cv2.destroyAllWindows()

    def start_bot(self, processor, feed):
        while 1:
            img = feed.get_feed()
            # TODO -------------------------------
            #   get processor to work
            #   fix sizing (maybe make feed dynamic? detect krunker window and resize accordingly)
            #   test on krunker
            img = processor.resize(img)
            self.paint(img)


if __name__ == '__main__':
    disp = Display(1440, 900)
    cap = cv2.VideoCapture('demos/vid1.mp4')
    while 1:
        ret, img = cap.read()
        disp.paint(img)
