import cv2


class Display():

    def __init__(self):
        pass

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
                cv2.imshow('img', img)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            cap.release()
            cv2.destroyAllWindows()


