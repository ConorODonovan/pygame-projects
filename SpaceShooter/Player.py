import pygame
from Projectile import Projectile


class Player:
    def __init__(self, x=0, y=0, width=32, height=32, velocity=6, health=100):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity = velocity
        self.health = health

    def move_player(self, keys_pressed):
        if keys_pressed[pygame.K_LEFT]:
            self.x -= self.velocity

        if keys_pressed[pygame.K_RIGHT]:
            self.x += self.velocity

        if keys_pressed[pygame.K_UP]:
            self.y -= self.velocity

        if keys_pressed[pygame.K_DOWN]:
            self.y += self.velocity

    def draw_player(self, win):
        pygame.draw.rect(win, (0, 0, 255), pygame.Rect(self.x, self.y, self.width, self.height))

    def fire_projectile(self, keys_pressed, win):
        if keys_pressed[pygame.K_SPACE]:
            new_projectile = Projectile(self.x, self.y, 16, 4, 12)
