# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # clear the screen by filling it with black
        screen.fill((0, 0, 0))


        pygame.display.flip()
        dt = clock.tick(60)

if __name__ == "__main__":
    main()