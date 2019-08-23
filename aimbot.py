from processor import Processor
from display import Display


class Aimbot():
    def __init__(self, path='', isDemo=True):
        self.processor = Processor()
        self.isDemo = isDemo
        self.running = False

        # check if this is a demo or an actual game
        # if demo, create a display and begin running aimbot on demo file
        if self.isDemo:
            self.path = path
            self.display = Display()
        # otherwise, this is a game and initialize tracking variables
        else:
            self.enemies = []

    def start(self):
        if self.isDemo:
            self.running = True
            self.display.start(self.path, self.processor)
        else:
            # IMPLEMENT LATER
            pass

