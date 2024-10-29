import pygame
import os
import storage
import lvl
pygame.init()



store = storage.Storage()
# screen
screen = pygame.display.set_mode((store.width,store.height))
pygame.display.set_caption("main")


def render_text(text,y) -> None:
    textRender = store.font.render(text, True, store.WHITE)
    
    screen.blit(textRender,((store.width - textRender.get_width()) / 2,y))


level = lvl.Lvl(screen,'lvl1')
player = level.player


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
        screen.blit(level.img,(0,0))
        
        level.draw()
        render_text(level.text,70)
        render_text(f'LVL:{level.number+1}',650)
        
        player.move()
        player.draw()
        
        
            
        #print(pygame.mouse.get_pos())

        # pygame.display.flip()
        pygame.display.update()
    pygame.quit()
    quit()

if __name__ == '__main__':
    main()