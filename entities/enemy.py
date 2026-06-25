## enemy.py

import pygame

class Enemy:
    def __init__(self, x, y, size, speed):
        self.x = x
        self.y = y
        self.size = size
        self.speed = speed
    

    def move(self, dt):
        self.y += self.speed * dt

    def off_screen(self, HEIGHT):
        return self.y > HEIGHT

    def rect(self):
        return pygame.Rect(self.x, self.y, self.size, self.size)
    
    def collides_with(self, rect):
        return self.rect().colliderect(rect)

    def draw(self, screen, sprite):
        screen.blit(sprite, (self.x, self.y))

    
