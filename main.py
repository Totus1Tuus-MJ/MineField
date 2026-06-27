## main.py

import pygame

from core import game_flow, game_events, setup, config
from core.state import State
import systems
from systems.difficulty import update_difficulty
import rendering.renderer as rendering
from ui.login_screen import login_screen
from services import login

state = State(width=1550, height=950)
screen, reg_font, small_font, clock = setup.pre_login_init()

user = login_screen(screen, reg_font, small_font, quit_button = None)

if user is None:
    game_flow.stop_game(False, state, None)

state.load_user(user)
high_score, sprites, sounds, hud_icons, pause_buttons, achievements_buttons, quit_button = setup.post_login_init(state, screen, reg_font, small_font)

running = True
while running:

    dt = clock.tick(60) / 1000
    state.dt = dt
    keys = pygame.key.get_pressed()

    # 1. INPUT
    systems.controls.handle(state, keys)

    if state.game_going:
        # 3. MOVEMENT
        systems.movement.move_game(state, dt)

        # 4. COLLISIONS → EVENTS
        events = systems.collisions.check_collisions(state)

        # 5. RESOLVE EVENTS
        game_events.handle_events(state, events, sounds)

        # 6. DIFFICULTY (IMPORTANT: keep here for now)
        update_difficulty(state)

        # 7. SPAWNING
        systems.spawning.spawn_game(state, sprites["planets"])

        # 9. ACHIEVEMENTS
        systems.achievements.check(state)

    # 8. RENDER
    rendering.draw_game(screen, state, sprites, reg_font, small_font, high_score, pause_buttons, achievements_buttons, hud_icons, quit_button)

    # Update highscore and award token in session
    if state.score > high_score:
        high_score = state.score
        config.save_highscore(high_score)
        # Award token for beating highscore (only once per session when passing it)
        if not getattr(state, "highscore_token_awarded", False):
            login.add_token(state.current_user["username"], state.current_user)
            state.highscore_token_awarded = True

    pygame.display.flip()

    if state.game_over:
        state.game_going = False
        if keys[pygame.K_q]:

            game_flow.stop_game(True, state, sounds)
