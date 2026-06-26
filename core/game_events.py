## game_events.py

from services import audio
from entities.explosion import Explosion
from systems.upgrade_effects import grant_reward


def handle_events(state, events, sounds):
    for event in events:

        if event["type"] == "enemy_killed":
            state.score += 10
            state.enemies_destroyed += 1

            enemy = event["enemy"]
            state.explosions.append(
                Explosion(enemy.x, enemy.y)
            )

            audio.play_sound(state, sounds["enemy"])


        elif event["type"] == "player_hit":
            if state.shields > 0:
                state.shields -= 1
            else:
                state.lives -= 1

            if state.lives <= 0:
                state.game_over = True


        elif event["type"] == "upgrade_collected":
            state.upgrades_collected += 1
            state.score += 25
            grant_reward(state)
            audio.play_sound(state, sounds["upgrade"])