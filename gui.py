import pygame
from sys import exit
from generator import generate_board
from solver import print_board,solveit
import copy
import math

#solver
def canPlace(bo,number,row,col,n):
    # check row and col
    for i in range(n):
        if(bo[row][i]==number or bo[i][col]==number):
            return False

    # check subgrid
    rn = int(math.sqrt(n))
    sx = (row // rn) * rn
    sy = (col // rn) * rn

    for x in range(int(sx), int(sx+rn)):
        for y in range(int(sy), int(sy+rn)):
            if(bo[x][y] == number):
                return False

    return True

def solveSudoku(bo,row,col,n):
    # base case
    if row == n:
        if 0 not in bo[n-1]:
            print(row," ", col)
            print("BASE CASE TRIGGERED")
            return 5
        return True
    if(col == n):
        if solveSudoku(bo,row+1,0,n) == 5:
            pygame.time.delay(1000)
            exit()
            # for event in pygame.event.get():
            #
            #     if event.type == pygame.K_RETURN:
            #         pygame.quit()
            #         exit()


        return solveSudoku(bo,row+1,0,n)
    if bo[row][col] != 0:
        return solveSudoku(bo,row,col+1,n)

    for number in range(1,n+1):
        if(canPlace(bo,number,row,col,n)):
            bo[row][col] = number
            auto_insert(screen, (row, col), number)
            check = solveSudoku(bo,row,col+1,n)
            auto_backtrack(screen, (row, col))
            if(check):
                return True
    # Backtrack
    bo[row][col] = 0
    # remove from guiboard
    auto_backtrack(screen, (row, col))
    return False




### CONSTANTS
WIDTH  = 800
HEIGHT = 800
BG_COLOR = (251,247,245)
LINE_THICKNESS = 2
cell_x,cell_y =0,0
BUFFER = 5

board = [
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
solved = solveit(board,0,0,9)
unsolved = generate_board(solved)

gui_board = copy.deepcopy(unsolved)
# print_board(solveit(unsolved,0,0,9))

class Button:
    def __init__(self,text,width,height,pos,elevation):
        # core attributes
        self.pressed = False
        self.elevation = elevation
        self.dynamic_elevation = elevation
        self.original_y_pos = pos[1]

        # top rectangle
        self.top_rect = pygame.Rect(pos,(width,height))
        self.top_color = (65, 157, 123)

        # bottom rectangle
        self.bottom_rect = pygame.Rect(pos,(width,elevation))
        self.bottom_color = '#354B5E'

        # text
        self.text_surf = gui_font.render(text,True,'#FFFFFF')
        self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)

    def draw(self):
        #elevation logic
        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dynamic_elevation

        self.top_rect.y = self.original_y_pos - self.dynamic_elevation
        self.text_rect.center = self.top_rect.center

        pygame.draw.rect(screen,self.bottom_color,self.bottom_rect,border_radius=12)
        pygame.draw.rect(screen,self.top_color,self.top_rect,border_radius=12)
        screen.blit(self.text_surf,self.text_rect)
        self.check_click()

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):

            clock.tick(60)
            pygame.display.update()
            self.top_color = '#D74B4B'
            if pygame.mouse.get_pressed()[0]: # Returns a 3-tuple of mouse buttons ([left-click],middle-click,right-click)
                self.top_color = (65, 157, 123)
                self.dynamic_elevation = 0
                self.pressed = True
            else:
                self.dynamic_elevation = self.elevation
                if self.pressed == True:
                    # AUTO SOLVE CODE TO BE EXECUTED
                    solveSudoku(gui_board,0,0,9) # solveSudoku(bo,row,col,n,gui_board):
                    print_board(gui_board)
                    # unsolved = generate_board(gui_board)
                    self.pressed = False

        else:
            self.dynamic_elevation = self.elevation
            self.top_color = (65, 157, 123)



pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
gui_font = pygame.font.Font(None, 30)
clock = pygame.time.Clock()


def auto_insert(screen, position,number):
    i, j = position[0], position[1]

    base_font = pygame.font.Font(None, 50)
    text_surface = base_font.render(str(number), True, (153, 102, 204))
    text_rect = text_surface.get_rect(center=(72 + j * 72 + 36, 72 + i * 72 + 36))
    screen.blit(text_surface, text_rect)
    clock.tick(60)
    pygame.display.update()


def auto_backtrack(screen,position):
    i, j = position[0], position[1]
    erase_rect = pygame.Rect((72 + j * 72 +3, 72 + i * 72 + 3), (67, 67))
    pygame.draw.rect(screen, BG_COLOR, erase_rect)
    clock.tick(60)
    pygame.display.update()

def board():

    pygame.display.set_caption("SUDOKU")
    screen.fill(BG_COLOR)

    # Set up fonts
    # pygame.font.Font(style, size)
    base_font = pygame.font.Font(None, 50)
    medium_font = pygame.font.Font(None, 40)
    small_font = pygame.font.Font(None, 30)

    # Button to automatic solve
    # Instance of Button class
    auto_solve_btn = Button('Solve it!', 72 * 2, 36, (72, 20), 6)

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
                    erase_rect = pygame.Rect((72 + cell_x * 72 +3, 35+ cell_y * 72 + 36 + 5), (67, 67))
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

        # Draw the auto solve button
        auto_solve_btn.draw()

        for i in range(10):
            # print(i)
            if (i % 3 == 0):
                LINE_THICKNESS = 4
            else:
                LINE_THICKNESS = 2
            pygame.draw.line(screen, (0, 0, 0), (72 + 72 * i, 72), (72 + 72 * i, 720), LINE_THICKNESS)
            pygame.draw.line(screen, (0, 0, 0), (72, 72 + 72 * i), (720, 72 + 72 * i), LINE_THICKNESS)

        clock.tick(10)
        pygame.display.update()


board()