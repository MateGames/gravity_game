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


def render_text(text) -> None:
    textRender = store.font.render(text, True, store.WHITE)
    
    screen.blit(textRender,((store.width - textRender.get_width()) / 2,70))


img = pygame.image.load(f'{store.phat}//src//map0.png')
img = pygame.transform.scale(img,(store.width,store.height))


group = []
group.append(lvl.HitLine((1250,200),(1250,500),'vert'))
group.append(lvl.HitLine((150,200),(150,500),'vert'))
group.append(lvl.HitLine((150,200),(1250,200),'horiz'))
group.append(lvl.HitLine((150,500),(1250,500),'horiz'))

lvle = lvl.Lvl(1,group,(200,450),(1200,450))
player = player.Player(screen,group,(200,450))


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
                
        lvle.draw(screen)
            
        player.move()
        player.draw()
        
        
            
        #print(pygame.mouse.get_pos())

        # pygame.display.flip()
        pygame.display.update()
    pygame.quit()
    quit()

if __name__ == '__main__':
    main()