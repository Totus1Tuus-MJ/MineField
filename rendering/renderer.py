## drawing.py
from ui.colors import Color
from ui.ui import draw_hud, draw_game_over, draw_pause_menu, draw_achievements_screen


import config

def draw_game(screen, state, sprites, reg_font, small_font, high_score, pause_buttons, achievements_buttons, hud_icons, quit_button):
    screen.fill(Color.BLACK)

    for planet in state.planets:
        planet.draw(screen)
    for star in state.stars:
        star.draw(screen)
    for enemy in state.enemies:
        enemy.draw(screen, sprites["enemy"])
    for upgrade in state.upgrades:
        upgrade.draw(screen, sprites["upgrade"])
    for bullet in state.bullets:
        bullet.draw(screen, sprites["bullet"])
    for torpedo in state.torpedoes:
        torpedo.draw(screen, sprites["torpedo"])
    for bomb in state.bomb_list:
        bomb.draw(screen, sprites["bomb"])
    for explosion in state.explosions:
        explosion.draw(screen, Color.ORANGE)

    state.player.draw(screen, sprites["player"], Color.GREEN, state.shields, 1)

    draw_hud(screen, state, reg_font, small_font, high_score, hud_icons, quit_button)

    if state.game_over:
        performance = config.calc_performance(state.score, high_score)
        draw_game_over(screen, state, reg_font, small_font, performance, quit_button)

    if state.paused:
        if not state.show_achievements:
            draw_pause_menu(screen, state, reg_font, pause_buttons, quit_button)
        else:
            draw_achievements_screen(screen, state, reg_font, small_font, achievements_buttons, quit_button)


