import pygame

class Character ():

    def __init__(self, screen):
        
        self.screen = screen
        self.image = pygame.image.load('character.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect ()
        self.rect.centerx = self.screen_rect.centerx

    def blitme(self):

        """Dibujar el ship en su posicion actual"""

        self.screen.blit (self.image, self.rect)