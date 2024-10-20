import pygame
import random
import math

from bounce.game_object import GameObject


class Ball(GameObject):
    VEL_MULTIPLIER = 2

    def __init__(self, x, y, radius, is_white):
        super().__init__(x, y, radius, radius)
        self.is_white = is_white
        self.x_vel = random.choice([-1, 1])
        self.y_vel = random.choice([-1, 1])

    def draw(self, screen):
        color = (255, 255, 255) if self.is_white else (0, 0, 0)
        pygame.draw.circle(screen, color, (int(self.x), int(self.y)), self.width)

    def update(self, blocks):
        self.x += Ball.VEL_MULTIPLIER * self.x_vel
        self.y += Ball.VEL_MULTIPLIER * self.y_vel

        update_x = False
        update_y = False
        width, height = pygame.display.get_surface().get_size()

        # Boundary collision (window edges)
        if self.x - self.width <= 0 or self.x + self.width >= width:
            update_x = True

        if self.y - self.width <= 0 or self.y + self.height >= height:
            update_y = True

        # Block collision detection
        candidate_blocks = []

        for block in blocks:
            if block.is_white == self.is_white and self.distance_from_block(block) < self.width:
                candidate_blocks.append(block)

                closest_points = self.closest_point(block)
                if abs(closest_points[0] - self.x) > abs(closest_points[1] - self.y):
                    update_x = True
                else:
                    update_y = True

        # Flip the nearest block color
        if candidate_blocks:
            closest_block = min(candidate_blocks, key=lambda block: self.distance_from_block(block))
            closest_block.queue_flip()

        if update_x:
            self.x_vel *= -1

        if update_y:
            self.y_vel *= -1

    def distance_from_block(self, block):
        closest_points = self.closest_point(block)
        distance_x = self.x - closest_points[0]
        distance_y = self.y - closest_points[1]
        distance_squared = (distance_x ** 2) + (distance_y ** 2)
        return math.sqrt(distance_squared)

    def closest_point(self, block):
        closest_x = max(block.x, min(self.x, block.x + block.width))
        closest_y = max(block.y, min(self.y, block.y + block.height))
        return closest_x, closest_y
