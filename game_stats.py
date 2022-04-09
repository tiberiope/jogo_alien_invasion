class GameStats():
    '''Armazena dados estatísticos da Invasão Alienígena.'''

    def __init__(self, ai_settings):
        '''Inicializa os dados estatísticos.'''
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = True

    def reset_stats(self):
        '''Inicializa os dados estatísticos que podem mudar durante o jogo.'''
        self.ship_left = self.ai_settings.ship_limit
