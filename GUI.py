import pygame
import time

# Initialize pygame and predefine some useful stuff
pygame.init()
screen = pygame.display.set_mode((720, 720))
white = (238, 238, 210)
green = (118, 150, 86)
wPawn = pygame.image.load('sprites/white_pawn.png')
wKing = pygame.image.load('sprites/white_king.png')
wQueen = pygame.image.load('sprites/white_queen.png')
wBishop = pygame.image.load('sprites/white_bishop.png')
wKnight = pygame.image.load('sprites/white_knight.png')
wRook = pygame.image.load('sprites/white_rook.png')
bPawn = pygame.image.load('sprites/black_pawn.png')
bKing = pygame.image.load('sprites/black_king.png')
bQueen = pygame.image.load('sprites/black_queen.png')
bBishop = pygame.image.load('sprites/black_bishop.png')
bKnight = pygame.image.load('sprites/black_knight.png')
bRook = pygame.image.load('sprites/black_rook.png')

#temporary table
board = "1rkbqKbkr/2pppppppp|7pppppppp/8rkbqKbkr"

# draw board function
def drawBoard():
    global board
    row = 0
    col = 0
    colour = 'b'
    for i in board:
        posX = 90 * col + 10
        posY = 90 * row + 10
        if i.isdigit():
            row = (int)(i) - 1
        elif i == '|':
            colour = 'w'
            col = 0
        elif i == '/':
            col = 0
        else:
            if colour == 'b':
                if i == 'p':
                    screen.blit(bPawn, (posX + 13, posY + 6))
                elif i == 'K':
                    screen.blit(bKing, (posX + 5, posY + 4))
                elif i == 'q':
                    screen.blit(bQueen, (posX, posY))
                elif i == 'k':
                    screen.blit(bKnight, (posX + 4, posY + 4))
                elif i == 'b':
                    screen.blit(bBishop, (posX + 4, posY + 4))
                else:
                    screen.blit(bRook, (posX + 6, posY + 1)) 
            else:
                if i == 'p':
                    screen.blit(wPawn, (posX + 13, posY + 6))
                elif i == 'K':
                    screen.blit(wKing, (posX + 5, posY + 4))
                elif i == 'q':
                    screen.blit(wQueen, (posX, posY))
                elif i == 'k':
                    screen.blit(wKnight, (posX + 4, posY + 4))
                elif i == 'b':
                    screen.blit(wBishop, (posX + 4, posY + 4))
                else:
                    screen.blit(wRook, (posX + 6, posY + 1)) 
            col += 1
            
def main():
    running = True
    while running:        
        time.sleep(0.01)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouseX, mouseY = pygame.mouse.get_pos()
                    squareX = mouseX // 90 
                    squareY = mouseY // 90

def start():
    pygame.display.set_caption("Chess")
    pygame.display.set_icon(pygame.image.load('pawn.png'))
    screen.fill(white)
    start = 0
    for i in range(0, 8, 1):
        for j in range(1, 8, 2):
            pygame.draw.rect(screen, green, (90 * j  - start, 90 * i, 90, 90))
        if start == 0:
            start = 90
        else:
            start = 0
    drawBoard()
    pygame.display.update()
    main()

start()
