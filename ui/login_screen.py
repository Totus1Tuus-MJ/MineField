## login_screen.py

import pygame
from services.login import check_credentials
from ui.colors import Color
from core import game_flow
from ui.ui import message_screen

def login_screen(screen, reg_font, small_font):
    username = ""
    password = ""

    active = "username"

    while True:
        screen.fill(Color.BLACK)

        title = reg_font.render("MineField Login", True, Color.WHITE)
        disp_user = reg_font.render(f"User: {username}", True, Color.WHITE)
        disp_password = reg_font.render(f"Password: {'*'*len(password)}", True, Color.WHITE)

        prompt = small_font.render("[TAB] changes fields / [ENTER] logs in", True, Color.NOBEL)
        
        screen.blit(title,(350,150))
        screen.blit(disp_user,(250,300))
        screen.blit(disp_password,(250,360))
        screen.blit(prompt,(250,500))

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
                        message_screen(screen, reg_font, small_font, "ERROR: INVALID LOGIN", "Your Username or Password was Incorrect. Please try again.", "To set up an account or troubleshoot login issues, please contact an administator.")
                        
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
        
