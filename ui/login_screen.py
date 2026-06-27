## login_screen.py

import pygame
from services.login import check_credentials
from ui.colors import Color
from ui.ui import message_screen
from core import config


def login_screen(screen, reg_font, small_font, quit_button):
    username = ""
    password = ""

    active = "username"

    while True:
        screen.fill(Color.BLACK)

        title = reg_font.render("MineField Login", True, Color.WHITE)
        disp_user = reg_font.render(f"User: {username}", True, Color.WHITE)
        disp_password = reg_font.render(f"Password: {'*' * len(password)}", True, Color.WHITE)

        prompt = small_font.render("[TAB] changes fields / [ENTER] logs in", True, Color.RED)

        instructions_text = reg_font.render("If you are new to this game, press [I] for Instructions after logging in", True, Color.RED)
        owner_text = small_font.render("WARNING: This developmental resource is owned by Mario International™", True, Color.GOLD)
        cookies_text = small_font.render("By continuing, you agree to the Mario International Terms & Conditions", True, Color.GREEN)
        tampering_notice_text = small_font.render("Failure to comply with these Terms and laws may result in legal action.", True, Color.WHITE)
        rights_text = small_font.render("© Mario International 2026", True, Color.CYAN)

        screen.blit(title,(350,150))
        screen.blit(disp_user,(250,300))
        screen.blit(disp_password,(250,360))
        screen.blit(prompt,(250,500))
        screen.blit(instructions_text, (250, 800))
        screen.blit(owner_text, (config.WIDTH // 2 - owner_text.get_width() // 2, config.HEIGHT // 2 + 90))
        screen.blit(cookies_text, (config.WIDTH // 2 - cookies_text.get_width() // 2, config.HEIGHT // 2 + 140))
        screen.blit(tampering_notice_text, (
            config.WIDTH / 2 - tampering_notice_text.get_width() // 2, config.HEIGHT // 2 + 190))
        screen.blit(rights_text, (10, 975))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_TAB:

                    if active=="username":
                        active="password"
                    else:
                        active="username"
                elif event.key == pygame.K_RETURN:
                    user = check_credentials(username, password)
                    if user:
                        return user
                    else:
                        message_screen(screen, reg_font, small_font, "ERROR: INVALID LOGIN", "Your Username or Password was Incorrect. Please try again.", "To set up an account or troubleshoot login issues, please contact an administator.", quit_button)
                        
                elif event.key == pygame.K_BACKSPACE:

                    if active=="username":
                        username=username[:-1]
                    else:
                        password=password[:-1]

                else:
                    if active=="username":
                        username += event.unicode
                    else:
                        password += event.unicode
        
