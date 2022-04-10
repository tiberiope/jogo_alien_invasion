class Setting():
    '''Uma classe para armazenar todas as configurações da Invasão Alienígena.'''

    def __init__(self):
        '''Inicializa as configurações do jogo.'''

        # Configurações de tela.
        self.screen_width = 900
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # Configurações da nave.
        self.ship_limit = 3

        # Configurações dos projéteis.
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Configurações dos aliens.
        self.fleet_drop_speed = 10

        # A taxa com que a velocidade do jogo aumenta.
        self.speedup_scale = 1.1

        # A taxa com que os pontos para cada alien aumenta.
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        '''Inicializa as configurações que mudam no decorrer do jogo.'''
        self.ship_speed_factor = 1
        self.bullet_speed_factor = 0.5
        self.alien_speed_factor = 0.4

        # Pontuação
        self.alien_points = 50

        # Fleet_direction igual 1 representa a direita; -1 representa a esquerda.
        self.fleet_direction = 1

    def increase_speed(self):
        '''Aumenta as configurações de velocidade.'''
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.score_scale * self.alien_points)