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


def render_text(text) -> None:
    textRender = store.font.render(text, True, store.WHITE)
    
    screen.blit(textRender,((store.width - textRender.get_width()) / 2,70))


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