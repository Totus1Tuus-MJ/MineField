## movement.py

import random
from services import audio
import config
from entities.explosion import Explosion
from entities.upgrade import Upgrade

def move_planets(state, dt):
    for planet in state.planets[:]:
        planet.move(dt)

        if planet.off_screen(config.HEIGHT):
            state.planets.remove(planet)

def move_stars(state, dt):
    for star in state.stars:
        star.move(dt, state.score)

        if star.off_screen(config.HEIGHT):
            star.reset(config.WIDTH)

def move_enemies(state, dt):
    for enemy in state.enemies[:]:
        enemy.move(dt)

        if enemy.off_screen(config.HEIGHT):
            state.enemies.remove(enemy)

def move_upgrades(state, dt):
    for upgrade in state.upgrades[:]:
        upgrade.move(dt, state.upgrade_slowdown)

        if upgrade.off_screen(config.HEIGHT):
            state.upgrades.remove(upgrade)

def move_bullets(state, dt):
    for bullet in state.bullets[:]:
        bullet.move(dt)

        if bullet.off_screen():
            state.bullets.remove(bullet)

def move_torpedoes(state, dt):
    for torpedo in state.torpedoes[:]:
        torpedo.move(dt)

        if torpedo.off_screen():
            state.torpedoes.remove(torpedo)

def move_bombs(state, dt):
    for bomb in state.bomb_list:
        bomb.move(dt)

 
def move_explosions(state, dt):
    for explosion in state.explosions[:]:
        explosion.move(dt)

        if explosion.finished:
            state.explosions.remove(explosion)

def move_game(state, dt):
    move_planets(state, dt)
    move_stars(state, dt)
    move_enemies(state, dt)
    move_upgrades(state, dt)
    move_bullets(state, dt)
    move_torpedoes(state, dt)
    move_bombs(state, dt)
    move_explosions(state, dt)
    
