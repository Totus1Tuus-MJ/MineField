## game_events.py

from services import audio
from entities.explosion import Explosion
from systems.upgrade_effects import grant_reward


def handle_events(state, events, sounds):
    for event in events:

        if event["type"] == "enemy_killed":
            state.score += 20
            state.enemies_destroyed += 1

            enemy = event["enemy"]
            state.explosions.append(
                Explosion(enemy.x, enemy.y)
            )

            # Avoid playing the sound many times during a bomb screen clear
            if not event.get("is_bomb_kill"):
                audio.play_sound(state, sounds["enemy"])

        elif event["type"] == "player_hit":
            if state.shields > 0:
                state.shields -= 1
            else:
                state.lives -= 1

            if state.lives <= 0:
                state.game_over = True

        elif event["type"] == "player_hit by planet":
            state.shields = 0
            state.lives = 1
            state.score += 100
            
            planet = event["planet"]
            state.explosions.append(
                Explosion(planet.x, planet.y, max_radius = planet.radius * 3)
            )
            audio.play_sound(state, sounds["bomb_loud"])

        elif event["type"] == "planet_destroyed":
            state.score += 100
            
            planet = event["planet"]
            state.explosions.append(
                Explosion(planet.x, planet.y, max_radius = planet.radius * 3)
            )
            audio.play_sound(state, sounds["enemy"])

        elif event["type"] == "upgrade_collected":
            state.upgrades_collected += 1
            state.score += 30
            grant_reward(state)
            audio.play_sound(state, sounds["upgrade"])

        if event.get("source") == "bomb":
            state.score += 5
