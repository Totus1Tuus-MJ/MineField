## state.py

import pygame
from entities.player import Player
from systems import achievements

class State:
    def __init__(self, width, height):
        self.current_user = None
        self.width = width
        self.height = height
        self.restart(width, height)


    def load_user(self, user):
        self.current_user = user
        achievements.load_completed(self)
        
    def restart(self, width, height):

        ## ==========================================
        ## Game FLAGS
        ## ==========================================


        ## Game
        self.game_going = True
        self.show_achievements = False
        self.show_instructions = False
        self.game_over = False
        self.paused = False
        self.music_off = False
        self.sounds_off = False
        self.movement_sound_playing = False
        self.firing_mode = True
        self.bomb_mode = True
        self.torpedo_mode = True

        ## ==========================================

        ## Player
        ## ==========================================


        self.player = Player(width // 2, height - 25, 25, 750, 400)
        self.lives = 3
        self.shields = 0


        ## ==========================================

        ## Scores / Stats
        ## ==========================================

        self.score = 0
        self.hits = 0
        self.shots_fired = 0

        self.enemies_destroyed = 0
        self.upgrades_collected = 0
        self.bombs_used = 0
        self.bomb_kills = 0
        self.planets_destroyed = 0
        self.planet_collisions = 0
        self.torpedoes_used = 0
        self.shields_lost = 0
        self.lives_lost = 0


        ## ==========================================
        ## Enemies
        ## ==========================================
        self.enemies = []
        self.enemy_size = 50

        self.enemy_speed = 250
        self.spawn_delay = 500
        self.last_spawn = 0
        self.spawn_delay_benefit = 0


        if self.firing_mode:
            self.max_enemies = 40
            self.max_enemy_speed = 1500
            self.min_spawn_delay = 10
        else:
            self.max_enemies = 25
            self.max_enemy_speed = 700
            self.min_spawn_delay = 25


        ## ==========================================
        ## Bullets
        ## ==========================================
        self.bullets = []
        self.bullet_size = 15
        self.bullet_speed = 1500
        self.reload_cooldown = 100
        self.last_shot = 0
        self.accuracy = self.hits / self.shots_fired if self.shots_fired else 1

        self.max_bullet_speed = 2500

        ## ==========================================
        ## Bombs
        ## ==========================================
        self.last_bombed = 0
        self.bombs = 1
        self.bomb_list = []
        self.bomb_checkpoint = 0
        self.bomb_gain_interval = 250

        self.bomb_wait_time = 2000

        ## ==========================================
        ## Torpedoes
        ## ==========================================
        self.torpedoes = []
        self.torpedo_gain_interval = 100
        self.torpedo_count = 5
        self.last_torpedoed = 0
        self.torpedo_checkpoint = 0

        self.torpedo_x_size = 67
        self.torpedo_y_size = 100
        self.torpedo_speed = 1200
        self.torpedo_reload = 2500

        ## ==========================================
        ## Upgrades
        ## ==========================================
        self.upgrades = []
        self.upgrade_speed = self.enemy_speed + 5
        self.upgrade_slowdown = 0
        self.payload_delay = 2500
        self.last_payload = 0
        self.upgrades_collected = 0
        self.effect = None
        self.active_effects = []

        self.min_upgrade_speed = 5
        self.upgrade_size = 35

        ## ==========================================
        ## WORLD
        ## ==========================================
        self.stars = []
        self.planets = []
        self.last_planet_spawn = 0
        self.planet_spawn_delay = 15000

        ## ==========================================
        ## Explosions
        ## ==========================================
        self.explosions = []

        ## ==========================================
        ## Achievements
        ## ==========================================
        self.achievements = achievements.load_achievements()
        achievements.load_completed(self)
        self.achievements_completed, self.total_achievements = achievements.get_achievement_progress(self)
        self.achievement_message = ""
        self.achievement_timer = 0

        self.damage_timer = 0
        self.highscore_token_awarded = False
        self.stabilization_time = 3000
