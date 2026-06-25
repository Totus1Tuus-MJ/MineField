## bullet.py

import pygame

class Bullet:
    def __init__(self, x, y, size, speed):
        self.x = x
        self.y = y
        self.size = size
        self.speed = speed


    def move(self, dt):
        self.y -= self.speed * dt

    def off_screen(self):
        return self.y < -self.size

    def rect(self):
        return pygame.Rect(self.x, self.y, self.size, self.size)

    def draw(self, screen, sprite):
        screen.blit(sprite, (int(self.x), int(self.y)))
    def collides_with(self, rect):
        return self.rect().colliderect(rect)

        
