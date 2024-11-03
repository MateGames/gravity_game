import pygame
import storage
import player
import json
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
    def __init__(self,screen,name):
        with open(store.json, 'r') as f:
            data = json.load(f)
        data = data[name]
        
        self.text = data['text'] 
        self.number = data['number']
        self.start = data['start']
        self.end = data['end']
        self.screen = screen
        
        self.img = pygame.image.load(f'{store.phat}//src//img//lvl//lvl{self.number}.png')
        self.img = pygame.transform.scale(self.img,(store.width,store.height))
        
        self.hitLine = []
        for line in data['hitLine']:
            self.hitLine.append(HitLine(line[0],line[1],line[2]))    
        
        self.player = player.Player(self.screen,self.hitLine,self.start)
        
        
    def draw(self):
        if store.DEV:
            # start - end
            pygame.draw.rect(self.screen, store.RED, pygame.Rect(self.start,(50,50)), 1)
            pygame.draw.rect(self.screen, store.RED, pygame.Rect(self.end,(50,50)), 1)
            
            # hitLine
            for line in self.hitLine:
                pygame.draw.line(self.screen,store.BLUE if line.type == 'horiz' else store.PURPLE,line.start,line.end,4)
                
                
