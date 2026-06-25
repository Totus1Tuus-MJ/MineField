## main.py

import pygame

from core.state import State
from core import config
from systems.collisions import check_collisions
from systems.movement import move_game
from systems.spawning import spawn_game
from systems.upgrade_effects import update_effects

from rendering.drawing import draw_game

from ui.login_screen import login_screen

import game_logic
import setup
import input

state = State(config.WIDTH, config.HEIGHT)
screen, reg_font, small_font, clock = setup.pre_login_init()

user = login_screen(screen, reg_font, small_font)

if user is None:
    game_logic.stop_game(False, state, sounds)

state.load_user(user)
high_score, sprites, sounds, hud_icons, pause_buttons, achievements_buttons = setup.post_login_init(state, screen, reg_font, small_font)

while True:
    dt = clock.tick(60) / 1000
    keys = pygame.key.get_pressed()

    game_logic.update_difficulty(state)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_logic.stop_game(True, state, sounds)
        if event.type == pygame.KEYDOWN:
            if not state.show_achievements:
                if (event.key == pygame.K_p) or (state.paused and event.key == pygame.K_SPACE):
                    state.show_achievements = False
                    state.paused = not state.paused
                    state.game_going = not state.paused
            if state.game_over and event.key == pygame.K_SPACE:
                high_score = game_logic.attempt_restart(state, screen, reg_font, small_font, )          
        if state.paused:
            input.handle_pause_input(event, state, screen, reg_font, small_font, pause_buttons, achievements_buttons, sounds)

    if state.game_going:
        update_effects(state)
        input.handle_game_going_input(state, keys, sounds, dt)            
        spawn_game(state, sprites["planets"])
        move_game(state, dt, sounds["bomb"])
        check_collisions(state, sounds["death"], sounds["game_over"], sounds["upgrade"], sounds["enemy"], sounds["bomb"], sounds["bomb_loud"])
        achievements.check(state)
    draw_game(screen, state, sprites, reg_font, small_font, high_score, pause_buttons, achievements_buttons, hud_icons)
                                   

    if state.game_over:
        state.game_going = False
        if keys[pygame.K_q]:
            
            game_logic.stop_game(True, state, sounds)
        
    pygame.display.update()
