#ui.py
from ui.colors import Color
from core import config
import pygame
from services import login
from systems import achievements

def draw_rights(screen, small_font):
    rights_text = small_font.render("© Mario International 2026", True, Color.CYAN)
    screen.blit(rights_text, (10, 975))


def draw_hud(screen, state, reg_font, small_font, high_score, hud_icons, quit_button):

    tokens_text = reg_font.render(f"{login.get_tokens(state.current_user['username'])}", True, Color.BROWN)
    lives_text = reg_font.render(f"{state.lives}", True, Color.GOLD)
    shield_text = reg_font.render(f"{state.shields}", True, Color.GREEN)
    score_text = reg_font.render(f"{state.score}", True, Color.WHITE)
    high_text = reg_font.render(f"{high_score}", True, Color.ORANGE)
    speed_text = reg_font.render(f"{int(state.enemy_speed)}", True, Color.RED)
    bombs_text = reg_font.render(f"{state.bombs}", True, Color.CYAN)
    torpedoes_text = reg_font.render(f"{state.torpedo_count}", True, Color.BROWN)
    enemies_text = reg_font.render(f"{state.enemies_destroyed}", True, Color.RED)
    upgrades_text = reg_font.render(f"{state.upgrades_collected}", True, Color.PURPLE)
    last_effect_text = reg_font.render(f"{state.effect}", True, Color.MAGENTA)
    center = (config.WIDTH - last_effect_text.get_width()) // 2    

    screen.blit(hud_icons["token"], (10, 10))
    screen.blit(tokens_text, (45, 10))

    screen.blit(hud_icons["heart"], (10, 50))
    screen.blit(lives_text, (45, 50))

    screen.blit(hud_icons["shield"], (10, 90))
    screen.blit(shield_text, (45, 90))

    screen.blit(hud_icons["score"], (10, 130))
    screen.blit(score_text, (45, 130))

    screen.blit(hud_icons["high_score"], (10, 170))
    screen.blit(high_text, (45, 170))

    screen.blit(hud_icons["speed"], (10, 210))
    screen.blit(speed_text, (45, 210))

    screen.blit(hud_icons["bomb"], (10, 250))
    screen.blit(bombs_text, (45, 250))

    screen.blit(hud_icons["torpedo"], (10, 290))
    screen.blit(torpedoes_text, (45, 290))

    screen.blit(hud_icons["enemy"], (10, 330))
    screen.blit(enemies_text, (45, 330))

    screen.blit(hud_icons["upgrade"], (10, 370))
    screen.blit(upgrades_text, (45, 370))

    screen.blit(last_effect_text, (center, 25))
    draw_rights(screen,small_font)
    current_time = pygame.time.get_ticks()

    active_effects_title_text= reg_font.render("ACTIVE UPGRADES", True, Color.PURPLE)
    screen.blit(active_effects_title_text, (1000, 20))
    for i, effect in enumerate(state.active_effects):
        remaining = max(0,int((effect["expires"] - current_time) / 1000))
        timer_text = small_font.render(f"{effect['name']}: {remaining}s", True, Color.WHITE)

        screen.blit(timer_text, (1000, 50 + (i * 20)))



    current_time = pygame.time.get_ticks()

    if current_time - state.achievement_timer < 3000:
        achievements_text = reg_font.render(state.achievement_message, True, Color.GOLD)
        center = (config.WIDTH - achievements_text.get_width()) // 2    

        screen.blit(achievements_text, (center, 80))
    
    # Mission Critical warning
    if current_time - state.damage_timer < 1000:
        critical_text = reg_font.render("MISSION CRITICAL", True, Color.RED)
        screen.blit(critical_text, ((config.WIDTH - critical_text.get_width()) // 2, config.HEIGHT // 2 + 100))

    if quit_button:
        quit_button.draw(screen, reg_font, Color, Color.RED, Color.WHITE)

def draw_game_over(screen, state, reg_font, small_font, performance, quit_button):
    completion_text = reg_font.render("Training Simulation Complete", True, Color.YELLOW)
    performance_text = reg_font.render(f"Performance Analysis: {performance}", True, Color.SILVER)
    restart_text = reg_font.render("Press [SPACE] to Restart", True, Color.WHITE)

    screen.blit(completion_text, (config.WIDTH // 2 - completion_text.get_width() // 2, config.HEIGHT // 2 - 125))
    screen.blit(performance_text, (config.WIDTH // 2 - performance_text.get_width() // 2, config.HEIGHT // 2 - 50))
    screen.blit(restart_text, (config.WIDTH // 2 - restart_text.get_width() // 2, config.HEIGHT // 2 + 10))

    if quit_button:
        quit_button.draw(screen, reg_font, Color, Color.RED, Color.WHITE)

def draw_pause_menu(screen, state, reg_font, small_font, pause_buttons, quit_button):

    overlay = pygame.Surface((config.WIDTH, config.HEIGHT))
    overlay.set_alpha(150)
    overlay.fill(Color.BLACK)
    screen.blit(overlay, (0, 0))


    pause_text = reg_font.render("PAUSED", True, Color.YELLOW)
    resume_text = reg_font.render("Press P to Resume", True, Color.WHITE)
    gun_accuracy_text = reg_font.render(f"Gun Accuracy: {int(state.accuracy * 100)}%", True, Color.RED)
    screen.blit(pause_text, (config.WIDTH // 2 - pause_text.get_width() // 2, config.HEIGHT // 2 - 50))

    screen.blit(resume_text, (config.WIDTH // 2 - resume_text.get_width() // 2, config.HEIGHT // 2 + 10))
    screen.blit(gun_accuracy_text, (config.WIDTH // 2 - gun_accuracy_text.get_width() // 2, config.HEIGHT // 2 + 50))
    draw_rights(screen,small_font)

    for button in pause_buttons:
        button.draw(screen, reg_font, Color, Color.DARK_GRAY, Color.WHITE)
    
    if quit_button:
        quit_button.draw(screen, reg_font, Color, Color.RED, Color.WHITE)



def message_screen(screen, reg_font, small_font, title, message, message_2, quit_button):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.KEYDOWN:
                return True

        screen.fill(Color.BLACK)

        title_text = reg_font.render(title, True, Color.RED)
        msg_text = reg_font.render(message, True, Color.WHITE)
        msg_2_text = reg_font.render(message_2, True, Color.WHITE)
        info_text = small_font.render("Press any key to exit", True, Color.GRAY)

        screen.blit(title_text, (config.WIDTH // 2 - title_text.get_width() // 2, 300))

        screen.blit(msg_text, (config.WIDTH // 2 - msg_text.get_width() // 2, 360))
        screen.blit(msg_2_text, (config.WIDTH // 2 - msg_2_text.get_width() // 2, 420))

        screen.blit(info_text, (config.WIDTH // 2 - info_text.get_width() // 2, 480))
        draw_rights(screen,small_font)

        if quit_button:
            quit_button.draw(screen, reg_font, Color, Color.RED, Color.WHITE)

        pygame.display.flip()

def draw_achievements_screen(screen, state, reg_font, small_font, achievements_buttons,quit_button):

    screen.fill(Color.BLACK)
    completed, total = achievements.get_achievement_progress(state)
    title = reg_font.render(f"{completed}/{total}", True, Color.GOLD)
    screen.blit(title, (300, 50))
    starting_blit_position = 120
    blit_increment = 30
    for name, achievement in state.achievements.items():
        symbol = "**" if achievement["unlocked"] else "X"
        color = (Color.GREEN if achievement["unlocked"] else Color.WHITE)
        goal = achievement.get("goal")
        if goal:
            name_text = reg_font.render(f"{symbol} {name}  ({achievement["progress"]}/{goal})", True, color)
        else:
            name_text = reg_font.render(f"{symbol} {name}", True, color)

        description_text = reg_font.render(achievement["description"], True, Color.LIGHT_GRAY)
        screen.blit(name_text, (100, starting_blit_position))
        screen.blit(description_text, (750, starting_blit_position))
        starting_blit_position += blit_increment

    draw_rights(screen,small_font)

    for button in achievements_buttons:
        button.draw(screen, reg_font, Color, Color.DARK_GRAY, Color.WHITE)
    
    if quit_button:
        quit_button.draw(screen, reg_font, Color, Color.RED, Color.WHITE)

def draw_instructions_screen(screen, state, reg_font, small_font, quit_button):
    screen.fill(Color.BLACK)
    title_text = reg_font.render("MineField INSTRUCTION/Tutorial Page", True, Color.YELLOW)
    instructions = [
        "Use WASD or the arrow keys for UP, LEFT, DOWN, & RIGHT",
        "SPACE fires bullets, T fires torpedoes, and B launches bombs",
        "P toggles the PAUSE MENU (SPACE toggles it off).",
        "On the Pause Menu, press A to toggle the Achievements Menu",
        "On any Menu, the first letter of a button can be pressed with the same effect",
        "At any time you may press Q to end the game.",
        "Press I to open and close the Instruction Page",
        "Press B to go back from Achievements or Instructions"
    ]
    
    screen.blit(title_text, (config.WIDTH // 2 - title_text.get_width() // 2, 100))
    
    y = 200
    for line in instructions:
        text = reg_font.render(line, True, Color.WHITE)
        screen.blit(text, (200, y))
        y += 50

    draw_rights(screen,small_font)
    
    info_text = small_font.render("Press 'I' to close instructions", True, Color.GRAY)
    screen.blit(info_text, (config.WIDTH // 2 - info_text.get_width() // 2, config.HEIGHT - 100))
    
    if quit_button:
        quit_button.draw(screen, reg_font, Color, Color.RED, Color.WHITE)
