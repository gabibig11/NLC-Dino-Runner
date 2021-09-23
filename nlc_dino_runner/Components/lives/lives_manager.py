from nlc_dino_runner.Components.lives.live import Live
from nlc_dino_runner.utils.constants import DEFAULT_NUMBER_OF_LIVES


class LivesManager:
    def __init__(self):
        self.number_of_lives = DEFAULT_NUMBER_OF_LIVES

    def reduce_live(self):
        self.number_of_lives -= 1

    def restart_lives(self):
        self.number_of_lives = DEFAULT_NUMBER_OF_LIVES

    def print(self, screen):
        dinamic_pos_x = 30
        for i in range(self.number_of_lives):
            live = Live(dinamic_pos_x)
            live.draw(screen)
            dinamic_pos_x += 27
