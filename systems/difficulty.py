## difficulty.py

def update_difficulty(state):
    state.enemy_speed = min (state.max_enemy_speed, 250 + state.score ** 0.75)
    state.spawn_delay = max(state.min_spawn_delay, 500 - (state.score * 0.5) + state.spawn_delay_benefit)
    state.upgrade_speed = state.enemy_speed + 5
    state.shields = min(state.shields, 12)
    
    state.bombs, state.bomb_checkpoint = collect_firearms(state.score, state.bomb_checkpoint, state.bomb_gain_interval, state.bombs)
    
    state.torpedo_count, state.torpedo_checkpoint = collect_firearms(state.score, state.torpedo_checkpoint, state.torpedo_gain_interval, state.torpedo_count)
    
    # Dynamic Accuracy Update
    state.accuracy = state.hits / state.shots_fired if state.shots_fired > 0 else 1.0

def collect_firearms(score, firearm_checkpoint, firearm_gain_interval, firearms):
    while score >= firearm_checkpoint + firearm_gain_interval:
        firearm_checkpoint += firearm_gain_interval
        firearms += 1
    return firearms, firearm_checkpoint

def update_difficulty_modes(state):
    if state.firing_mode or state.bomb_mode or state.torpedo_mode:
        state.max_enemies = 40
        state.max_enemy_speed = 1500
        state.min_spawn_delay = 10
    else:
        state.max_enemies = 25
        state.max_enemy_speed = 700
        state.min_spawn_delay = 25