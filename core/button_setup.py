## button_setup.py

import pygame
from core import game_flow, config
from services import audio
from systems import weapons
from ui.button import Button

def create_buttons(state, screen, reg_font, small_font, sounds):
    quit_button = Button(pygame.Rect(1440, 0, 100, 50), lambda: f"[Q]UIT", lambda: game_flow.stop_game(True, state, sounds))

    music_button = Button(pygame.Rect(config.WIDTH - 400, 200, 200, 50), lambda: f"[M]usic: {'ON' if not state.music_off else 'OFF'}", lambda: audio.toggle_music(state))
    sounds_button = Button(pygame.Rect(config.WIDTH - 400, 275, 200, 50), lambda: f"[S]ounds: {'ON' if not state.sounds_off else 'OFF'}", lambda: audio.toggle_sounds(state))

    noise_logic = lambda: f"[N]oises: {'OFF' if state.music_off  and state.sounds_off else ('ON' if not state.music_off and not state.sounds_off else 'Mix')}"
    noise_button = Button(pygame.Rect(config.WIDTH - 400, 350, 200, 50), noise_logic, lambda: audio.toggle_noises(state))

    restart_button = Button(pygame.Rect(config.WIDTH // 2 - 100, 600, 200, 50), lambda: f"[R]ESTART", lambda: game_flow.attempt_restart(state, screen, reg_font, small_font))

    achievements_button = Button(pygame.Rect(config.WIDTH // 2 - 100, 700, 200, 50), lambda: f"[A]CHIEVE", lambda: setattr(state, "show_achievements", True))

    firing_button = Button(pygame.Rect(config.WIDTH - 400, 500, 200, 50), lambda: f"[F]iring: {'ON' if state.firing_mode else 'OFF'}", lambda: weapons.toggle_firing(state))
    bomb_button = Button(pygame.Rect(config.WIDTH - 400, 575, 200, 50), lambda: f"[B]ombs: {'ON' if state.bomb_mode else 'OFF'}", lambda: weapons.toggle_bombs(state))
    torpedo_button = Button(pygame.Rect(config.WIDTH - 400, 650, 200, 50), lambda: f"[T]orp: {'ON' if state.torpedo_mode else 'OFF'}", lambda: weapons.toggle_torpedoes(state))
    
    general_text_logic = lambda: f"[G]eneral: {'ON' if state.firing_mode and state.bomb_mode and state.torpedo_mode else ('OFF' if not state.firing_mode and not state.bomb_mode and not state.torpedo_mode else 'Mix')}"
    general_button = Button(pygame.Rect(config.WIDTH - 400, 725, 200, 50), general_text_logic, lambda: weapons.toggle_general(state))

    pause_buttons = [music_button, sounds_button, noise_button, restart_button, achievements_button, firing_button, bomb_button, torpedo_button, general_button]

    return_to_pause_button = Button(pygame.Rect(config.WIDTH - 400, 200, 200, 50), lambda: f"[B]ACK", lambda: setattr(state, "show_achievements", False))
    return_to_game_button = Button(pygame.Rect(config.WIDTH - 400, 275, 200, 50), lambda: f"[P]LAY", lambda: (setattr(state, "game_going", True), setattr(state, "paused", False), setattr(state, "show_achievements", False)))
    achievements_restart_button = Button(pygame.Rect(config.WIDTH - 400, 350, 200, 50), lambda: f"[R]ESTART", lambda: game_flow.attempt_restart(state, screen, reg_font, small_font))
    achievements_buttons = [return_to_pause_button, return_to_game_button, achievements_restart_button]

    return pause_buttons, achievements_buttons, quit_button
