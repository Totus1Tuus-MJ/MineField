## input.py

import pygame
import config
import game_logic
import audio
import weapons

def handle_pause_input(event, state, screen, reg_font, small_font, pause_buttons, achievements_buttons, sounds):
    if not state.show_achievements:
        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in pause_buttons:
                if button.rect.collidepoint(event.pos):
                    button.click()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                audio.toggle_sounds(state)
            elif event.key == pygame.K_m:
                audio.toggle_music(state)
            elif event.key == pygame.K_q:
                game_logic.stop_game(True, state, sounds)
            elif event.key == pygame.K_r:
                game_logic.attempt_restart(state, screen, reg_font, small_font)
            elif event.key == pygame.K_a:
                state.show_achievements = True
    else:
        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in achievements_buttons:
                if button.rect.collidepoint(event.pos):
                    button.click()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_b:
                state.show_achievements = False
            elif event.key in [pygame.K_p, pygame.K_SPACE]:
                state.game_going = True
                state.paused = False
                state.show_achievements = False
            elif event.key == pygame.K_q:
                game_logic.stop_game(True, state, sounds)
            elif event.key == pygame.K_r:
                game_logic.attempt_restart(state, screen, reg_font, small_font)
            elif event.key == pygame.K_a:
                state.show_achievements = False
  

def handle_game_going_input(state, keys, sounds, dt):

    state.player.move(keys, dt, config.WIDTH, config.HEIGHT)
    if state.game_going:
        moving = any([keys[pygame.K_RIGHT], keys[pygame.K_UP],
                      keys[pygame.K_DOWN], keys[pygame.K_LEFT],
                      keys[pygame.K_w], keys[pygame.K_a],
                      keys[pygame.K_s], keys[pygame.K_d]])
        if moving:
            if not state.movement_sound_playing:
                sounds["player_movement"].play(-1)
                state.movement_sound_playing = True

            else:
                if state.movement_sound_playing == True:
                    sounds["player_movement"].stop()
                    state.movement_sound_playing = False
                    
            
        if keys[pygame.K_SPACE]:
            if weapons.fire_gun(state):
                audio.play_sound(state, sounds["bullet"])

        if keys[pygame.K_b]:
            weapons.launch_bomb(state)

        if keys[pygame.K_t]:
            if weapons.launch_torpedo(state):
                audio.play_sound(state, sounds["torpedo"])

    if keys[pygame.K_q]:
        game_logic.stop_game(True, state, sounds)


