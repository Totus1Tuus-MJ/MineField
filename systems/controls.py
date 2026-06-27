## controls.py

import pygame
from core import game_flow, config
from services import audio
from systems import weapons

def handle(state, keys):
    """Unified input handler called from main.py."""
    sounds = getattr(state, 'sounds', {})
    
    # Process events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_flow.stop_game(True, state, sounds)
        
        # Global Instruction Toggle
        if event.type == pygame.KEYDOWN and event.key == pygame.K_i:
            state.show_instructions = not state.show_instructions
            if state.show_instructions:
                state.paused = True
                state.game_going = False
            elif not state.show_achievements:
                # Only resume if we aren't also in achievements
                state.paused = False
                state.game_going = True
            continue

        if state.show_instructions:
            handle_instructions_input(event, state)
        elif state.paused:
            handle_pause_input(event, state)
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    state.paused = True
                    state.game_going = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                quit_button = getattr(state, 'quit_button', None)
                if quit_button and quit_button.rect.collidepoint(event.pos):
                    quit_button.click()
        
        if not state.paused and not state.game_going:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_flow.attempt_restart(state, getattr(state, 'screen', None), getattr(state, 'reg_font', None), getattr(state, 'small_font', None))

    if state.game_going:
        handle_game_going_input(state, keys)

def handle_instructions_input(event, state):
    sounds = getattr(state, 'sounds', {})
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_q:
            game_flow.stop_game(True, state, sounds)
    elif event.type == pygame.MOUSEBUTTONDOWN:
        quit_button = getattr(state, 'quit_button', None)
        if quit_button and quit_button.rect.collidepoint(event.pos):
            quit_button.click()

def handle_pause_input(event, state):
    sounds = getattr(state, 'sounds', {})
    pause_buttons = getattr(state, 'pause_buttons', [])
    achievements_buttons = getattr(state, 'achievements_buttons', [])
    
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_q:
            game_flow.stop_game(True, state, sounds)
            return
        elif event.key == pygame.K_r:
            game_flow.attempt_restart(state, getattr(state, 'screen', None), getattr(state, 'reg_font', None), getattr(state, 'small_font', None))
            return
        if event.key == pygame.K_a and state.paused:
            state.show_achievements = not state.show_achievements
            return
        if event.key in [pygame.K_p, pygame.K_SPACE]:
            state.paused = False
            state.game_going = True
            state.show_achievements = False
            state.show_instructions = False
            return

    if not state.show_achievements:
        if event.type == pygame.MOUSEBUTTONDOWN:
            quit_button = getattr(state, 'quit_button', None)
            if quit_button and quit_button.rect.collidepoint(event.pos):
                quit_button.click()
            for button in pause_buttons:
                if button.rect.collidepoint(event.pos):
                    button.click()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                audio.toggle_sounds(state)
            elif event.key == pygame.K_m:
                audio.toggle_music(state)
            elif event.key == pygame.K_n:
                audio.toggle_noises(state)
            elif event.key == pygame.K_f:
                weapons.toggle_firing(state)
            elif event.key == pygame.K_b:
                weapons.toggle_bombs(state)
            elif event.key == pygame.K_t:
                weapons.toggle_torpedoes(state)
            elif event.key == pygame.K_g:
                weapons.toggle_general(state)

    elif state.show_achievements:
        if event.type == pygame.MOUSEBUTTONDOWN:
            quit_button = getattr(state, 'quit_button', None)
            if quit_button and quit_button.rect.collidepoint(event.pos):
                quit_button.click()
            for button in achievements_buttons:
                if button.rect.collidepoint(event.pos):
                    button.click()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_b:
                state.show_achievements = False


def handle_game_going_input(state, keys):
    sounds = getattr(state, 'sounds', {})
    dt = getattr(state, 'dt', 0.016)

    state.player.move(keys, dt, config.WIDTH, config.HEIGHT)

    movement_keys = (pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d)
    moving = any(keys[k] for k in movement_keys)
    
    if moving:
        if not state.movement_sound_playing:
            if "player_movement" in sounds:
                sounds["player_movement"].play(-1)
                state.movement_sound_playing = True
    else:
        if state.movement_sound_playing:
            if "player_movement" in sounds:
                sounds["player_movement"].stop()
            state.movement_sound_playing = False
    if state.firing_mode:
        if keys[pygame.K_SPACE]:
            if weapons.fire_gun(state):
                audio.play_sound(state, sounds.get("bullet"))
    if state.bomb_mode:
        if keys[pygame.K_b]:
            if weapons.launch_bomb(state):
                audio.play_sound(state, sounds.get("bomb"))
    if state.torpedo_mode:
        if keys[pygame.K_t]:
            if weapons.launch_torpedo(state):
                audio.play_sound(state, sounds.get("torpedo"))
    if keys[pygame.K_r]:
        game_flow.attempt_restart(state, getattr(state, 'screen', None), getattr(state, 'reg_font', None), getattr(state, 'small_font', None))

    if keys[pygame.K_q]:
        game_flow.stop_game(True, state, sounds)
