## background.py

import random
from colors import Color
import config

from space import Star


def init(state):
    for far_star in range(150):
        state.stars.append(Star(random.randint(0, config.WIDTH),random.randint(0, config.HEIGHT), random.randint(1, 2),
                                random.choices([Color.WHITE, Color.YELLOW, Color.RED, Color.CYAN,Color.LIME, Color.ORANGE, Color.GRAY],
                                               weights = [20, 15, 1 , 1, 1, 1, 1],k = 1)[0],random.randint(20, 40),0))
    for mid_star in range(85):
        state.stars.append(Star(random.randint(0, config.WIDTH), random.randint(0, config.HEIGHT),random.randint(2, 3),
                                random.choices([Color.WHITE, Color.YELLOW, Color.RED, Color.CYAN, Color.LIME, Color.ORANGE],
                                               weights = [40, 20, 2,1,1,1], k = 1)[0], random.randint(60, 80), 1))
    for near_star in range(35):
        state.stars.append(Star(random.randint(0, config.WIDTH), random.randint(0, config.HEIGHT), random.randint(3, 6),
                                random.choices([Color.WHITE, Color.YELLOW, Color.RED, Color.ORANGE],
                                               weights = [50, 30 , 1 , 2], k = 1)[0], random.randint(150, 200), 2))
