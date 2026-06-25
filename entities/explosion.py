## explosion.py

import pygame

class Explosion:
    def __init__(self, x, y, max_radius = 35):
        self.x = x
        self.y = y

        self.radius = 5
        self.max_radius = max_radius

        self.growth_speed = 120
        self.finished = False

    def move(self, dt):
        self.radius += self.growth_speed * dt

        if self.radius >= self.max_radius:
            self.finished = True

    def draw(self, screen, color):
        pygame.draw.circle(screen, color, (int(self.x), int(self.y)), int(self.radius), 5)
        
