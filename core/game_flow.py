## game_flow.py

import pygame
import sys

import services.audio
from  rendering import background
import config
from services import login
import ui.ui

def stop_game(should_play_sound, state, sounds = None):
    if should_play_sound and sounds:
        services.audio.play_sound(state, sounds["game_over"])
        pygame.time.wait(3000)
    pygame.quit()
    sys.exit()



def restart_game(state):
    state.restart(config.WIDTH, config.HEIGHT)
    background.init(state)
    state.game_over_sound_played = False
    high_score = config.load_highscore()
    return high_score


def attempt_restart(state, screen, reg_font, small_font, sounds = None):
    user = getattr(state, "current_user", None)
    if user and login.spend_token(state.current_user["username"]):
        return restart_game(state)
    
    ui.ui.message_screen(screen, reg_font, small_font, "ACCESS DENIED", "You do not have enough tokens.", "Please contact an administator to purchase more tokens.", quit_button = None)
    stop_game(False, state, sounds)
    return None
        
