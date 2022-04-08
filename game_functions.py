import sys
import pygame
from bullet import Bullet
from alien import Alien

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    '''Responde aos pressionamentos de tecla.'''
    # Inicia o movimento da nave.
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True

    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

    elif event.key == pygame.K_UP:
        ship.moving_up = True

    elif event.key == pygame.K_DOWN:
        ship.moving_down = True

    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)

    elif event.key == pygame.K_ESCAPE:
        sys.exit()

def check_keyup_events(event, ship):
    '''Responde às solturas de teclas.'''
    # Finaliza o movimento da nave.
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False

    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

    elif event.key == pygame.K_UP:
        ship.moving_up = False

    elif event.key == pygame.K_DOWN:
        ship.moving_down = False


def check_events(ai_settings, screen, ship, bullets):
    '''Responde eventos de pressionamento de teclas e de mouse.'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship, aliens, bullets):
    # Redesenha a tela a cada passagem pelo laço.
    screen.fill(ai_settings.bg_color)

    #Redesenha todos os projéteis atrás da nave e dos alienígenas.
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)

    # Deixa visível a tela mais recente.
    pygame.display.flip()

def update_bullets(bullets):
    # Livra-se dos projéteis que desaparecem
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def fire_bullet(ai_settings, screen, ship, bullets):
    # Cria um novo projétil e o adiciona ao grupo de projéteis.
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def create_fleet(ai_settings, screen, aliens):
    #Cria um alienígena e calcula o númerode alienígenas em uma linha.
    #I espaçamento entre os alienígenas é igual à largura de um alienígena.
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x/ (2 * alien_width))

    for alien_number in range(number_aliens_x):
        #Cria um alienígena e o posiciona na linha.
        alien = Alien(ai_settings, screen)
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        aliens.add(alien)
