import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class that manages bullets fired from the ship"""

    def __init__(self, ai_game):
        """Create a bullet object at the ship's current position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # create a rect at (0,0) and then set correct position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
            self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # store bullets position as a decimal value
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet up the screen"""
        # Update the decimal position by decimal
        self.y -= self.settings.bullet_speed
        # Update the rect position
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)


