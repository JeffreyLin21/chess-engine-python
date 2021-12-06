import pygame
import time

# Initialize pygame and predefine some useful stuff
pygame.mixer.pre_init(44100, 16, 1, 512)
pygame.init()
screen = pygame.display.set_mode((720, 720))
white = (238, 238, 210)
green = (118, 150, 86)
high_green = (186, 202, 43)
high_white = (246, 246, 105)
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
capture_sound = pygame.mixer.Sound("sounds/capture.wav")
colourTable = [
    ['w', 'g', 'w', 'g', 'w', 'g', 'w', 'g'],
    ['g', 'w', 'g', 'w', 'g', 'w', 'g', 'w'],
]

def fenToBoard(fen):
    board = [
        ['0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0']
    ]
    index = 0
    row = 0
    for i in fen:
        if i.isdigit():
            index += (int)(i)
        elif i == '/':
            index = 0
            row += 1
        else:
            board[row][index] = i
            index += 1
    return board

# draw board function
def drawBoard(fen):
    global board
    board = fenToBoard(fen)
    colour = 'b'
    for i in range(8):
        for j in range(8):
            if board[i][j].islower():
                if board[i][j] == 'p':
                    screen.blit(bPawn, (90 * j + 21, 90 * i + 16))
                elif board[i][j] == 'k':
                    screen.blit(bKing, (90 * j + 15, 90 * i + 14))
                elif board[i][j] == 'q':
                    screen.blit(bQueen, (90 * j + 10, 90 * i + 10))
                elif board[i][j] == 'n':
                    screen.blit(bKnight, (90 * j + 14, 90 * i + 14))
                elif board[i][j] == 'b':
                    screen.blit(bBishop, (90 * j + 14, 90 * i + 14))
                elif board[i][j] == 'r':
                    screen.blit(bRook, (90 * j + 16, 90 * i + 11)) 
            else:
                if board[i][j] == 'P':
                    screen.blit(wPawn, (90 * j + 21, 90 * i + 16))
                elif board[i][j] == 'K':
                    screen.blit(wKing, (90 * j + 15, 90 * i + 14))
                elif board[i][j] == 'Q':
                    screen.blit(wQueen, (90 * j + 10, 90 * i + 10))
                elif board[i][j] == 'N':
                    screen.blit(wKnight, (90 * j + 14, 90 * i + 14))
                elif board[i][j] == 'B':
                    screen.blit(wBishop, (90 * j + 14, 90 * i + 14))
                elif board[i][j] == 'R':
                    screen.blit(wRook, (90 * j + 16, 90 * i + 11))  
def main():
    running = True
    square = (-1, -1)
    while running:        
        time.sleep(0.01)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

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
    drawBoard("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR")
    pygame.display.update()
    main()

start()
