## asset_loader.py

import pygame

def load_images(state):
    sprites = {}
    sprites["player"] = pygame.image.load("assets/images/player.png").convert_alpha()
    sprites["enemy"] = pygame.image.load("assets/images/enemy.png").convert()
    sprites["bullet"] = pygame.image.load("assets/images/bullet.png").convert()
    sprites["upgrade"] = pygame.image.load("assets/images/upgrade.png").convert_alpha()
    sprites["torpedo"] = pygame.image.load("assets/images/torpedo.png").convert_alpha()
    sprites["bomb"] = pygame.image.load("assets/images/bomb.png").convert_alpha()

    sprites["planets"] = []
    
    for planet_number in range (1, 7):
        sprites["planets"].append(pygame.image.load(f"assets/images/planet_{planet_number}.png").convert_alpha())


    sprites["player"] = pygame.transform.scale(sprites["player"],(state.player.size, state.player.size))
    sprites["enemy"] = pygame.transform.scale(sprites["enemy"],(state.enemy_size, state.enemy_size))
    sprites["bullet"] = pygame.transform.scale(sprites["bullet"],(state.bullet_size, state.bullet_size))
    sprites["upgrade"] = pygame.transform.scale(sprites["upgrade"],(state.upgrade_size, state.upgrade_size))
    sprites["torpedo"] = pygame.transform.scale(sprites["torpedo"],(state.torpedo_x_size, state.torpedo_y_size))
    
    return sprites

def load_sounds():

    sounds = {}
    sounds["bullet"] = pygame.mixer.Sound("assets/sounds/bullet.mp3")
    sounds["enemy"] = pygame.mixer.Sound("assets/sounds/enemy.mp3")
    sounds["upgrade"] = pygame.mixer.Sound("assets/sounds/upgrade.mp3")
    sounds["torpedo"] = pygame.mixer.Sound("assets/sounds/torpedo.mp3")
    sounds["bomb"] = pygame.mixer.Sound("assets/sounds/bomb.mp3")
    sounds["game_over"] = pygame.mixer.Sound("assets/sounds/game_over.mp3")
    sounds["player_movement"] = pygame.mixer.Sound("assets/sounds/player_movement.mp3")
    sounds["death"] = pygame.mixer.Sound("assets/sounds/impact.mp3")
    sounds["bomb_loud"] = pygame.mixer.Sound("assets/sounds/bomb.mp3")

    sounds["bullet"].set_volume(0.025)
    sounds["enemy"].set_volume(0.2)
    sounds["upgrade"].set_volume(0.5)
    sounds["torpedo"].set_volume(0.3)
    sounds["bomb"].set_volume(0.7)
    sounds["game_over"].set_volume(0.9)
    sounds["player_movement"].set_volume(0.1)
    sounds["death"].set_volume(0.9)
    sounds["bomb_loud"].set_volume(1)

    return sounds

def load_hud_icons():
    icons = {}
    icons["token"] = pygame.image.load("assets/hud/token.png").convert_alpha()
    icons["heart"] = pygame.image.load("assets/hud/heart.png").convert_alpha()
    icons["shield"] = pygame.image.load("assets/hud/shield.png").convert_alpha()
    icons["score"] = pygame.image.load("assets/hud/score.png").convert_alpha()
    icons["high_score"] = pygame.image.load("assets/hud/high_score.png").convert_alpha()
    icons["speed"] = pygame.image.load("assets/hud/speed.png").convert_alpha()
    icons["bomb"] = pygame.image.load("assets/hud/bomb.png").convert_alpha()
    icons["torpedo"] = pygame.image.load("assets/hud/torpedo.png").convert_alpha()
    icons["enemy"] = pygame.image.load("assets/hud/enemy.png").convert_alpha()
    icons["upgrade"] = pygame.image.load("assets/hud/upgrade.png").convert_alpha()

    for name in icons:
        icons[name] = pygame.transform.smoothscale(icons[name], (32, 32))
    return icons

def load_music():
    pygame.mixer.music.load("assets/sounds/background.mp3")
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1)
