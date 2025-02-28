import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *
from circleshape import *

def main():
    pygame.init()    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        updatable.update(dt)
        shots.update(dt)
        shots.draw(screen)

        for asteroid in asteroids:
            if player.collides_with(asteroid):
                print("Game over!")
                pygame.quit()
                exit()
            for shot in shots:
                if shot.collides_with(asteroid):
                    shot.kill()  # Remove bullet
                    asteroid.kill()  # Remove asteroid
                    print("Asteroid destroyed!")

        screen.fill((0, 0, 0))
        for sprite in drawable:
            sprite.draw(screen)  # Draw the player
        pygame.display.flip()

        dt = clock.tick(60) / 1000

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}") 
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()
