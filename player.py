import pygame
import storage

pygame.init()

store = storage.Storage()

class Player():
    def __init__(self,screen,hitLine,spawn):
        self.friction = .8
        self.accel_rate = .4
        self.max_speed = 12
        self.speed = 0
        
        self.size = 50
        self.x =  spawn[0]
        self.y = spawn[1]
        
        self.rect = pygame.Rect((self.x,self.y),(self.size,self.size))
        
        self.screen = screen
        self.sprite = store.sprite_splitter(f'{store.phat}//src//img//car.png',40,8,8,8,6.25)
        self.limit = 0
        self.anime = 0
        self.hitLine = hitLine
        
        self.flip = False
        self.lock = True
        self.cd = 0
        
    
    def move(self):
        # horizontal   
        key = pygame.key.get_pressed()
        
        if key[pygame.K_d] or key[pygame.K_RIGHT]:
            self.speed += self.accel_rate    
        if key[pygame.K_a] or key[pygame.K_LEFT]:
            self.speed -= self.accel_rate


        if self.speed > self.max_speed: self.speed = self.max_speed
        if self.speed < -self.max_speed: self.speed = -self.max_speed

        self.speed = round(self.speed,1)
        print(self.speed)
        if not (key[pygame.K_RIGHT] or key[pygame.K_LEFT] or key[pygame.K_d] or key[pygame.K_a]) and self.speed != 0:
            if self.speed > 0:
                self.speed -= self.friction
            else:   
                self.speed += self.friction

            if self.speed < self.friction and self.speed > 0:
                self.speed = 0
            if self.speed > -self.friction and self.speed < 0:
                self.speed = 0
                
        
        self.x += self.speed
        self.rect = pygame.Rect((self.x,self.y),(self.size,self.size))
        
        for line in self.hitLine:
            if line.type == 'vert' and self.rect.clipline(line.start, line.end):
                self.x -= self.speed
                self.speed = round(-self.speed*.5,1)
        
        
        #vertical
        if key[pygame.K_SPACE] == False:
            self.lock = True

        if self.cd > 0: self.cd -= 1
        if key[pygame.K_SPACE] and self.lock and self.cd == 0:
            self.cd = 30
            self.flip = not self.flip
            self.lock = False
 

        while True:
            limit = False
            self.y -= 1 if self.flip else -1
            self.rect = pygame.Rect((self.x,self.y),(self.size,self.size))
            
            for line in self.hitLine:
                if line.type == 'horiz' and self.rect.clipline(line.start, line.end):
                    self.y += 1 if self.flip else -1
                    limit = True
                    break
            
            if limit:
                break
            
        self.rect = pygame.Rect((self.x,self.y),(self.size,self.size))
    
    
    def finish(self,pos):
        finish = pygame.Rect(pos,(50,50))   
        if self.rect.colliderect(finish):
            return True
        else:
            return False
           
            
    def draw(self):
        self.limit += 1
        if self.limit == 3:
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
        
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] and self.lock and not self.cd == 0:
            store.render_text(self.screen,f"You can't switch gravity yet!",300,store.RED)
            
    class animation():
        def __init__(self, ):
            ...