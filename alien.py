import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    '''Classe que representa um único alienígena da frota.'''

    def __init__(self, ai_settings, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #Carrega a imagem do alienígena e define seu atributo rect.
        self.image =  pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #Inicia cada novo alienígena próximo à Y == 0.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Armazena a posição exata do alienígena.
        self.x = float(self.rect.x)

    def blitme(self):
        '''Desenha a nave alienígena em sua posição atual.'''
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        '''Devolve True se o alien estiver na borda da tela.'''
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        '''Move o alien para a direira e para a esquerda.'''
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x

