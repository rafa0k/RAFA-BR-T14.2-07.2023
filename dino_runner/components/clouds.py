import random

from dino_runner.utils.constants import SCREEN_WIDTH, CLOUD

class Clouds:
    def __init__(self):
        self.image = CLOUD
        self.cloud_rect = self.image.get_rect()       

    def update(self):
        self.cloud_rect.x  -= 5
        if self.cloud_rect.right < 0:
            self.cloud_rect.x = SCREEN_WIDTH + random.randint(200, 1000)
            self.cloud_rect.y = random.randint(25, 200)

    def draw(self, screen):
         screen.blit(self.image, (self.cloud_rect.x , self.cloud_rect.y))
