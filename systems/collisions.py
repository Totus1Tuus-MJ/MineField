## collision.py

from core import game_flow
from services import audio
from systems.upgrade_effects import grant_reward
from entities.explosion import Explosion

import pygame
import math

def check_collisions(state):
    events = []

    events += bullet_enemy_collisions(state)
    events += player_enemy_collisions(state)
    events += upgrade_player_collisions(state)
    events += torpedo_enemy_collisions(state)
    events += bomb_enemy_collisions(state)
    events += player_planet_collisions(state)

    return events


def bullet_enemy_collisions(state):
    events = []

    for bullet in state.bullets[:]:
        bullet_rect = bullet.rect()

        for enemy in state.enemies[:]:
            if bullet_rect.colliderect(enemy.rect()):
                if bullet in state.bullets:
                    state.bullets.remove(bullet)
                state.enemies.remove(enemy)

                events.append({
                    "type": "enemy_killed",
                    "source": "bullet",
                    "enemy": enemy
                })
                break

    return events


def player_enemy_collisions(state):
    events = []

    player_rect = state.player.rect(state.shields)

    for enemy in state.enemies[:]:
        if player_rect.colliderect(enemy.rect()):
            state.enemies.remove(enemy)

            events.append({
                "type": "player_hit",
                "enemy": enemy
            })

    return events


def upgrade_player_collisions(state):
    events = []

    player_rect = state.player.rect(state.shields)

    for upgrade in state.upgrades[:]:
        if upgrade.collides_with(player_rect):
            state.upgrades.remove(upgrade)

            events.append({
                "type": "upgrade_collected",
                "upgrade": upgrade
            })

    return events


def torpedo_enemy_collisions(state):
    events = []

    for torpedo in state.torpedoes[:]:
        t_rect = torpedo.rect()

        for enemy in state.enemies[:]:
            if t_rect.colliderect(enemy.rect()):
                state.enemies.remove(enemy)
                if torpedo in state.torpedoes:
                    state.torpedoes.remove(torpedo)

                events.append({
                    "type": "enemy_killed",
                    "source": "torpedo",
                    "enemy": enemy
                })
                break

    return events

def bomb_enemy_collisions(state):
    events = []
    
    for bomb in state.bomb_list[:]:
        if bomb.detonated:
            for enemy in state.enemies[:]:
                # Distance check (center to center)
                ex = enemy.x + enemy.size / 2
                ey = enemy.y + enemy.size / 2
                
                dx = bomb.x - ex
                dy = bomb.y - ey
                distance = math.sqrt(dx*dx + dy*dy)
                
                if distance <= bomb.radius:
                    state.enemies.remove(enemy)
                    events.append({
                        "type": "enemy_killed",
                        "source": "bomb",
                        "enemy": enemy
                    })
            
            # Remove bomb after detonation effect
            state.bomb_list.remove(bomb)
            
    return events

def player_planet_collisions(state):
    events = []
    player_rect = state.player.rect(state.shields)
    
    for planet in state.planets[:]:
        if player_rect.colliderect(planet.rect()):
            state.planets.remove(planet)
            events.append({
                "type": "player_hit",
                "planet": planet
            })
    return events
