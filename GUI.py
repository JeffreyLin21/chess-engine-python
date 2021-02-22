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
hi1 = (-1, -1)
hi2 = (-1, -1)

def unhighlight():
    global hi1
    global hi2
    if hi1[0] == -1:
        return
    if colourTable[hi1[0]%2][hi1[1]] == 'w':
        colour = white
    else:
        colour = green
    if colourTable[hi2[0]%2][hi2[1]] == 'w':
        colour2 = white
    else:
        colour2 = green

    pygame.draw.rect(screen, colour, (90 * hi1[0], 90 * hi1[1], 90, 90))
    pygame.draw.rect(screen, colour2, (90 * hi2[0], 90 * hi2[1], 90, 90))
    i, j = hi2[1], hi2[0]
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

def movePiece(type, start, end, soundType):
    global hi1
    global hi2
    x1, y1 = start
    x2, y2 = end
    if board[y2][x2] != '0':
        sound = capture_sound
        sound2 = capture_sound
    else:
        sound = move1_sound
        sound2 = move2_sound
    if colourTable[x1%2][y1] == 'w':
        colour = high_white
    else:
        colour = high_green
    if colourTable[x2%2][y2] == 'w':
        colour2 = high_white
    else:
        colour2 = high_green   

    pygame.draw.rect(screen, colour, (90 * x1, 90 * y1, 90, 90))
    pygame.draw.rect(screen, colour2, (90 * x2, 90 * y2, 90, 90))
    board[y1][x1] = '0'
    board[y2][x2] = type
    if type.islower():
        if start != end:
            sound.play()
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
        if start != end:
            sound2.play()
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
    hi1 = start
    hi2 = end
    pygame.display.update()
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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if square[0] == -1 and square[1] == -1:
                        #get move list from another function
                        # draw circles to show avalable movelist
                        # unhighlight previous moves
                        mouseX, mouseY = pygame.mouse.get_pos()
                        if board[mouseY//90][mouseX//90] == '0':
                            continue
                        square = (mouseX // 90, mouseY // 90)
                        unhighlight()
                        movePiece(board[square[1]][square[0]], square, square, False)

                    else:
                        mouseX, mouseY = pygame.mouse.get_pos()
                        if board[square[1]][square[0]] != '0':
                            #check if move is in movelist
                            #from from another file will read a txt file of whether castling is still possible, etc
                            #get the type of move this is, capture, move, castle, check, etc
                            movePiece(board[square[1]][square[0]], square, (mouseX // 90, mouseY // 90), False)
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
    drawBoard("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR")
    pygame.display.update()
    main()

start()
