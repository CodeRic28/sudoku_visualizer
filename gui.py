import pygame
from sys import exit
from generator import generate_board
from solver import *
import copy

### CONSTANTS
WIDTH  = 800
HEIGHT = 800
BG_COLOR = (251,247,245)
LINE_THICKNESS = 2
cell_x,cell_y =0,0

sudoku_board = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]
unsolved = generate_board(sudoku_board)
gui_board = copy.deepcopy(unsolved)

def auto_solve(screen):


def insert(screen, position):
    print(position[0],position[1])
    i, j = position[0], position[1]

    base_font = pygame.font.Font(None, 50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.unicode.isdigit() and 1 <= event.unicode <= '9':
                value = event.key - 48
                text_surface = base_font.render(str(value), True, (0, 0, 0))
                text_rect = text_surface.get_rect(center=(int(i),int(j)))
                screen.blit(text_surface, (i,j))
                pygame.display.update()

    pygame.display.update()




def board():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption("SUDOKU")
    screen.fill(BG_COLOR)

    # Set up fonts
    # pygame.font.Font(style, size)
    base_font = pygame.font.Font(None, 50)
    small_font = pygame.font.Font(None, 30)

    # Button to automatic solve

    # Populating the grid
    for row in range(9):
        for col in range(9):
            value = gui_board[row][col]
            if value != 0:
                # base_font.render(text_to_insert, enable_antialiasing,color)
                text_surface = base_font.render(str(value), True, (65, 157, 123))
                # positioning the centerpiece of the rectangle
                text_rect = text_surface.get_rect(center=(72 + col * 72 + 36, 72 + row * 72 + 36))
                # pygame.draw.rect(screen,(245,235,62),text_rect)
                screen.blit(text_surface, text_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                # insert(screen, (mouse_x//72 -1, mouse_y//72 - 1))
                x,y = mouse_x//72 -1, mouse_y//72 - 1
                cell_x,cell_y = x,y
            elif event.type == pygame.KEYDOWN:
                if event.key == 48 or event.key == pygame.K_BACKSPACE:
                    erase_rect = pygame.Rect((72 + cell_x * 72, 35+ cell_y * 72 + 36), (72, 72))
                    pygame.draw.rect(screen, BG_COLOR, erase_rect)
                    gui_board[y][x] = 0
                    pygame.display.update()
                if event.unicode.isdigit() and '1' <= event.unicode <= '9':
                    if gui_board[y][x] != 0:
                        continue
                    value = event.key - 48
                    text_surface = base_font.render(str(value), True, (0, 0, 0))
                    text_rect = text_surface.get_rect(center=(72 + x * 72 + 36, 72 + y * 72 + 36))
                    screen.blit(text_surface, text_rect)
                    gui_board[y][x] = event.key-48
                    pygame.display.update()
                    print(x," ",y)
                    print("__________________________")
                    print_board(gui_board)
                    print("__________________________")

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


        pygame.display.update()

board()