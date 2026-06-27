## spawning.py

import random
import pygame

from core import config
from entities.enemy import Enemy
from entities.upgrade import Upgrade
from entities.background_entities import Planet
from ui.colors import Color


def spawn_planets(state, current_time, planet_sprites):
    if current_time - state.last_planet_spawn > state.planet_spawn_delay:
        state.planets.append(Planet(random.randint(100, config.WIDTH - 100), -200, random.randint(50, 550), random.choice([Color.LIGHT_PURPLE, Color.LIGHT_RED, Color.LIGHT_ORANGE, Color.LIGHT_GREEN]), random.randint(10, 100), random.choice(planet_sprites)))
        state.last_planet_spawn = current_time

def spawn_enemies(state, current_time):
    if current_time - state.last_spawn > state.spawn_delay:
        if len(state.enemies) < state.max_enemies:
            state.enemies.append(Enemy(random.randint(0, config.WIDTH - state.enemy_size), -state.enemy_size, state.enemy_size, state.enemy_speed))
            state.last_spawn = current_time

def spawn_upgrades(state, current_time):
    if current_time - state.last_payload > state.payload_delay:
        if len(state.upgrades) < Upgrade.max_upgrades:
            state.upgrades.append(Upgrade(random.randint(0, config.WIDTH - state.upgrade_size), -state.upgrade_size, 35, state.upgrade_speed, 5))
            state.last_payload = current_time

def spawn_game(state, planet_sprites):
    current_time = pygame.time.get_ticks()

    spawn_planets(state, current_time, planet_sprites)
    
    # Use firing mode specific caps
    current_max = 40 if state.firing_mode else 25
    if len(state.enemies) < current_max:
        spawn_enemies(state, current_time)

    spawn_upgrades(state, current_time)
