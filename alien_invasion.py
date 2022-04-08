import sys
import pygame
from settings import Setting
from ship import Ship
import game_functions as gf
from pygame.sprite import Group

def run_game():
    # Inicializa o jogo e cria um objeto para a tela.
    pygame.init()
    ai_settings = Setting()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    # Cria a nave.
    ship = Ship(ai_settings, screen)

    # Cria um grupo no qual serão armazenados os projéteis.
    bullets = Group()

    # Inicia o laço principal do jogo.
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_screen(ai_settings, screen, ship, bullets)
        gf.update_bullets(bullets)


run_game()

