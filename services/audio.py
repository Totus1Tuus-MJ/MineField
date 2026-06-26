## audio.py
import pygame

def play_sound(state, sound):
    if not state.sounds_off:
        sound.play()

def toggle_music(state):
    state.music_off = not state.music_off
    
    if not state.music_off:
            pygame.mixer.music.unpause()
    else:
        pygame.mixer.music.pause()

def toggle_sounds(state):
    state.sounds_off = not state.sounds_off
