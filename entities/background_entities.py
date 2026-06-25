## space.py

import random
import pygame

class Star:
    def __init__(self, x, y, size, color, base_speed, layer):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.base_speed = base_speed
        self.layer = layer

    def move(self, dt, score):
        layer_speed_multiplier = [0.4, 0.7, 1.2]
        star_multiplier = min(600, score * 0.5)
        
        self.y += (self.base_speed * layer_speed_multiplier[self.layer] + star_multiplier)* dt

    def off_screen(self, HEIGHT):
        return self.y > HEIGHT
    def reset(self, width):
        self.x = random.randint(1, width)
        self.y = -self.size

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.size)

class Planet:
    def __init__(self, x, y, radius, color, speed, sprite):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.speed = speed
        self.sprite = sprite

    def move(self, dt):
        self.y += self.speed * dt

    def rect(self):
        diameter = self.radius * 2
        return pygame.Rect(self.x - self.radius, self.y - self.radius, diameter, diameter)

    def draw(self, screen):
        diameter = self.radius * 2
        sprite = pygame.transform.scale(self.sprite, (diameter, diameter))
        screen.blit(sprite, (int(self.x - self.radius), int(self.y- self.radius)))

    def off_screen(self, height):
        return self.y - self.radius > height  
