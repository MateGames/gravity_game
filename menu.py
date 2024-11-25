import pygame
import webbrowser
from storage import Storage

class Menu:
    def __init__(self, storage):
        self.storage = storage
        self.screen = pygame.display.set_mode((self.storage.width, self.storage.height))
        pygame.display.set_caption("Game Menu")
        self.active_menu = "main"  # "main", "levels", or None (in-game)
        self.selected_level = None  # Tracks the selected level
        self.level_count = 9
        self.github = False
        self.background_main = pygame.image.load(f"{self.storage.phat}//src//img//main_menu.png")
        self.background_main = pygame.transform.scale(self.background_main, (self.storage.width, self.storage.height))
        self.background_lvl = pygame.image.load(f"{self.storage.phat}//src//img//lvl_select.png")
        self.background_lvl = pygame.transform.scale(self.background_lvl, (self.storage.width, self.storage.height))

    def draw_button(self, text, rect, color):
        """
        Render a button with text centered inside its clickable area.
        """
        #pygame.draw.rect(self.screen, color, rect, 0)  # Draw button background
        if self.storage.DEV:
            pygame.draw.rect(self.screen, self.storage.RED, rect, 2)  # Draw boundary in DEV mode

        # Render text in the center of the button
        text_render = self.storage.font.render(text, True, self.storage.WHITE)
        text_x = rect.x + (rect.width - text_render.get_width()) // 2
        text_y = rect.y + (rect.height - text_render.get_height()) // 2
        self.screen.blit(text_render, (text_x, text_y))

    def handle_main_menu_events(self, event):
        """
        Handle events for the main menu.
        """
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            button_width, button_height = 300, 60
            right_x = self.storage.width - button_width - 50

            # Play button
            if right_x <= x <= right_x + button_width and 200 <= y <= 200 + button_height:
                self.active_menu = "levels"
                
            # GitHub button
            elif right_x <= x <= right_x + button_width and 300 <= y <= 300 + button_height:
                if not self.github:
                    webbrowser.open("https://github.com/MateGames/gravity_game")
                    self.github = True
            
            # Quit button
            elif right_x <= x <= right_x + button_width and 400 <= y <= 400 + button_height:
                pygame.quit()
                raise SystemExit
            
        # reset git_b
        if event.type == pygame.MOUSEBUTTONUP:
            self.github = False

            
    def draw_main_menu(self):
        """
        Draw the main menu screen.
        """
        self.screen.blit(self.background_main, (0, 0))
        self.storage.render_text(self.screen, "Main Menu", 50, self.storage.WHITE)

        # Right-aligned buttons
        button_width, button_height = 300, 60
        x = self.storage.width - button_width - 50  # Right alignment with 50px padding
        self.draw_button("Play", pygame.Rect(x, 200, button_width, button_height), self.storage.BLUE)
        self.draw_button("GitHub", pygame.Rect(x, 300, button_width, button_height), self.storage.PURPLE)
        self.draw_button("Quit", pygame.Rect(x, 400, button_width, button_height), self.storage.RED)

    def draw_level_menu(self):
        """
        Draw the level selection menu screen.
        """
        self.screen.blit(self.background_lvl, (0, 0))
        self.storage.render_text(self.screen, "Select Level", 50, self.storage.WHITE)

        # Two-column level layout
        button_width, button_height = 160, 50
        padding_x, padding_y = 140, 100
        start_x = 320
        start_y = 150

        for i in range(self.level_count):
            col = i % 3
            row = i // 3
            x = start_x + col * (button_width + padding_x)
            y = start_y + row * (button_height + padding_y)
            self.draw_button(f"Level {i + 1}", pygame.Rect(x, y, button_width, button_height), self.storage.BLUE)


        # Back button
        self.draw_button("Back", pygame.Rect(45, self.storage.height - 100, 160, 50), self.storage.RED)

    def handle_level_menu_events(self, event):
        """
        Handle events for the level selection menu.
        """
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            button_width, button_height = 160, 50
            padding_x, padding_y = 140, 100
            start_x = 320
            start_y = 150

            for i in range(self.level_count):
                col = i % 3
                row = i // 3
                bx = start_x + col * (button_width + padding_x)
                by = start_y + row * (button_height + padding_y)

                # Check if the button was clicked
                if bx <= x <= bx + button_width and by <= y <= by + button_height:
                    self.selected_level = f"level{i + 1}"  # Set selected level
                    self.active_menu = None  # Transition to game
                    break

            # Back button
            if 45 <= x <= 45 + 160 and self.storage.height - 100 <= y <= self.storage.height - 50:
                self.active_menu = "main"
