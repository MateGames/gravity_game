import pygame
import os
pygame.init()


# variables
width = 1400
height = 700
phat = __file__[:len(__file__)-len(os.path.basename(__file__))]
FPS = 60



# color
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (30,100,200)
PURPLE = (125, 31, 224)
RED = (200,50,50)


class Hitbox():
    def __init__(self,start,end,type):
        self.type = type # horiz, vert
        self.start = start
        self.end = end
        self.color = BLUE if self.type == 'horiz' else PURPLE
        
    def draw(self):
        pygame.draw.line(screen,self.color,self.start,self.end,5)
        
        
class Player():
    def __init__(self):
        self.friction = .2
        self.accel_rate = .2
        self.max_speed = 6
        self.speed = 0
        
        self.color = RED
        self.size = 50
        self.x =  width/2
        self.y = 500-self.size
        
        self.rect = pygame.Rect((self.x,self.y),(self.size,self.size))

    
    def move(self):
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
                self.speed = -self.speed*.2
        

        self.rect = pygame.Rect((self.x,self.y),(self.size,self.size))
        
            
    def draw(self):
        pygame.draw.rect(screen,self.color,self.rect,0)
        #print(round(self.speed,1),self.x)
                        

player = Player()

group = []
group.append(Hitbox((1250,200),(1250,500),'vert'))
group.append(Hitbox((150,200),(150,500),'vert'))
group.append(Hitbox((150,200),(1250,200),'horiz'))
group.append(Hitbox((150,500),(1250,500),'horiz'))


img = pygame.image.load(f'{phat}\\src\\map0.png')
img = pygame.transform.scale(img,(width,height))

# screen
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("main")


def main():
    clock = pygame.time.Clock()

    run = True        
    while run:
        clock.tick(FPS) 
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        # key events
        key = pygame.key.get_pressed()
        if key[pygame.K_ESCAPE]:
            run = False 
            break
        
        screen.fill(BLACK)
        screen.blit(img,(0,0))
        
        
        for object in group:
            object.draw()
            
        player.move()
        player.draw()
        
            
        print(pygame.mouse.get_pos())

        # pygame.display.flip()
        pygame.display.update()
    pygame.quit()
    quit()

if __name__ == '__main__':
    main()