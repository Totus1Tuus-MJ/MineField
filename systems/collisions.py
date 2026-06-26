
import pygame
import math

def check_collisions(state):
    events = []

    events += bullet_enemy_collisions(state)
    events += player_enemy_collisions(state)
    events += upgrade_player_collisions(state)
    events += torpedo_enemy_collisions(state)
    events += torpedo_planet_collisions(state)
    events += torpedo_upgrade_collisions(state)
    events += bomb_collisions(state)
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
                "enemy": enemy,
                "source": "player"
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
                "source": "player",
                "upgrade": upgrade,
                "is_bomb_kill": False
            })

    return events


def torpedo_enemy_collisions(state):
    events = []

    for torpedo in state.torpedoes:
        t_rect = torpedo.rect()

        for enemy in state.enemies[:]:
            if t_rect.colliderect(enemy.rect()):
                state.enemies.remove(enemy)
                events.append({
                    "type": "enemy_killed",
                    "source": "torpedo",
                    "enemy": enemy,
                    "is_bomb_kill": False
                })
    return events

def torpedo_planet_collisions(state):
    events = []
    for torpedo in state.torpedoes:
        t_rect = torpedo.rect()
        for planet in state.planets[:]:
            if t_rect.colliderect(planet.rect()):
                state.planets.remove(planet)
                state.planets_destroyed += 1
                events.append({
                    "type": "planet_destroyed",
                    "source": "torpedo",
                    "planet": planet,
                    "is_bomb_kill": False
                })
    return events

def torpedo_upgrade_collisions(state):
    for torpedo in state.torpedoes:
        t_rect = torpedo.rect()
        for upgrade in state.upgrades[:]:
            if upgrade.collides_with(t_rect):
                state.upgrades.remove(upgrade)
    return []

def bomb_collisions(state):
    events = []
    
    for bomb in state.bomb_list[:]:
        if bomb.detonated:
            for enemy in state.enemies[:]:
                state.enemies.remove(enemy)
                events.append({
                    "type": "enemy_killed",
                    "source": "bomb",
                    "enemy": enemy,
                    "is_bomb_kill": True
                })
            
            for planet in state.planets[:]:
                state.planets.remove(planet)
                state.planets_destroyed += 1
                events.append({
                    "type": "planet_destroyed",
                    "source": "bomb",
                    "planet": planet,
                    "is_bomb_kill": True
                })
            
            for upgrade in state.upgrades[:]:
                state.upgrades.remove(upgrade)
                events.append({
                    "type": "upgrade_destroyed",
                    "source": "bomb",
                    "upgrade": upgrade,
                    "is_bomb_kill": False
                })
            
            state.bomb_list.remove(bomb)
            
    return events

def player_planet_collisions(state):
    events = []
    player_rect = state.player.rect(state.shields)
    
    for planet in state.planets[:]:
        if player_rect.colliderect(planet.rect()):
            state.planets.remove(planet)
            events.append({
                "type": "player_hit by planet",
                "source": "player",
                "planet": planet,
                "is_bomb_kill": False
            })
    return events
