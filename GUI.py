import pygame
from engine import *

pygame.init()
pygame.display.set_caption("Chess")
screen = pygame.display.set_mode((720, 720))

def drawSquare(game, x, y, selected, highlighted, isPossibleMove):
    colour = (0,0,0)
    if game.colourTable[x%2][y%2] == 'w':
        if selected:
            colour = game.selected_white
        elif highlighted:
            colour = game.high_white
        elif isPossibleMove:
            colour = game.move_white
        else:
            colour = game.white
    else:
        if selected:
            colour = game.selected_green
        elif highlighted:
            colour = game.high_green
        elif isPossibleMove:
            colour = game.move_green
        else:
            colour = game.green
    if isPossibleMove:
        if game.board[x][y] == '0':
            pygame.draw.circle(screen, colour, (90 * y + 45, 90 * x + 45), 15)
        else:
            pygame.draw.circle(screen, colour, (90 * y + 45, 90 * x + 45), 44, 6)
    else:
        pygame.draw.rect(screen, colour, (90 * y, 90 * x, 90, 90))
        if game.board[x][y].islower():
            if game.board[x][y] == 'p':
                screen.blit(game.bPawn, (90 * y + 21, 90 * x + 16))
            elif game.board[x][y] == 'k':
                screen.blit(game.bKing, (90 * y + 15, 90 * x + 14))
            elif game.board[x][y] == 'q':
                screen.blit(game.bQueen, (90 * y + 10, 90 * x + 10))
            elif game.board[x][y] == 'n':
                screen.blit(game.bKnight, (90 * y + 14, 90 * x + 14))
            elif game.board[x][y] == 'b':
                screen.blit(game.bBishop, (90 * y + 14, 90 * x + 14))
            elif game.board[x][y] == 'r':
                screen.blit(game.bRook, (90 * y + 16, 90 * x + 11)) 
        else:
            if game.board[x][y] == 'P':
                screen.blit(game.wPawn, (90 * y + 21, 90 * x + 16))
            elif game.board[x][y] == 'K':
                screen.blit(game.wKing, (90 * y + 15, 90 * x + 14))
            elif game.board[x][y] == 'Q':
                screen.blit(game.wQueen, (90 * y + 10, 90 * x + 10))
            elif game.board[x][y] == 'N':
                screen.blit(game.wKnight, (90 * y + 14, 90 * x + 14))
            elif game.board[x][y] == 'B':
                screen.blit(game.wBishop, (90 * y + 14, 90 * x + 14))
            elif game.board[x][y] == 'R':
                screen.blit(game.wRook, (90 * y + 16, 90 * x + 11))  

def draw_entire_board(game):
    for x in range(8):
        for y in range(8):
            drawSquare(game, x, y, False, False, False)
    pygame.display.update()

def select(game, pos):
    drawSquare(game, pos[0], pos[1], True, False, False)
    game.moves = getMoves(pos, game)
    for move in game.moves:
        drawSquare(game, move[0], move[1], False, False, True)
    pygame.display.update()

def moveSelected(game, selected, position):
    if position in game.moves:

        if game.board[position[0]][position[1]] == '0' and not position[1] == selected[1]:
            if game.board[selected[0]][selected[1]] == 'P':
                game.board[position[0]+1][position[1]] = '0'
                drawSquare(game, position[0]+1, position[1], True, False, False)
            elif game.board[selected[0]][selected[1]] == 'p':
                game.board[position[0]-1][position[1]] = '0'
                drawSquare(game, position[0]-1, position[1], True, False, False)

        game.board[position[0]][position[1]] = game.board[selected[0]][selected[1]]
        game.board[selected[0]][selected[1]] = '0'
        drawSquare(game, selected[0], selected[1], True, False, False)
        drawSquare(game, position[0], position[1], True, False, False)
        
        if game.board[position[0]][position[1]] == 'K':
            game.wK = (position[0], position[1])
        elif game.board[position[0]][position[1]] == 'k':
            game.bK = (position[0], position[1])

        if game.board[position[0]][position[1]] == 'P' and selected[0] - position[0]== 2:
            game.enpassant = (position[0], position[1], 1)
        elif game.board[position[0]][position[1]] == 'p' and position[0] - selected[0] == 2:
            game.enpassant = (position[0], position[1], 0)
        else:
            game.enpassant = (-1, -1, -1)
        pygame.display.update()
        return True
    else:
        draw_entire_board(game)
        pygame.display.update()
        return False


