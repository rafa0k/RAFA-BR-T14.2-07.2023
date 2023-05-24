import random

from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import OBSTACLE_Y_POS

class Bird(Obstacle):
    def __init__(self, images):
        super().__init__(images[0]) #iniciando com uma imagem inicial
        
        self.ini_y_pos = random.randint(150,280)
        self.images = images #array de images
        self.rect.y = self.ini_y_pos #desenhando no ar
        self.flying_index = 0 #usado para mudar a imagen
        
        self.touched_ground = False
        self.moving = random.randint(1,2) % 2 == 0 and True or False
            
    def update(self, game_speed, obstacles):
        self.fly()
        
        if self.flying_index > 9:
            self.flying_index = 0
        
        super().update(game_speed, obstacles)
        
    def fly(self):
        self.image = self.images[self.flying_index//5]
        self.flying_index += 1
        
        if self.moving:
            if not self.touched_ground:
                self.rect.y +=10
                if self.rect.y > OBSTACLE_Y_POS:
                    self.touched_ground = True
            else:
                self.rect.y -= 10
                if self.rect.y < self.ini_y_pos:
                    self.touched_ground = False
        
