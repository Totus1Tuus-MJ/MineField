## setup.py

import pygame

import config
from core import game_flow
from services import asset_loader
from ui.button import Button

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
    hud_icons = asset_loader.load_hud_icons()
    asset_loader.load_music()
    quit_button = Button(pygame.Rect(1300, 0, 200, 50), lambda: f"QUIT", lambda: game_flow.stop_game(True, state, sounds))

    music_button = Button(pygame.Rect(200, 200, 200, 50), lambda: f"Music: {'ON' if not state.music_off else 'OFF'}", lambda: game_flow.toggle_music(state))
    sounds_button = Button(pygame.Rect(config.WIDTH - 400, 200, 200, 50), lambda: f"Sounds: {'ON' if not state.sounds_off else 'OFF'}", lambda: game_logic.toggle_sounds(state))
    restart_button = Button(pygame.Rect(config.WIDTH - 400, 600, 200, 50), lambda: f"RESTART", lambda: game_flow.attempt_restart(state, screen, reg_font, small_font))
    pause_buttons = [music_button, sounds_button, restart_button]

    return_to_pause_button = Button(pygame.Rect(config.WIDTH - 400,200, 200, 50), lambda: f"BACK", lambda: setattr(state, "show_achievements", False))
    return_to_game_button = Button(pygame.Rect(config.WIDTH - 400, 275, 200, 50), lambda: f"PLAY", lambda: (setattr(state, "game_going", True), setattr(state, "paused", False), setattr(state, "show_achievements", False)))
    restart_button = Button(pygame.Rect(config.WIDTH - 400, 425, 200, 50), lambda: f"RESTART", lambda: game_flow.attempt_restart(state, screen, reg_font, small_font))
    achievements_buttons = [return_to_pause_button, return_to_game_button, restart_button]
    state.sounds = sounds
    state.pause_buttons = pause_buttons
    state.achievements_buttons = achievements_buttons
    state.quit_button = quit_button
    state.reg_font = reg_font
    state.small_font = small_font
    state.screen = screen

    return high_score, sprites, sounds, hud_icons, pause_buttons, achievements_buttons, quit_button
