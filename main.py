import pygame
import os
import storage
import menu

import lvl
pygame.init()


store = storage.Storage()
menu = menu.Menu(store)


# screen
screen = pygame.display.set_mode((store.width,store.height))
pygame.display.set_caption("main")
icon = pygame.image.load(f'{store.phat}//src//img//icon.png')
pygame.display.set_icon(icon)


level = lvl.Lvl(screen,'lvl2')
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
        
        



        if menu.active_menu == "main":
            menu.handle_main_menu_events(event)
        elif menu.active_menu == "levels":
            menu.handle_level_menu_events(event)

        # Draw the active menu
        if menu.active_menu == "main":
            menu.draw_main_menu()
        elif menu.active_menu == "levels":
            menu.draw_level_menu()


        if menu.selected_level and menu.active_menu is None:
            print(f"Loading {menu.selected_level}...")
            run = False


        '''
        screen.fill(store.BLACK)
        screen.blit(level.img,(0,0))
        
        level.draw()
        store.render_text(screen,level.text,60,store.WHITE)
        store.render_text(screen,f'LVL:{level.number+1}',660,store.WHITE)
        
        player.finish(level.end)
        player.move()
        player.draw()
        
        '''
            
        #print(pygame.mouse.get_pos())

        # pygame.display.flip()
        pygame.display.update()
    pygame.quit()
    quit()

if __name__ == '__main__':
    main()