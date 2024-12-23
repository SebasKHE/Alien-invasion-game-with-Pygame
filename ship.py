import pygame
from pygame.sprite import Sprite

class Ship(Sprite):

    def __init__(self, ai_settings, screen):
        """inicializazmos el ship y lo configuramos a su posicion inicial"""
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        #cargamos la imagen del ship y obtenemos su rectangulo

        self.image = pygame.image.load('rocket.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #comenzamos cada nuevo sheep en el centro abajo de la pantalla
        
        self.rect.bottom = self.screen_rect.bottom
        self.rect.centerx = self.screen_rect.centerx

        #store decimal value for the ship's center.
        self.center = float(self.rect.centerx)

        #Movemente flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """ Update the ships position based on the movement flag."""
        #update the ship's center value, not the rect
        if self.moving_right and self.rect.right < (self.screen_rect.right):
            self.center += self.ai_settings.ship_speed_factor

        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        #update de rect objetc from self.center

        self.rect.centerx = self.center

    def blitme(self):

        """Dibujar el ship en su posicion actual"""

        self.screen.blit (self.image, self.rect)

    def center_ship(self):
        """Center the ship on the screen"""
        self.center = self.screen_rect.centerx