## weapons.py

import pygame
from entities.bullet import Bullet
from entities.bomb import Bomb
from entities.torpedo import Torpedo
from systems import difficulty


def fire_gun(state):
    current_time = pygame.time.get_ticks()

    if current_time - state.last_shot > state.reload_cooldown:
        bullet = Bullet(
            state.player.x + state.player.size // 2 - state.bullet_size // 2,
            state.player.y - state.player.size,
            state.bullet_size,
            state.bullet_speed
        )

        state.bullets.append(bullet)
        state.last_shot = current_time
        state.shots_fired += 1

        return True

    return False


def launch_bomb(state):
    current_time = pygame.time.get_ticks()

    if state.bombs > 0 and (current_time - state.last_bombed > state.bomb_wait_time):
        state.bombs -= 1
        state.bombs_used += 1

        bomb = Bomb(
            state.player.x + state.player.size // 2,
            state.player.y
        )

        state.bomb_list.append(bomb)
        state.last_bombed = current_time

        return True

    return False


def launch_torpedo(state):
    current_time = pygame.time.get_ticks()

    if state.torpedo_count > 0 and (current_time - state.last_torpedoed > state.torpedo_reload):
        cx, cy = state.player.center()

        torpedo = Torpedo(
            cx - state.torpedo_x_size // 2,
            cy - state.player.size,
            state.torpedo_speed,
            state.torpedo_x_size,
            state.torpedo_y_size
        )

        state.torpedoes.append(torpedo)
        state.torpedo_count -= 1
        state.torpedoes_used += 1
        state.last_torpedoed = current_time

        return True

    return False


def toggle_firing(state):
    state.firing_mode = not state.firing_mode
    difficulty.update_difficulty_modes(state)
    if not state.firing_mode:
        state.bullets = []

def toggle_bombs(state):
    state.bomb_mode = not state.bomb_mode
    difficulty.update_difficulty_modes(state)
    if not state.bomb_mode:
        state.bomb_list = []

def toggle_torpedoes(state):
    state.torpedo_mode = not state.torpedo_mode
    difficulty.update_difficulty_modes(state)
    if not state.torpedo_mode:
        state.torpedoes = []

def toggle_general(state):
    # If any mode is ON, turn them all OFF.
    if state.firing_mode or state.bomb_mode or state.torpedo_mode:
        state.firing_mode = False
        state.bomb_mode = False
        state.torpedo_mode = False
        state.bullets = []
        state.bomb_list = []
        state.torpedoes = []
    else:
        # If all were OFF, turn them all ON.
        state.firing_mode = True
        state.bomb_mode = True
        state.torpedo_mode = True
    difficulty.update_difficulty_modes(state)
