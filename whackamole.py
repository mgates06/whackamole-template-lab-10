import pygame


screen = pygame.display.set_mode((640, 512))


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


def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen
        clock = pygame.time.Clock()
        running = True


        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            screen.fill(color = (15, 185, 220))
            draw_grid()
            pygame.display.flip()


            clock.tick(60)


    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
