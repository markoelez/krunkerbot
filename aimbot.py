from processor import Processor
from display import Display
from output import Mouse
from feed import Feed


class Aimbot():
    def __init__(self, path='', isDemo=True):
        self.processor = Processor(Mouse(0.03))
        self.isDemo = isDemo
        self.running = False

        # check if this is a demo or an actual game
        # if demo, create a display and begin running aimbot on demo file
        if self.isDemo:
            self.path = path
            self.display = Display((0, 0), 720, 450)
        # otherwise, this is a game and initialize tracking variables
        else:
            self.feed = Feed((0, 0), 800, 800)
            self.display = Display((900, 500), 400, 400)
            self.enemies = []

    def start(self):
        if self.isDemo:
            self.running = True
            self.display.start(self.path, self.processor)
        else:
            # IMPLEMENT LATER
            self.running = True
            self.display.start_bot(self.processor, self.feed)

