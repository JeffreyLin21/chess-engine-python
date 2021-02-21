import pygame
import time

# Initialize pygame and predefine some useful stuff
pygame.mixer.pre_init(44100, -16, 1, 512)
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
move1_sound = pygame.mixer.Sound("sounds/move.wav")
move2_sound = pygame.mixer.Sound("sounds/move2.wav")
colourTable = [
    ['w', 'g', 'w', 'g', 'w', 'g', 'w', 'g'],
    ['g', 'w', 'g', 'w', 'g', 'w', 'g', 'w'],
]
board = [
    ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
    ['0', '0', '0', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0', '0', '0', '0'],
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
    ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
]


def movePiece(type, start, end):
    x1, y1 = start
    x2, y2 = end
    if colourTable[x1%2][y1] == 'w':
        colour = white
    else:
        colour = green
    if colourTable[x2%2][y2] == 'w':
        colour2 = white
    else:
        colour2 = green   

    pygame.draw.rect(screen, colour, (90 * x1, 90 * y1, 90, 90))
    pygame.draw.rect(screen, colour2, (90 * x2, 90 * y2, 90, 90))
    board[y1][x1] = '0'
    board[y2][x2] = type
    if type.islower():
        move1_sound.play()
        if type == 'p':
            screen.blit(bPawn, (x2 * 90 + 21, y2 * 90 + 16))
        elif type == 'k':
            screen.blit(bKing, (x2 * 90 + 15, y2 * 90 + 14))
        elif type == 'q':
            screen.blit(bQueen, (x2 * 90 + 10, y2 * 90 + 10))
        elif type == 'n':
            screen.blit(bKnight, (x2 * 90 + 14, y2 * 90 + 14))
        elif type == 'b':
            screen.blit(bBishop, (x2 * 90 + 14, y2 * 90 + 14))
        elif type == 'r':
            screen.blit(bRook, (x2 * 90 + 16, y2 * 90 + 11)) 
    else:
        move2_sound.play()
        if type == 'P':
            screen.blit(wPawn, (x2 * 90 + 23, y2 * 90 + 16))
        elif type == 'K':
            screen.blit(wKing, (x2 * 90 + 15, y2 * 90 + 14))
        elif type == 'Q':
            screen.blit(wQueen, (x2 * 90 + 10, y2 * 90 + 10))
        elif type == 'N':
            screen.blit(wKnight, (x2 * 90 + 14, y2 * 90 + 14))
        elif type == 'B':
            screen.blit(wBishop, (x2 * 90 + 14, y2 * 90 + 14))
        else:
            screen.blit(wRook, (x2 * 90 + 16, y2 * 90 + 11))  
    pygame.display.update()
# draw board function
def drawBoard():
    global board
    colour = 'b'
    for i in range(8):
        for j in range(8):
            posX = 90 * j + 10
            posY = 90 * i + 10
            if board[i][j].islower():
                if board[i][j] == 'p':
                    screen.blit(bPawn, (posX + 11, posY + 6))
                elif board[i][j] == 'k':
                    screen.blit(bKing, (posX + 5, posY + 4))
                elif board[i][j] == 'q':
                    screen.blit(bQueen, (posX, posY))
                elif board[i][j] == 'n':
                    screen.blit(bKnight, (posX + 4, posY + 4))
                elif board[i][j] == 'b':
                    screen.blit(bBishop, (posX + 4, posY + 4))
                elif board[i][j] == 'r':
                    screen.blit(bRook, (posX + 6, posY + 1)) 
            else:
                if board[i][j] == 'P':
                    screen.blit(wPawn, (posX + 11, posY + 6))
                elif board[i][j] == 'K':
                    screen.blit(wKing, (posX + 5, posY + 4))
                elif board[i][j] == 'Q':
                    screen.blit(wQueen, (posX, posY))
                elif board[i][j] == 'N':
                    screen.blit(wKnight, (posX + 4, posY + 4))
                elif board[i][j] == 'B':
                    screen.blit(wBishop, (posX + 4, posY + 4))
                elif board[i][j] == 'R':
                    screen.blit(wRook, (posX + 6, posY + 1)) 
            
def main():
    running = True
    square = (-1, -1)
    while running:        
        time.sleep(0.01)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if square[0] == -1 and square[1] == -1:
                        mouseX, mouseY = pygame.mouse.get_pos()
                        if board[mouseY//90][mouseX//90] == '0':
                            continue
                        square = (mouseX // 90, mouseY // 90)
                        print(square)
                    else:
                        mouseX, mouseY = pygame.mouse.get_pos()
                        if board[square[1]][square[0]] != '0':
                            movePiece(board[square[1]][square[0]], square, (mouseX // 90, mouseY // 90))
                            square = (-1, -1)

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
