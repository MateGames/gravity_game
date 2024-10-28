import pygame
import storage
pygame.init()

store = storage.Storage()


class HitLine():
    def __init__(self,start,end,type):
        if type not in ['horiz','vert']:
            raise ValueError('hitboxLine must be either "horiz" or "vert"')
        self.type = type # horiz, vert
        self.start = start
        self.end = end
        self.color = store.BLUE if self.type == 'horiz' else store.PURPLE




class Lvl():
    def __init__(self,number,hitLine,start,end):
        self.numbe = number
        self.hitLine = hitLine
        self.start = start
        self.end = end
        
    def draw(self,screen):
        if store.DEV:
            # start - end
            pygame.draw.rect(screen, store.RED, pygame.Rect(self.start,(50,50)), 1)
            pygame.draw.rect(screen, store.RED, pygame.Rect(self.end,(50,50)), 1)
            
            # hitLine
            for line in self.hitLine:
                pygame.draw.line(screen,store.BLUE if line.type == 'horiz' else store.PURPLE,line.start,line.end,4)