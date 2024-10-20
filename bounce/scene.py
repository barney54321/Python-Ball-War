import random

from bounce.ball import Ball
from bounce.block import Block


# Import Ball and Block (you'll need to define these similar to your Java objects)

class Scene:
    def __init__(self, screen):
        self.screen = screen
        width, height = self.screen.get_size()

        # Initialize balls
        self.balls = [
            Ball(width // 2, 20, 12, True),
            Ball(width // 2, height - 40, 12, False)
        ]

        # Initialize blocks
        self.blocks = []
        block_dim = 30
        num_blocks = (width * height) // (block_dim * block_dim)
        num_blocks_starting_black = (
                (num_blocks // 2) +
                (random.randint(-num_blocks // 4, num_blocks // 4))
        )

        # Create the blocks grid
        for y in range(0, height, block_dim):
            for x in range(0, width, block_dim):
                is_white = len(self.blocks) > num_blocks_starting_black
                self.blocks.append(Block(x, y, block_dim, block_dim, is_white))

    def update(self, width, height):
        # Update each ball's position based on block collisions
        for ball in self.balls:
            ball.update(self.blocks)

        # Flip block color if needed
        for block in self.blocks:
            block.flip_if_needed()

        # Draw the blocks and balls
        for block in self.blocks:
            block.draw(self.screen)
        for ball in self.balls:
            ball.draw(self.screen)

    def reset(self):
        # Reset the scene if needed (e.g., on key press 'R')
        width, height = self.screen.get_size()
        self.__init__(self.screen)
