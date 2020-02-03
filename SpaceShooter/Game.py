# Space Shooter
# A game made with Pygame by Conor O'Donovan

import pygame

screen_width = 1280
screen_height = 800
frames_per_second = pygame.time.Clock()


def redraw_game_window():
    pygame.display.update()


if __name__ == "__main__":
    game_window = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Space Shooter")

    # Game loop
    running = True

    while running:
        frames_per_second.tick(30)

        # Closing window and exiting program
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        redraw_game_window()

    pygame.quit()
