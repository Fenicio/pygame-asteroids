# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable)
    Shot.containers = (updatable, drawable, shots)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    spawner = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Quitting")
                return

        # clear the screen by filling it with black
        screen.fill((0, 0, 0))
    
        for sprite in updatable:
            sprite.update(dt)

        for sprite in drawable:
            sprite.draw(screen)
        
        for sprite in asteroids:
            if player.collides(sprite):
                player.kill()
                print("Game Over!")
                return
            for bullet in shots:
                if sprite.collides(bullet):
                    bullet.kill()
                    sprite.kill()

        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()