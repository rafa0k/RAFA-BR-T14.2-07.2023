import random
import pygame

from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD


class ObstacleManager:
    def __init__(self):
        self.obstacles = []
    
    def update(self, game):
        if len(self.obstacles) == 0:
            option = random.randint(1,3)
            if option == 1:
                self.obstacles.append(Cactus(SMALL_CACTUS[random.randint(0,2)]))
            elif option == 2:
                cactus = Cactus(LARGE_CACTUS[random.randint(0,2)])
                cactus.rect.y = 300# mudando a posição do cactus Largo
                self.obstacles.append(cactus)
            elif option == 3:
                self.obstacles.append(Bird(BIRD))
                
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(500)
                game.playing = False
                game.death_count += 1
            
        
    def draw(self,screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
            
    def reset_obstacles(self):
        self.obstacles.clear()