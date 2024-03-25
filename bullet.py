import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the bullet image
        self.image = pygame.image.load('Absolut.png')  # Adjust the filename as needed
        self.rect = self.image.get_rect()

        # Position the bullet at the top center of the ship
        self.rect.midtop = ai_game.ship.rect.midtop

        # Store the bullet's position as a decimal value
        self.y = float(self.rect.y)

    def update(self):
        # Move the bullet up the screen
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        # Draw the bullet image onto the screen
        self.screen.blit(self.image, self.rect)
