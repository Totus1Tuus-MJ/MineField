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

def toggle_noises(state):
    if not state.sounds_off or not state.music_off:
        state.sounds_off = True
        state.music_off = True
        pygame.mixer.music.pause()
    else:
        state.music_off = False
        state.sounds_off = False
        pygame.mixer.music.unpause()

