#Whack-A-Mole game full functionality

import pygame
from random import randrange

from pygame import MOUSEBUTTONDOWN


screen = pygame.display.set_mode((640, 512)) #Defined screen here so I could reference it in the draw_grid function

def draw_grid():
    #Vertical lines
    for i in range(1, 20):
        pygame.draw.line(
            screen,
            (0, 0, 0),
            (i * 32, 0),
            (i * 32, 512),
        )

    #Horizontal lines
    for i in range(1, 16):
        pygame.draw.line(
            screen,
            (0, 0, 0),
            (0, i * 32),
            (640, i * 32),
        )

def random_x():
    return randrange(0, 20) #Random column number

def random_y():
    return randrange(0, 16) #Random row number



def main():
    try:

        temp_x = random_x() #Placeholder x-value
        temp_y = random_y() #Placeholder y-value

        pygame.init()
        mole_image = pygame.image.load("mole.png")

        screen
        clock = pygame.time.Clock()
        running = True

        while running:

            screen.fill(color=(15, 185, 220))
            draw_grid()

            screen.blit(mole_image,
                        mole_image.get_rect(topleft=(temp_x * 32, temp_y * 32)))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == MOUSEBUTTONDOWN:
                    x, y = event.pos
                    x //= 32
                    y //= 32

                    if x == temp_x and y == temp_y:
                        temp_x = random_x()
                        temp_y = random_y()

                        screen.blit(mole_image,
                                    mole_image.get_rect(topleft=(temp_x * 32, temp_y * 32)))

            pygame.display.flip()

            clock.tick(60)

    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
