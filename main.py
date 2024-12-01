import pygame
import os
import storage
import menu
import lvl
import sys
pygame.init()


store = storage.Storage()
menu = menu.Menu(store)


# screen
screen = pygame.display.set_mode((store.width,store.height))
pygame.display.set_caption("main")
icon = pygame.image.load(f'{store.phat}//src//img//icon.png')
pygame.display.set_icon(icon)
 
 
 
 
def main(): 
    clock = pygame.time.Clock()
    active = False
    ob = False

    run = True        
    while run:
        clock.tick(store.FPS) 
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        # key events
        key = pygame.key.get_pressed()
        if key[pygame.K_ESCAPE] and store.DEV:
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



        if menu.selected_level and menu.active_menu is None and not active:
            if int(menu.selected_level[-1:])+1 >= 5:
                store.render_text(screen,'level work in progress!',120,store.RED)
                menu.active_menu = "levels"
                menu.selected_level = None
                active = False
            else:
                level = lvl.Lvl(screen,menu.selected_level)
                player = level.player
                try:
                    object =  level.object
                    ob = True
                except: 
                    ob = False
                    #print('No ob!')
                active = True
                #print(f"Loading {menu.selected_level}...")
            
        print(pygame.time.get_ticks() / 1000
)
        if active and menu.active_menu is None:
            screen.fill(store.BLACK)
            
            level.draw(screen)
            store.render_text(screen,level.text,60,store.WHITE)
            store.render_text(screen,f'LVL:{level.number+1}',660,store.WHITE)
            
            if player.finish(level.end):
                menu.active_menu = "levels"
                menu.selected_level = None
                active = False
                
            player.move()
            
            try:
                if object:
                    if object.button_rect.colliderect(player.rect):
                        if not object.action:
                            player.hitLine.pop()
                            player.hitLine.pop()
                        object.is_pressd()
                    
                    object.draw(screen)
            except: pass
                
            player.draw()

        #print(pygame.mouse.get_pos())

        pygame.display.flip()
        pygame.display.update()

    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()