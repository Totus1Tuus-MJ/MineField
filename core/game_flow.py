## game_logic.py

import pygame
import sys

import achievements
import audio
import background
import config
import login
from ui import message_screen
import weapons

def stop_game(should_play_sound, state, sounds = None):
    if should_play_sound and sounds:
        audio.play_sound(state, sounds["game_over"])
        pygame.time.wait(3000)
    pygame.quit()
    sys.exit()


def update_difficulty(state):
    state.enemy_speed = min (state.max_enemy_speed, 250 + state.score ** 0.75)
    state.spawn_delay = max(state.min_spawn_delay, 500 - (state.score * 0.5) + state.spawn_delay_benefit)
    state.upgrade_speed = state.enemy_speed + 5
    state.shields = min(state.shields, 12)
    state.torpedo_count, state.torpedo_checkpoint = weapons.collect_firearms(state.score, state.torpedo_checkpoint, state.torpedo_gain_interval, state.torpedo_count)    

    state.bombs, state.bomb_checkpoint = weapons.collect_firearms(state.score, state.bomb_checkpoint, state.bomb_gain_interval, state.bombs)
  
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
    
    message_screen(screen, reg_font, small_font, "ACCESS DENIED", "You do not have enough tokens.", "Please contact an administator to purchase more tokens.")
    stop_game(False, state, sounds)
        
