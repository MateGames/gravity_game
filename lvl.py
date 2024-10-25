'''
make a class to store lvl data, it shoud be a general storge

lvl num
line/hitbox group: hitLine
finis and start pos:start,end

reset fucntion for storage
'''

'''
class HitLine():
    def __init__(self,start,end,type):
        if type not in ['horiz','vert']:
            raise ValueError('hitboxLine must be either "horiz" or "vert"')
        self.type = type # horiz, vert
        self.start = start
        self.end = end
        self.color = store.BLUE if self.type == 'horiz' else store.PURPLE
        
    def draw(self):
        if store.DEV:
            pygame.draw.line(screen,self.color,self.start,self.end,5)
        

        
self.group = []
self.group.append(HitLine((1250,200),(1250,500),'vert'))
self.group.append(HitLine((150,200),(150,500),'vert'))
self.group.append(HitLine((150,200),(1250,200),'horiz'))
self.group.append(HitLine((150,500),(1250,500),'horiz'))
'''