import pygame
from constants import *
from circleshape import *


class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        self.image = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)  # Transparent surface
        self.rect = self.image.get_rect(center=(x, y))  # Center the rectangle on the shot position

    def draw(self, screen):
        pygame.draw.circle(self.image, "white", (self.radius, self.radius), self.radius, 2)  # Draw on self.image
        screen.blit(self.image, self.rect.topleft)  # Blit surface to screen

    def update(self, dt):
        self.position += self.velocity * dt
        self.rect.center = self.position  # Sync rectangle position with the shot position

        if (self.rect.right < 0 or self.rect.left > SCREEN_WIDTH or
            self.rect.bottom < 0 or self.rect.top > SCREEN_HEIGHT):
            self.kill()  # Remove the shot from all sprite groups
