import sys
import pygame

import game_functions
from settings import Settings
from ship import Ship


def run_game():
    pygame.init()
    pygame.display.set_caption("Alien Invasion")
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    ship = Ship(screen)
    while True:
        game_functions.check_events(ship)
        game_functions.update_screen(ai_settings, screen, ship)
        ship.update()

if __name__ == '__main__':
    run_game()
