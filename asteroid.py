import pygame
from circleshape import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius, 2)  # Draw the asteroid

    def update(self, dt):
        self.position += self.velocity * dt

    def set_velocity(self, velocity):
        self.velocity = velocity # May not need this since we inherited from CircleShape
