## difficulty.py

from systems import weapons
def update_difficulty(state):
    state.enemy_speed = min (state.max_enemy_speed, 250 + state.score ** 0.75)
    state.spawn_delay = max(state.min_spawn_delay, 500 - (state.score * 0.5) + state.spawn_delay_benefit)
    state.upgrade_speed = state.enemy_speed + 5
    state.shields = min(state.shields, 12)

