import pygame
import random
from Board_class import Game
from gui import draw_entire_board, printBoard, select, moveSelected, drawSquare
from engine import computeMove

def isNotSame(game, selected, position):
    if game.board[position[0]][position[1]].isdigit():
        return True
    if game.board[position[0]][position[1]].islower() == game.board[selected[0]][selected[1]].islower():
        return False
    return True
 
def switchTurn(game):
    if game.turn:
        game.turn = False
    else:
        game.turn = True
    
def controller(game, mouseButton, position):
    if mouseButton == 1:
        game.highlightMode = False
        draw_entire_board(game)
        if not game.selected == (-1,-1) and isNotSame(game, game.selected, position):
            flag = moveSelected(game, game.selected, position)
            game.selected = (-1, -1)
            if flag:
                switchTurn(game)
        elif game.selected == position:
            game.selected = (-1,-1)
        elif game.board[position[0]][position[1]] != '0' and game.turn == game.board[position[0]][position[1]].islower():
            game.selected = position
            select(game, position)
    if mouseButton == 3:
        if not game.highlightMode:
            draw_entire_board(game)
            game.highlightMode = True
        drawSquare(game, position[0], position[1], False, True, False)
        pygame.display.update()

def refresh(game):
    game.selected = (-1, -1)
    game.turn = False
    game.highlightMode = False
    game.board = [
        ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
        ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
        ['0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0'],
        ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
        ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
    ]
    game.enpassant = (-1, -1, -1)
    game.bK = (0, 4)
    game.wK = (7, 4)
    game.wCastleL = True
    game.wCastleR = True
    game.bCastleL = True
    game.bCastleR = True
    game.initial = '0'
    game.moves = []
    game.history = {}
    game.fiftyMove = 0
    game.blackScore = 0
    game.whiteScore = 0
    game.restart = False
    game.flipped = False

def main(game):
    running = True
    while running:
        if game.restart:
            running = False
            start()     
        if not game.turn == game.flipped:
            computeMove(game, 1, not game.turn, -10000, 10000)
            print(1)
            controller(game, 1, (game.bestMove[0], game.bestMove[1]))
            controller(game, 1, (game.bestMove[2], game.bestMove[3]))
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if game.flipped:
                    controller(game, event.button, (7-(pygame.mouse.get_pos()[1] // 90), 7- (pygame.mouse.get_pos()[0] // 90)))
                else:
                    controller(game, event.button, (pygame.mouse.get_pos()[1] // 90, pygame.mouse.get_pos()[0] // 90))
            if event.type == pygame.QUIT:
                running = False
        pygame.time.Clock().tick(60)

def start():

    game = Game()
    refresh(game)

    if random.randint(0,1) == 1:
        game.flipped = True

    draw_entire_board(game)
    main(game)

start()