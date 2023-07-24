import pygame
from sys import exit



### CONSTANTS
WIDTH  = 800
HEIGHT = 800
BG_COLOR = (251,247,245)

def board():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption("SUDOKU")
    # test_surface = pygame.Surface((400,400))
    # test_surface.fill('Blue')
    screen.fill(BG_COLOR)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        for i in range(10):
            # print(i)
            if (i % 3 == 0):
                LINE_THICKNESS = 4
            else:
                LINE_THICKNESS = 2
            pygame.draw.line(screen, (0, 0, 0), (72 + 72 * i, 72), (72 + 72 * i, 720), LINE_THICKNESS)
            pygame.draw.line(screen, (0, 0, 0), (72, 72 + 72 * i), (720, 72 + 72 * i), LINE_THICKNESS)

        # screen.blit(test_surface,(200,100))

        pygame.display.update()