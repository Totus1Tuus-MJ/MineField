## upgrade.py
import random
import pygame

class Upgrade:
    max_upgrades = 5

    
    def __init__(self, x, y, size, speed, min_speed):
        self.x = x
        self.y = y
        self.size = size
        self.speed = speed
        self.min_speed = min_speed
        

    def move(self, dt, upgrade_slowdown):
        self.y += max(self.min_speed,(self.speed - upgrade_slowdown)) * dt

    def off_screen(self, HEIGHT):
        return self.y > HEIGHT

    def rect(self):
        return pygame.Rect(self.x, self.y, self.size, self.size)
    
    def collides_with(self, rect):
        return self.rect().colliderect(rect)

    def draw(self, screen, sprite):
        screen.blit(sprite, (self.x, self.y))

    
