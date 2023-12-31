import pygame
from pygame.locals import *


nought_cross   = "X"   
board_grid = [ [ None ]*3, \
         [ None ]*3, \
         [ None]*3 ]

winner_status = None



def init_board(menace_display):
    
    background = pygame.Surface (menace_display.get_size())
    background = background.convert()
    background.fill ((230, 230, 250))

    
    pygame.draw.line (background, (0,0,0), (100, 0), (100, 300), 2)
    pygame.draw.line (background, (0,0,0), (200, 0), (200, 300), 2)
    pygame.draw.line (background, (0,0,0), (300, 0), (300, 300), 2)


    
    pygame.draw.line (background, (0,0,0), (0, 100), (300, 100), 2)
    pygame.draw.line (background, (0,0,0), (0, 200), (300, 200), 2)
    pygame.draw.line (background, (0,0,0), (0, 300), (300, 300), 2)

    # return the board
    return background

def drawStatus (board):
    
    global nought_cross, winner_status

    # determine the status message
    if (winner_status is None):
        message = nought_cross + "'s turn"
    else:
        message = winner_status + " won!"
        
    # render the status message
    font = pygame.font.Font(None, 24)
    text = font.render(message, 1, (10, 10, 10))

    # copy the rendered message onto the board
    board.fill ((230, 230, 250), (0, 325, 300, 25))
    board.blit(text, (10, 315))

def show_board (menace_display, board):
    

    drawStatus (board)
    menace_display.blit (board, (0, 0))
    pygame.display.flip()
    
def board_position (mouse_X, mouse_Y):
    
    if (mouse_Y < 100):
        row = 0
    elif (mouse_Y < 200):
        row = 1
    else:
        row = 2

    # determine the column the user clicked
    if (mouse_X < 100):
        col = 0
    elif (mouse_X < 200):
        col = 1
    else:
        col = 2

    # return the tuple containg the row & column
    return (row, col)

def place_move (board, board_row, board_col, move_):
   
    center_X = ((board_col) * 100) + 50
    center_Y = ((board_row) * 100) + 50

    # draw the appropriate piece
    if (move_ == 'O'):
        pygame.draw.circle (board, (0,0,0), (center_X, center_Y), 44, 2)
    else:
        pygame.draw.line (board, (0,0,0), (center_X - 22, center_Y - 22), \
                         (center_X + 22, center_Y + 22), 2)
        pygame.draw.line (board, (0,0,0), (center_X + 22, center_Y - 22), \
                         (center_X - 22, center_Y + 22), 2)

    
    board_grid [board_row][board_col] = move_
    
def click_board(board):
   
    
    global board_grid
    
    (mouse_X, mouse_Y) = pygame.mouse.get_pos()
    (row_val, col_val) = board_position (mouse_X, mouse_Y)
    
    if ((board_grid[row_val][col_val] == "X") or (board_grid[row_val][col_val] == "O")):
       
        return None, None

    
    place_move (board, row_val, col_val, "X")
    return board, row_val, col_val

    
def winning_games(board):
    
    global board_grid, winner_status

    
    for row in range (0, 3):
        if ((board_grid [row][0] == board_grid[row][1] == board_grid[row][2]) and \
           (board_grid [row][0] is not None)):
            # this row won
            winner_status = board_grid[row][0]
            pygame.draw.line (board, (250,0,0), (0, (row + 1)*100 - 50), \
                              (300, (row + 1)*100 - 50), 2)
            break

   
    for col in range (0, 3):
        if (board_grid[0][col] == board_grid[1][col] == board_grid[2][col]) and \
           (board_grid[0][col] is not None):
            
            winner_status = board_grid[0][col]
            pygame.draw.line (board, (250,0,0), ((col + 1)* 100 - 50, 0), \
                              ((col + 1)* 100 - 50, 300), 2)
            break

    
    if (board_grid[0][0] == board_grid[1][1] == board_grid[2][2]) and \
       (board_grid[0][0] is not None):
       
        winner_status = board_grid[0][0]
        pygame.draw.line (board, (250,0,0), (50, 50), (250, 250), 2)

    if (board_grid[0][2] == board_grid[1][1] == board_grid[2][0]) and \
       (board_grid[0][2] is not None):
       
        winner_status = board_grid[0][2]
        pygame.draw.line (board, (250,0,0), (250, 50), (50, 250), 2)
