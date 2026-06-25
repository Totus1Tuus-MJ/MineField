## button.py

import random
import pygame

class Button:
    def __init__(self, rect, get_text, callback):
        self.rect = rect
        self.get_text = get_text
        self.callback = callback

    def click(self):
        self.callback()

    def draw(self, screen, reg_font, Color):
        pygame.draw.rect(screen, Color.DARK_GRAY, self.rect)
        pygame.draw.rect(screen, Color.WHITE, self.rect, 2)

        text = self.get_text()
        
        text_surface = reg_font.render(text, True, Color.WHITE)
        text_rect = text_surface.get_rect(center = self.rect.center)

        screen.blit(text_surface, text_rect)
