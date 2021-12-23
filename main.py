from constants import *
from gui import *

def isNotSame(selected, position):
    if board[position[0]][position[1]].isdigit():
        return True
    if board[position[0]][position[1]].islower() == board[selected[0]][selected[1]].islower():
        return False
    return True

def switchTurn():
    global turn
    if turn:
        turn = False
    else:
        turn = True
def controller(mouseButton, position):
    global selected
    global highlightMode
    if mouseButton == 1:
        highlightMode = False
        draw_entire_board()
        if not selected == (-1,-1) and isNotSame(selected, position):
            flag = moveSelected(selected, position)
            selected = (-1, -1)
            if flag:
                switchTurn()
        elif selected == position:
            selected = (-1,-1)
        elif board[position[0]][position[1]] != '0' and turn == board[position[0]][position[1]].islower():
            selected = position
            select(position)
    if mouseButton == 3:
        if not highlightMode:
            draw_entire_board()
            highlightMode = True
        drawSquare(position[0], position[1], False, True, False)
        pygame.display.update()
        
def main():
    running = True
    while running:        
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                controller(event.button, (pygame.mouse.get_pos()[1] // 90, pygame.mouse.get_pos()[0] // 90))
            if event.type == pygame.QUIT:
                running = False
        pygame.time.Clock().tick(60)

draw_entire_board()
main()
