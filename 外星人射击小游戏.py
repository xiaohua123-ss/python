import pygame
from pygame.sprite import Group
import login
import game_functions as gf
from button import Button
from game_stats import Gamestats
from scoreboard import Scoreboard
from settings import Settings
from ship import Ship


def run_game():
    pygame.init()
    ai = Settings()
    screen = pygame.display.set_mode((ai.screen_width, ai.screen_height))
    ship = Ship(ai, screen)
    bullets = Group()
    aliens = Group()
    gf.create_fleet(ai, screen, ship, aliens)
    stats = Gamestats(ai)
    sb = Scoreboard(ai, screen, stats)

    pygame.display.set_caption("Alien Invasion")
    play_button = Button(ai, screen, "play")

    while True:
        gf.check_events(ai, screen, stats, sb, play_button, ship, aliens, bullets)

        ship.update()
        gf.update_bullets(ai, screen, stats, sb, ship, aliens, bullets)
        gf.update_aliens(ai, screen, stats, sb, ship, aliens, bullets)

        pygame.display.flip()
        gf.update_screen(ai, screen, stats, sb, ship, aliens, bullets, play_button)


username=login.great_user()
run_game()
