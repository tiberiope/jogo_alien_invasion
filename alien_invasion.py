import sys
import pygame
from settings import Setting
from ship import Ship

def run_game():
    # Inicializa o jogo e cria um objeto para a tela.
    pygame.init()
    ai_settings = Setting()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')
    ship = Ship(screen)
    # Inicia o laço principal do jogo.
    while True:

        # Obeserva eventos de teclado e de mouse.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Redesenha a tela a cada passagem pelo laço.
        screen.fill(ai_settings.bg_color)
        ship.blitme()

        # Deixa visível a tela mais recente.
        pygame.display.flip()

run_game()

