import pygame
from pathlib import Path

class Storage():
    def __init__(self):
        # variables
        self.width = 1400
        self.height = 700
        self.phat = Path(__file__).parent
        self.FPS = 30
        self.font = pygame.font.Font(f'{self.phat}//font//Mateo-Regular.ttf', 40)
        self.json = f'{self.phat}//src//lvlData.json'
        self.DEV = True

        # color
        self.WHITE = (255,255,255)
        self.BLACK = (0,0,0)
        self.BLUE = (30,100,200)
        self.PURPLE = (125, 31, 224)
        self.RED = (200,50,50)


    def render_text(self,screen,text,y,color) -> None:
        textRender = self.font.render(text, True, color)
        
        screen.blit(textRender,((self.width - textRender.get_width()) / 2,y))
        
        
    def sprite_splitter(self,sprite:str, wid:int, hig:int, box_wid:int, box_hig:int, size:float) -> list:
        '''
        Splits a sprite sheet into a matrix of smaller images.
        Returns a list of images or a matrix based on the sheet's height.
        '''
        
        # Scale the width and height by the size factor
        wid *= size; hig *= size
        box_wid *= size; box_hig *= size

        # Load and scale the sprite image
        sprite = pygame.image.load(sprite)
        sprite = pygame.transform.scale(sprite, (wid, hig))
        
        # Split the sprite into smaller images
        mapp = []
        for i in range(int(hig / box_hig)):
            mapp.append([])
            for j in range(int(wid / box_wid)):
                img = pygame.Surface((box_wid, box_hig)).convert_alpha()
                img.blit(sprite, (0, 0), ((j * box_wid), (i * box_hig), box_wid, box_hig))
                img.set_colorkey((0,0,0))
                mapp[i].append(img)

        # Return a flat list if there's only one row, otherwise return the full matrix
        return mapp[0] if hig == box_hig else mapp

  
'''
taile ratio = 16 : 28, 168px : 98px
tile = 1 : 1, 8px : 8px
'''

