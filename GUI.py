import pygame
from constants import *
from engine import *

pygame.init()
pygame.display.set_caption("Chess")
screen = pygame.display.set_mode((720, 720))

def drawSquare(x, y, selected, highlighted, isPossibleMove):
    colour = (0,0,0)
    if colourTable[x%2][y%2] == 'w':
        if selected:
            colour = selected_white
        elif highlighted:
            colour = high_white
        elif isPossibleMove:
            colour = move_white
        else:
            colour = white
    else:
        if selected:
            colour = selected_green
        elif highlighted:
            colour = high_green
        elif isPossibleMove:
            colour = move_green
        else:
            colour = green
    if isPossibleMove:
        if board[x][y] == '0':
            pygame.draw.circle(screen, colour, (90 * y + 45, 90 * x + 45), 15)
        else:
            pygame.draw.circle(screen, colour, (90 * y + 45, 90 * x + 45), 44, 6)
    else:
        pygame.draw.rect(screen, colour, (90 * y, 90 * x, 90, 90))
        if board[x][y].islower():
            if board[x][y] == 'p':
                screen.blit(bPawn, (90 * y + 21, 90 * x + 16))
            elif board[x][y] == 'k':
                screen.blit(bKing, (90 * y + 15, 90 * x + 14))
            elif board[x][y] == 'q':
                screen.blit(bQueen, (90 * y + 10, 90 * x + 10))
            elif board[x][y] == 'n':
                screen.blit(bKnight, (90 * y + 14, 90 * x + 14))
            elif board[x][y] == 'b':
                screen.blit(bBishop, (90 * y + 14, 90 * x + 14))
            elif board[x][y] == 'r':
                screen.blit(bRook, (90 * y + 16, 90 * x + 11)) 
        else:
            if board[x][y] == 'P':
                screen.blit(wPawn, (90 * y + 21, 90 * x + 16))
            elif board[x][y] == 'K':
                screen.blit(wKing, (90 * y + 15, 90 * x + 14))
            elif board[x][y] == 'Q':
                screen.blit(wQueen, (90 * y + 10, 90 * x + 10))
            elif board[x][y] == 'N':
                screen.blit(wKnight, (90 * y + 14, 90 * x + 14))
            elif board[x][y] == 'B':
                screen.blit(wBishop, (90 * y + 14, 90 * x + 14))
            elif board[x][y] == 'R':
                screen.blit(wRook, (90 * y + 16, 90 * x + 11))  

def select(pos):
    drawSquare(pos[0], pos[1], True, False, False)
    moves = getMoves(pos, board)
    for move in moves:
        drawSquare(move[0], move[1], False, False, True)
    pygame.display.update()

def moveSelected(selected, position):
    global board
    board[position[0]][position[1]] = board[selected[0]][selected[1]]
    board[selected[0]][selected[1]] = '0'
    drawSquare(selected[0], selected[1], True, False, False)
    drawSquare(position[0], position[1], True, False, False)
    pygame.display.update()
    if board[position[0]][position[1]] == 'k':
        bK = board[position[0]][position[1]]
    elif board[position[0]][position[1]] == 'K':
        wK = board[position[0]][position[1]]


def draw_entire_board():
    for x in range(8):
        for y in range(8):
            drawSquare(x, y, False, False, False)
    pygame.display.update()
