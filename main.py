import pygame
import os
import storage
import lvl
import player
pygame.init()


store = storage.Storage()

# screen
screen = pygame.display.set_mode((store.width,store.height))
pygame.display.set_caption("main")


palyer = player.Player(screen)



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


def render_text(text) -> None:
    textRender = pygame.font.render(text, True, store.WHITE)
    
    screen.blit(textRender,((store.width - textRender.get_width()) / 2,70))


class Hitbox():
    def __init__(self,start,end,type):
        self.type = type # horiz, vert
        self.start = start
        self.end = end
        self.color = store.BLUE if self.type == 'horiz' else store.PURPLE
        
    def draw(self):
        if store.DEV:
            pygame.draw.line(screen,self.color,self.start,self.end,5)
        
              

# make levl mechanic, test lvl ->
group = []
group.append(Hitbox((1250,200),(1250,500),'vert'))
group.append(Hitbox((150,200),(150,500),'vert'))
group.append(Hitbox((150,200),(1250,200),'horiz'))
group.append(Hitbox((150,500),(1250,500),'horiz'))


img = pygame.image.load(f'{store.phat}\\src\\map0.png')
img = pygame.transform.scale(img,(store.width,store.height))


def main():
    clock = pygame.time.Clock()

    run = True        
    while run:
        clock.tick(store.FPS) 
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        # key events
        key = pygame.key.get_pressed()
        if key[pygame.K_ESCAPE]:
            run = False 
            break
        
        screen.fill(store.BLACK)
        screen.blit(img,(0,0))
        
        render_text(
            'Use "A" and "D", or the arrow keys (<- ->), to move left and right.'
        )
                
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