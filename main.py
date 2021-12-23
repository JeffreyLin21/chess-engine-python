from Board_class import Game
from gui import draw_entire_board
from gui import pygame
from gui import select
from gui import moveSelected

def isNotSame(game, selected, position):
    if game.board[position[0]][position[1]].isdigit():
        return True
    if game.board[position[0]][position[1]].islower() == board[selected[0]][selected[1]].islower():
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
        
def main(game):
    running = True
    while running:        
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                controller(game, event.button, (pygame.mouse.get_pos()[1] // 90, pygame.mouse.get_pos()[0] // 90))
            if event.type == pygame.QUIT:
                running = False
        pygame.time.Clock().tick(60)

game = Game()
draw_entire_board(game)
main(game)
