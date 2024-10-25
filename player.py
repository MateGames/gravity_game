import pygame
import storage

pygame.init()

store = storage.Storage()

class Player():
    def __init__(self,screen):
        self.friction = .2
        self.accel_rate = .2
        self.max_speed = 6
        self.speed = 0
        
        self.size = 50
        self.x =  store.width/2
        self.y = store.height/2
        
        self.rect = pygame.Rect((self.x,self.y),(self.size,self.size))
        
        self.screen = screen
        self.sprite = sprite_splitter(f'{store.phat}/src/car.png',40,8,8,8,6.25)
        self.limit = 0
        self.anime = 0
        
        self.flip = False
        self.lock = True
        
    
    def move(self):
        # horizontal   
        key = pygame.key.get_pressed()
        
        if key[pygame.K_RIGHT]:
            self.speed += self.accel_rate    
        if key[pygame.K_LEFT]:
            self.speed -= self.accel_rate
        
        if self.speed > self.max_speed: self.speed = self.max_speed
        if self.speed < -self.max_speed: self.speed = -self.max_speed

        if not (key[pygame.K_RIGHT] or key[pygame.K_LEFT]) and round(self.speed,1) != 0:
            if self.speed > 0:
                self.speed -= self.friction
            else:   
                self.speed += self.friction
                
        
        self.x += self.speed
        
        for line in group:
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
                    
                    for line in group:
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
                
                for line in group:
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
  