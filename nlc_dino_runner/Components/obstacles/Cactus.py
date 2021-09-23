import random

from nlc_dino_runner.Components.obstacles.Obstacles import Obstacles


class Cactus(Obstacles):

    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 321


