import sys
import pygame
from settings import Setting
from ship import Ship
import game_functions as gf

def run_game():
    # Inicializa o jogo e cria um objeto para a tela.
    pygame.init()
    ai_settings = Setting()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')
    ship = Ship(ai_settings, screen)
    # Inicia o laço principal do jogo.
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)


run_game()

