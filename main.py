from constants import *
from gui import *

def isNotSame(selected, position):
    if board[position[0]][position[1]].isdigit():
        return True
    if board[position[0]][position[1]].islower() == board[selected[0]][selected[1]].islower():
        return False
    return True

def controller(mouseButton, position):
    global selected

    if mouseButton == 1:
        if not selected == (-1,-1) and isNotSame(selected, position):
            draw_entire_board()
            moveSelected(selected, position)
            selected = (-1, -1)
        elif selected == position:
            draw_entire_board()
            selected = (-1,-1)
        elif board[position[0]][position[1]] != '0':
            draw_entire_board()
            selected = position
            select(position)

def main():
    running = True
    while running:        
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                controller(event.button, (pygame.mouse.get_pos()[1] // 90, pygame.mouse.get_pos()[0] // 90))
            if event.type == pygame.QUIT:
                running = False
        pygame.time.Clock().tick(60)

draw_entire_board()
main()
