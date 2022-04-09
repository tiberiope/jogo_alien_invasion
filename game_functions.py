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

def update_bullets(ai_settings, screen, ship, aliens, bullets):
    # Livra-se dos projéteis que desaparecem.
    bullets.update()

    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    if len(aliens) == 0:
        # Destrói os projéteis existentes e cria uma nova frota.
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)

    # Verifica se algum projétil atingiu um alien.
    # Em caso afirmativo, livra-se do projétil e do alien.
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

def fire_bullet(ai_settings, screen, ship, bullets):
    # Cria um novo projétil e o adiciona ao grupo de projéteis.
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def get_number_rows(ai_settings, ship_height, alien_height):
    '''Determina o número de linhas com aliens que cabem na tela.'''
    availeble_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_row = int(availeble_space_y / (2 * alien_height))
    return number_row

def get_number_aliens_x(ai_settings, alien_width):
    '''Determina o número de alienígenas que cabem em uma linha.'''
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    #Cria uma alien e o posiciona na linha.
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens):
    # Cria um alienígena e calcula o númerode alienígenas em uma linha.
    # Espaçamento entre os alienígenas é igual à largura de um alienígena.

    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    for row_number in range(number_rows):
        # Cria um alienígena e o posiciona na linha.
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)

def check_fleet_edges(ai_settings, aliens):
    '''Responde se algum alien alcançou uma borda.'''
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    '''Faz a frota de aliens descer e muda a direção.'''
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def update_aliens(ai_settings, ship, aliens):
    '''Verifica se a frota está na borda, então atualiza as posições de todos os aliens.'''
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # Verifica se houve colisão entre a nave e o alien.
    if pygame.sprite.spritecollideany(ship, aliens):
        print('Colidiu')

