import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self, ai_settings, screen, ship=None, alien=None):
        """Create a bullet object at the ship0s current position"""
        super().__init__()
        self.screen=screen

        #Create a bullet rect at (0, 0 and then set correct position.)
        if ship:
            self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_heigth)
            self.rect.centerx = ship.rect.centerx
            self.rect.top = ship.rect.top
            self.direction = "up"
        elif alien:
            self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_heigth)
            self.rect.centerx = alien.rect.centerx
            self.rect.bottom = alien.rect.bottom
            self.direction = "down"

        #store the bullet's position as a decimal value
        self.y = float(self.rect.y)
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """Move the bullet up the screen"""
        #Update the decimal position of the bullet
        if self.direction == "up":
            self.y -= self.speed_factor
        elif self.direction == "down":
            self.y += self.speed_factor
        #update the rect position.
        self.rect.y = self.y

    def draw_bullet (self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
