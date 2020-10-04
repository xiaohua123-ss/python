import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    def __init__(self,ai_settings,screen):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load('images\hua.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.ai_settings = ai_settings
        self.center1 = float(self.rect.centerx)
        self.center2 = float(self.rect.centery)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center1 += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center1 -= self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.top > 0:
            self.center2 -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom <= self.screen_rect.bottom:
            self.center2 += self.ai_settings.ship_speed_factor
        self.rect.centerx = self.center1
        self.rect.centery = self.center2

    def center_ship(self):
        self.center1 = self.screen_rect.centerx
        self.center2 = self.screen_rect.bottom
