import pygame

from bounce.game_object import GameObject


class Block(GameObject):
    def __init__(self, x, y, width, height, is_white):
        super().__init__(x, y, width, height)
        self.is_white = is_white
        self.queued = False

    def draw(self, screen):
        color = (255, 255, 255) if self.is_white else (0, 0, 0)
        pygame.draw.rect(screen, color, pygame.Rect(self.x, self.y, self.width, self.height))

    def queue_flip(self):
        self.queued = True

    def flip_if_needed(self):
        if self.queued:
            self.is_white = not self.is_white
        self.queued = False
