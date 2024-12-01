import pygame
import storage

store = storage.Storage()


class ButtonDoor:
    def __init__(self, button_pos, door_pos):
        self.button_pos = button_pos
        self.button_rect = pygame.Rect(button_pos[0], button_pos[1], 50, 100)
        self.door_pos = door_pos
        self.action = False
        
        image_paths = [
            f"{store.phat}\\src\\img\\button1.png",
            f"{store.phat}\\src\\img\\door1.png",
            f"{store.phat}\\src\\img\\button.png",
            f"{store.phat}\\src\\img\\door.png"
        ]
        
        self.img = [
            [
                pygame.image.load(image_paths[0]).convert_alpha(),
                pygame.image.load(image_paths[1]).convert_alpha()
            ],
            [
                pygame.image.load(image_paths[2]).convert_alpha(),
                pygame.image.load(image_paths[3]).convert_alpha()
            ]
        ]

        for row in self.img:
            for i in range(len(row)):
                original_size = row[i].get_size()
                target_size = (int(original_size[0] * 6.25), int(original_size[1] * 6.25))
                row[i] = pygame.transform.scale(row[i], target_size)

                
        self.button_rect = pygame.Rect(button_pos[0], button_pos[1], self.img[0][0].get_width(), self.img[0][0].get_height())


    def draw(self, screen):
        if self.action:
            screen.blit(self.img[0][0], self.button_pos)
            screen.blit(self.img[0][1], self.door_pos)
        else:
            screen.blit(self.img[1][0], self.button_pos)
            screen.blit(self.img[1][1], self.door_pos)
            


    def is_pressd(self):
        self.action = True

