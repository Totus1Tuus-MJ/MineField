## collision.py

import game_logic
import audio
from upgrade_effects import grant_reward
from explosion import Explosion

def player_enemy_collision(state, death_sound, game_over_sound):

    player_rect = state.player.rect(state.shields)

    for enemy in state.enemies[:]:

        if player_rect.colliderect(enemy.rect()):
            audio.play_sound(state, death_sound)
            state.enemies.remove(enemy)
            state.enemies_destroyed += 1

            if state.shields > 0:
                state.shields -= 1
                state.shields_lost += 1

            else:
                state.lives -= 1
                state.lives_lost += 1

            if state.lives <= 0:
                audio.play_sound(state, game_over_sound)                    
                state.game_over = True
                state.game_going = False

            break

def player_upgrade_collision(state, upgrade_sound):

    player_expanded_rect = state.player.expanded_rect()

    for upgrade in state.upgrades[:]:

        if player_expanded_rect.colliderect(upgrade.rect()):
            audio.play_sound(state, upgrade_sound)
            state.upgrades_collected +=1
            state.score += 25
            state.upgrades.remove(upgrade)
            grant_reward(state)

def player_planet_collision(state, bomb_loud_sound):

    player_rect = state.player.rect(state.shields)

    for planet in state.planets[:]:

        if player_rect.colliderect(planet.rect()):
            state.shields = 0
            state.lives = 1
            state.planets_destroyed += 1
            state.planet_collisions += 1
            state.planets.remove(planet)
            state.explosions.append(Explosion(int(planet.x), int(planet.y), planet.radius * 3))
            state.explosions.append(Explosion(int(state.player.x), int(state.player.y), state.player.size * 2))
            audio.play_sound(state, bomb_loud_sound)
            state.score += 100
                
def bullet_enemy_collision(state, enemy_sound):

    for bullet in state.bullets[:]:
            
        for enemy in state.enemies[:]:
            
            if bullet.collides_with(enemy.rect()):
                audio.play_sound(state, enemy_sound)
                state.explosions.append(Explosion(enemy.x + enemy.size // 2, enemy.y + enemy.size // 2))
                state.enemies.remove(enemy)
                state.enemies_destroyed += 1
                state.bullets.remove(bullet)
                state.score += 5
                state.hits +=1
                state.accuracy = state.hits / state.shots_fired
                break

def torpedo_enemy_collision(state):

    for torpedo in state.torpedoes[:]:            

        for enemy in state.enemies[:]:

                if torpedo.collides_with(enemy.rect()):
                    state.explosions.append(Explosion(enemy.x + enemy.size // 2, enemy.y + enemy.size // 2))
                    state.enemies.remove(enemy)
                    state.enemies_destroyed += 1
                    state.score += 50

def torpedo_planet_collision(state, bomb_sound):

    for torpedo in state.torpedoes[:]:

        for planet in state.planets[:]:

            if torpedo.collides_with(planet.rect()):
                audio.play_sound(state, bomb_sound)
                state.explosions.append(Explosion(int(planet.x), int(planet.y), planet.radius))
                state.planets.remove(planet)
                state.score += 150

def check_collisions(state, death_sound, game_over_sound, upgrade_sound, enemy_sound, bomb_sound, bomb_loud_sound):
    player_enemy_collision(state, death_sound, game_over_sound)
    player_upgrade_collision(state, upgrade_sound)
    player_planet_collision(state, bomb_loud_sound)
    bullet_enemy_collision(state, enemy_sound)
    torpedo_enemy_collision(state)
    torpedo_planet_collision(state, bomb_sound)
                           
