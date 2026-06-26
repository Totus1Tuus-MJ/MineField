## torpedo.py

import pygame

class Torpedo:
    def __init__(self, x, y, speed, x_size, y_size):
        self.x = x
        self.y = y
        self.speed = speed
        self.x_size = x_size
        self.y_size = y_size
        

    def move(self, dt):
        self.y -= self.speed * dt


    def off_screen(self):
        return self.y < -self.y_size

    def rect(self):
        return pygame.Rect(self.x, self.y, self.x_size, self.y_size)

    def draw(self, screen, sprite ):
        screen.blit(sprite, (self.x, self.y))
        

    def collides_with(self, rect):
        return self.rect().colliderect(rect)
        
        
