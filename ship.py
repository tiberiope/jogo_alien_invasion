import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self, ai_settings, screen):
        '''Inicializa a nave e define a sua posição inicial'''
        super(Ship, self).__init__()

        self.screen = screen
        self.ai_settings = ai_settings

        # Carrega a imagem da nava e obtém o seu rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Inicia cada nova nave em sua posição atual.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Cria as coordenadas com valor decimal.
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.bottom)

        # Carrega as flags de movimento.
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        '''Atualiza a posição da nave de acordo com a flag de movimento.'''
        if (self.moving_right) and (self.rect.right < self.screen_rect.right):
            self.centerx += self.ai_settings.ship_speed_factor

        elif (self.moving_left) and (self.rect.left > 0):
            self.centerx -= self.ai_settings.ship_speed_factor

        if (self.moving_up) and (self.rect.top > 5):
            self.centery -= self.ai_settings.ship_speed_factor

        elif (self.moving_down) and (self.rect.bottom < self.screen_rect.bottom):
            self.centery += self.ai_settings.ship_speed_factor

        # Atualiza o objeto de acordo com o centerx e centery.
        self.rect.centerx = self.centerx
        self.rect.bottom = self.centery

    def blitme(self):
        '''Desenha a nave em sua posição atual.'''
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        '''Centraliza a nave na tela.'''
        self.centerx = self.screen_rect.centerx
        self.centery = self.screen_rect.bottom

