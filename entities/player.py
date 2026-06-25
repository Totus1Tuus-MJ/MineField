## player.py

import pygame

class Player:
    def __init__(self, x, y, size, x_speed, y_speed):
        self.x = x
        self.y = y
        self.size = size
        self.x_speed = x_speed
        self.y_speed = y_speed

    def move(self, keys, dt, width, height):
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.x -= self.x_speed * dt

        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.x += self.x_speed * dt

        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.y -= self.y_speed * dt

        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.y += self.y_speed * dt

        self.x = max(0, min(self.x, width - self.size))
        self.y = max(0, min(self.y, height - self.size))

    
    def rect(self, shields):
        shielded_size = max(1, self.size - shields * 2)
        return pygame.Rect(self.x + shields, self.y + shields, shielded_size, shielded_size)

    
    def expanded_rect(self):
        return pygame.Rect(self.x, self.y, self.size, self.size)

    def draw(self, screen, sprite, shields_color, shields, shields_size):
        screen.blit(sprite, (self.x, self.y))
        pygame.draw.rect(screen, shields_color, self.rect(shields), shields_size)
 
    def center(self):
        return (self.x + self.size // 2, self.y)
