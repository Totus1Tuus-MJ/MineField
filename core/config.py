## config.py
import json
import os
import pygame

## Font Size
REG_FONT_SIZE = 40
SMALL_FONT_SIZE = 15

## Screen
WIDTH = 1550
HEIGHT = 950


## Highscore
HIGH_SCORE_FILE = "minefield_highscore.json"

def load_highscore():
    if os.path.exists(HIGH_SCORE_FILE):
        try:
            with open(HIGH_SCORE_FILE, "r") as f:
                return json.load(f).get("highscore", 0)
        except (json.JSONDecodeError, OSError):
            return 0
    return 0

def save_highscore(score):
    with open(HIGH_SCORE_FILE, "w") as f:
        json.dump({"highscore": score}, f)
def calc_performance(score, highscore):
    if score > highscore:
        performance = "Success"
        save_highscore(score)
    elif score == highscore:
        performance = "Incomplete"
    elif score < highscore:
        performance = "Failure"
    return performance

highscore = load_highscore()



    
