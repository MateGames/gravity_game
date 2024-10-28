import pygame
import storage

pygame.init()

store = storage.Storage()


def sprite_splitter(sprite:str, wid:int, hig:int, box_wid:int, box_hig:int, size:float) -> list:
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



class Player():
    def __init__(self,screen,hitLine,spawn):
        self.friction = .2
        self.accel_rate = .2
        self.max_speed = 6
        self.speed = 0
        
        self.size = 50
        self.x =  spawn[0]
        self.y = spawn[1]
        
        self.rect = pygame.Rect((self.x,self.y),(self.size,self.size))
        
        self.screen = screen
        self.sprite = sprite_splitter(f'{store.phat}/src/car.png',40,8,8,8,6.25)
        self.limit = 0
        self.anime = 0
        self.hitLine = hitLine
        
        self.flip = False
        self.lock = True
        
    
    def move(self):
        # horizontal   
        key = pygame.key.get_pressed()
        
        if key[pygame.K_d] or key[pygame.K_RIGHT]:
            self.speed += self.accel_rate    
        if key[pygame.K_a] or key[pygame.K_LEFT]:
            self.speed -= self.accel_rate


        if self.speed > self.max_speed: self.speed = self.max_speed
        if self.speed < -self.max_speed: self.speed = -self.max_speed

        if not (key[pygame.K_RIGHT] or key[pygame.K_LEFT] or key[pygame.K_d] or key[pygame.K_a]) and round(self.speed,1) != 0:
            if self.speed > 0:
                self.speed -= self.friction
            else:   
                self.speed += self.friction
                
        
        self.x += self.speed
        
        for line in self.hitLine:
            if line.type == 'vert' and self.rect.clipline(line.start, line.end):
                self.x -= self.speed*2
                self.speed = -self.speed*.5
        
        
        #vertical
        if key[pygame.K_SPACE] == False:
            self.lock = True

        if key[pygame.K_SPACE] and self.lock:
            self.flip = not self.flip
            self.lock = False

 
        if self.flip:
                while True:
                    limit = False
                    self.y -= 1
                    self.rect = pygame.Rect((self.x,self.y),(self.size,self.size))
                    
                    for line in self.hitLine:
                        if line.type == 'horiz' and self.rect.clipline(line.start, line.end):
                            self.y += 1
                            limit = True
                            break
                    
                    if limit:
                        break
            
        else:
            while True:
                limit = False
                self.y += 1
                self.rect = pygame.Rect((self.x,self.y),(self.size,self.size))
                
                for line in self.hitLine:
                    if line.type == 'horiz' and self.rect.clipline(line.start, line.end):
                        self.y -= 1
                        limit = True
                        break
                
                if limit:
                    break
                
            
            self.rect = pygame.Rect((self.x,self.y),(self.size,self.size))
                
            
    def draw(self):
        self.limit += 1
        if self.limit == 8:
            self.anime += 1
            self.limit = 0
        
        if self.anime == 5:
            self.anime = 0
        
        sprite = self.sprite[self.anime]
        if self.flip:
            sprite = pygame.transform.flip(self.sprite[self.anime], False, True).convert_alpha()
        
        if self.speed < 0:
            sprite = pygame.transform.flip(sprite, True, False).convert_alpha()
            self.screen.blit(sprite,(self.x,self.y))
        else:
            self.screen.blit(sprite,(self.x,self.y))
  