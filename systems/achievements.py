## achievements.py
import json
import pygame
from services import login

def load_achievements():
    with open("assets/data/achievements.json") as file:
        data = json.load(file)
    achievements = {}

    for name, info in data.items():
        achievements[name] = {
            "description": info["description"],
            "unlocked": False,
            "progress" : 0}
        if "stat" in info:
            achievements[name]["stat"] = info["stat"]
        if "goal" in info:
            achievements[name]["goal"] = info["goal"]

    return achievements

def get_achievement_progress(state):
    total = len(state.achievements)
    completed = sum(a["unlocked"] for a in state.achievements.values())
    return completed, total


def load_completed(state):
    if state.current_user is None:
        return
    completed = state.current_user.get("achievements", [])
    for achievement in completed:
        if achievement in state.achievements:
            state.achievements[achievement]["unlocked"] = True

def unlock(state, name):

    achievement = state.achievements[name]
    if achievement["unlocked"]:
        return
    achievement["unlocked"] = True
    state.achievement_message = (f"Achievement Unlocked: {name}")
    state.achievement_timer = (pygame.time.get_ticks())

    if state.current_user is None:
        return
    
    user = state.current_user
    if "achievements" not in user:
        user["achievements"] = []
    if name not in user["achievements"]:
        user["achievements"].append(name)
        login.save_user(state.current_user)

def check_automatic(state):

    for name, achievement in state.achievements.items():
        stat = achievement.get("stat")
        goal = achievement.get("goal")

        if stat and goal:
            value = getattr(state, stat)

            achievement["progress"] = min(value, goal)

            if value >= goal:
                unlock(state, name)
                
def check_manual(state):

    if (state.accuracy >= 0.9 and state.shots_fired >= 250):
        unlock(state, "Sniper")
    if (state.score >= 500 and state.lives == 3 and state.shields_lost == 0):
        unlock(state, "Untouchable")
    if (state.lives == 1 and state.shields == 0):
        unlock(state, "Escape Artist")

def check(state):
    check_automatic(state)
    check_manual(state)
    state.achievements_completed, state.total_achievements = get_achievement_progress(state)

