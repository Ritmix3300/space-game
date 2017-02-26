import pygame
from pygame.sprite import Group

import game_functions
from button import Button
from game_stats import GameStats
from settings import Settings
from ship import Ship


def run_game():
    pygame.init()
    pygame.display.set_caption("Alien Invasion")
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    stats = GameStats(ai_settings)
    play_button = Button(ai_settings, screen, 'Play')
    game_functions.create_fleet(ai_settings, screen, ship, aliens)
    while True:
        game_functions.check_events(
            ai_settings, screen, stats, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            game_functions.update_bullets(
                ai_settings, screen, ship, aliens, bullets)
            game_functions.update_aliens(
                ai_settings, stats, screen, ship, aliens, bullets)
        game_functions.update_screen(
            ai_settings, screen, stats, ship, aliens, bullets, play_button)

if __name__ == '__main__':
    run_game()
