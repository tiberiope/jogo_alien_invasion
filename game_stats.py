class GameStats():
    '''Armazena dados estatísticos da Invasão Alienígena.'''

    def __init__(self, ai_settings):
        '''Inicializa os dados estatísticos.'''
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False

        # A pontuação máxima jamais deverá ser reiniciada.
        self.carrega_score_max()

    def reset_stats(self):
        '''Inicializa os dados estatísticos que podem mudar durante o jogo.'''
        self.ship_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1


    def carrega_score_max(self):
        caminho = 'score.txt'
        score_max_str = ''

        with open(caminho, 'r') as arq_score_max:
            for linha in arq_score_max:
                score_max_str = linha

            if score_max_str == '':
                self.high_score = 0
            else:
                self.high_score = int(score_max_str)