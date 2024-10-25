from pygame import font
from pathlib import Path

class Storage():
    def __init__(self):
        # variables
        self.width = 1400
        self.height = 700
        self.phat = Path(__file__).parent
        self.FPS = 60
        self.font = font.Font(f'{self.phat}\\font\\Mateo-Regular.ttf', 40)
        self.DEV = False


        # color
        self.WHITE = (255,255,255)
        self.BLACK = (0,0,0)
        self.BLUE = (30,100,200)
        self.PURPLE = (125, 31, 224)
        self.RED = (200,50,50)