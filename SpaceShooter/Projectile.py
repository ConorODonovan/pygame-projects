import pygame


class Projectile:
    def __init__(self, x, y, width, height, velocity):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity = velocity

    def projectile_move(self):
        self.x += self.velocity

    def draw_projectile(self, win):
        pygame.draw.rect(win, (255, 0, 0), pygame.Rect(self.x, self.y, self.width, self.height))
