## upgrade_effects.py

import pygame
import random

def add_temporary_effect(state, name, duration_ms):
    expiration = pygame.time.get_ticks() + duration_ms
    state.active_effects.append({"name": name, "expires": expiration})

def update_effects(state):
    current_time = pygame.time.get_ticks()

    for effect in state.active_effects[:]:
        if current_time >= effect["expires"]:

            if effect["name"] == "Larger Bullets":
                state.bullet_size -= 5

            elif effect["name"] == "Faster Reload":
                state.reload_cooldown += 10

            elif effect["name"] == "Faster Bullets":
                state.bullet_speed -= 100

            elif effect["name"] == "Upgrades Fall Slower":
                state.upgrade_slowdown += 25
                
            elif effect["name"] == "Upgrades Deposit Faster":
                state.payload_delay -= 200
                
            elif effect["name"] == "Enemies Spawn Slower":
                state.spawn_delay_benefit -= 25

            state.active_effects.remove(effect)


def grant_reward(state):
    effects = ["Larger Bullets","+2 Bombs",
        "+5 Torpedoes","Upgrades Fall Slower",
        "Upgrades Deposit Faster","Enemies Spawn Slower",
        "+1 Life","Faster Reload",
        "Faster Bullets","Earn Bombs Faster",
        "Earn Torpedoes Faster", "Shield Power-Up"]
    state.effect = random.choice(effects)
    if state.effect == "Larger Bullets":
        state.bullet_size += 5
        add_temporary_effect(state, "Larger Bullets", 15000)

    elif state.effect == "+2 Bombs":
        state.bombs += 2

    elif state.effect == "+5 Torpedoes":
        state.torpedo_count += 5

    elif state.effect == "Upgrades Fall Slower":
        state.upgrade_slowdown += 25
        add_temporary_effect(state, "Upgrades Fall Slower", 15000)

    elif state.effect == "Upgrades Deposit Faster":
        state.payload_delay = max(500, state.payload_delay - 200)
        add_temporary_effect(state, "Upgrades Deposit Faster", 15000)

    elif state.effect == "Enemies Spawn Slower":
        state.spawn_delay_benefit += 25
        add_temporary_effect(state, "Enemies Spawn Slower", 15000)


    elif state.effect == "+1 Life":
        state.lives += 1

    elif state.effect == "Faster Reload":
        state.reload_cooldown = max(25, state.reload_cooldown - 10)
        add_temporary_effect(state, "Faster Reload", 15000)


    elif state.effect == "Faster Bullets":
        state.bullet_speed = min(state.max_bullet_speed, state.bullet_speed + 100)
        add_temporary_effect(state, "Faster Bullets", 15000)


    elif state.effect == "Earn Bombs Faster":
        state.bomb_gain_interval = max(25, state.bomb_gain_interval - 10)

    elif state.effect == "Earn Torpedoes Faster":
        state.torpedo_gain_interval = max(10, state.torpedo_gain_interval - 5)

    elif state.effect == "Shield Power-Up":
        state.shields = min(12, state.shields + 2)
