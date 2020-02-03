# Space Shooter
# A game made with Pygame by Conor O'Donovan

import pygame
from Player import Player
from Projectile import Projectile

screen_width = 1280
screen_height = 800
frames_per_second = pygame.time.Clock()


def redraw_game_window(win):
    game_window.fill((0, 0, 0))
    player.draw_player(game_window)
    pygame.display.update()


if __name__ == "__main__":
    game_window = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Space Shooter")

    player = Player(screen_width / 8, screen_height / 2, 64, 64, 6, 100)

    # Game loop
    running = True

    while running:
        frames_per_second.tick(60)
        keys_pressed = pygame.key.get_pressed()

        player.move_player(keys_pressed)

        # Closing window and exiting program
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        redraw_game_window(game_window)

    pygame.quit()
