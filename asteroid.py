import pygame
import random
from circleshape import *
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius, 2)  # Draw the asteroid

    def update(self, dt):
        self.position += self.velocity * dt

    def set_velocity(self, velocity):
        self.velocity = velocity # May not need this since we inherited from CircleShape

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        random_angle = random.uniform(20,50)

        # Step 5: Rotate original velocity by positive and negative random angles
        velocity_1 = self.velocity.rotate(random_angle) * 1.2  # Slightly faster
        velocity_2 = self.velocity.rotate(-random_angle) * 1.2  # Slightly faster

        # Step 6: Create two new smaller asteroids
        asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)

        # Set their velocities
        asteroid_1.set_velocity(velocity_1)
        asteroid_2.set_velocity(velocity_2)
