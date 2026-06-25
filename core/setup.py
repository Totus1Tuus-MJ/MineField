## setup.py

import pygame

import config
import game_logic
import asset_loader
from button import Button
import achievements

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
    high_score = game_logic.attempt_restart(state, screen, reg_font, small_font)

    hud_icons = asset_loader.load_hud_icons()
    sprites = asset_loader.load_images(state)
    sounds = asset_loader.load_sounds()
    hud_icons = asset_loader.load_hud_icons()
    asset_loader.load_music()

    music_button = Button(pygame.Rect(200, 200, 200, 50), lambda: f"Music: {'ON' if not state.music_off else 'OFF'}", lambda: game_logic.toggle_music(state))
    sounds_button = Button(pygame.Rect(config.WIDTH - 400, 200, 200, 50), lambda: f"Sounds: {'ON' if not state.sounds_off else 'OFF'}", lambda: game_logic.toggle_sounds(state))
    quit_button = Button(pygame.Rect(200, 600, 200, 50), lambda: f"QUIT", lambda: game_logic.stop_game(True, state, sounds))
    restart_button = Button(pygame.Rect(config.WIDTH - 400, 600, 200, 50), lambda: f"RESTART", lambda: game_logic.attempt_restart(state, screen, reg_font, small_font))
    pause_buttons = [music_button, sounds_button, quit_button, restart_button]

    return_to_pause_button = Button(pygame.Rect(config.WIDTH - 400,200, 200, 50), lambda: f"BACK", lambda: setattr(state, "show_achievements", False))
    return_to_game_button = Button(pygame.Rect(config.WIDTH - 400, 275, 200, 50), lambda: f"PLAY", lambda: (setattr(state, "game_going", True), setattr(state, "paused", False), setattr(state, "show_achievements", False)))
    quit_button = Button(pygame.Rect(config.WIDTH - 400, 350, 200, 50), lambda: f"QUIT", lambda: game_logic.stop_game(True, state, sounds))
    restart_button = Button(pygame.Rect(config.WIDTH - 400, 425, 200, 50), lambda: f"RESTART", lambda: game_logic.attempt_restart(state, screen, reg_font, small_font))
    achievements_buttons = [return_to_pause_button, return_to_game_button, quit_button, restart_button]
    
    
    return high_score, sprites, sounds, hud_icons, pause_buttons, achievements_buttons
