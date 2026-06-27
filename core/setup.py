## setup.py

import pygame

from core import game_flow, button_setup, config
from services import asset_loader

def pre_login_init():

    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
    pygame.display.set_caption("MineField EXT Standard 7.7")

    reg_font = pygame.font.SysFont(None, config.REG_FONT_SIZE)
    small_font = pygame.font.SysFont(None, config.SMALL_FONT_SIZE)
    
    clock = pygame.time.Clock()

    return screen, reg_font, small_font, clock

def post_login_init(state, screen, reg_font, small_font):
    high_score = game_flow.attempt_restart(state, screen, reg_font, small_font)

    hud_icons = asset_loader.load_hud_icons()
    sprites = asset_loader.load_images(state)
    sounds = asset_loader.load_sounds()
    asset_loader.load_music()
    
    pause_buttons, achievements_buttons, quit_button = button_setup.create_buttons(state, screen, reg_font, small_font, sounds)

    state.sounds = sounds
    state.pause_buttons = pause_buttons
    state.achievements_buttons = achievements_buttons
    state.quit_button = quit_button
    state.reg_font = reg_font
    state.small_font = small_font
    state.screen = screen

    return high_score, sprites, sounds, hud_icons, pause_buttons, achievements_buttons, quit_button
