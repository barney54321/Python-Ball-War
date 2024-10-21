import pygame
import sys

from bounce.scene import Scene


FPS = 220
START_WIDTH = 480
START_HEIGHT = 480


# Initialize the game
def main():
    pygame.init()
    width = START_WIDTH
    height = START_HEIGHT
    screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
    pygame.display.set_caption("Bounce")
    clock = pygame.time.Clock()

    scene = Scene(screen)

    # Main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Handle window resize
            if event.type == pygame.VIDEORESIZE:
                width, height = event.w, event.h
                scene = Scene(screen)

            # Handle key presses
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    scene.reset()  # Reset the scene when "R" is pressed

        # Update the scene
        scene.update(width, height)

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(FPS)


if __name__ == "__main__":
    main()
