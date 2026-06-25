## torpedo.py

import pygame

class Bomb:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 100
        self.speed = 250
        self.requested_distance_from_player = 500
        self.distance_travelled = 0
        
        self.detonated = False

    def move(self, dt):
        if not self.detonated:
            distance = self.speed * dt

            self.y -= distance
            self.distance_travelled += distance

            if self.distance_travelled >= self.requested_distance_from_player:
                self.detonated = True


    def finished(self):
        return self.detonated

    def draw(self, screen, sprite):
            diameter = self.radius * 2
            sprite = pygame.transform.scale(sprite, (diameter, diameter))
            screen.blit(sprite, (int(self.x - self.radius), int(self.y - self.radius)))
