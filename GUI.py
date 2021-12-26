import pygame
from engine import getMoves, isWKingChecked, isBKingChecked

pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()
pygame.font.init()
font = pygame.font.Font("arial.ttf", 30)
pygame.display.set_caption("Chess")
screen = pygame.display.set_mode((720, 720))

def printBoard(game):
    print(game.board[0])
    print(game.board[1])
    print(game.board[2])
    print(game.board[3])
    print(game.board[4])
    print(game.board[5])
    print(game.board[6])
    print(game.board[7])

def addRecord(game):
    fen = ""
    space = 0
    for i in range (8):
        for j in range (8):
            if game.board[i][j] == '0':
                space += 1
            else:
                if not space == 0:
                    fen += (str(space) + game.board[i][j])
                    space = 0
        fen += '/'

    if fen in game.history.keys():
        game.history.update({fen: game.history.get(fen) + 1})
    else:
        game.history.update({fen: 1})

    if game.history.get(fen) == 3:
        return True
    return False

def drawSquare(game, x, y, selected, highlighted, isPossibleMove):

    i,j = x,y
    if game.flipped:
        x = 7-x
        y = 7-y
        

    colour = (0,0,0)
    if game.colourTable[i%2][j%2] == 'w':
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
        if game.board[i][j] == '0':
            pygame.draw.circle(screen, colour, (90 * y + 45, 90 * x + 45), 15)
        else:
            pygame.draw.circle(screen, colour, (90 * y + 45, 90 * x + 45), 44, 6)
    else:
        pygame.draw.rect(screen, colour, (90 * y, 90 * x, 90, 90))
        if game.board[i][j].islower():
            if game.board[i][j] == 'p':
                screen.blit(game.bPawn, (90 * y + 21, 90 * x + 16))
            elif game.board[i][j] == 'k':
                screen.blit(game.bKing, (90 * y + 15, 90 * x + 14))
            elif game.board[i][j] == 'q':
                screen.blit(game.bQueen, (90 * y + 10, 90 * x + 10))
            elif game.board[i][j] == 'n':
                screen.blit(game.bKnight, (90 * y + 14, 90 * x + 14))
            elif game.board[i][j] == 'b':
                screen.blit(game.bBishop, (90 * y + 14, 90 * x + 14))
            elif game.board[i][j] == 'r':
                screen.blit(game.bRook, (90 * y + 16, 90 * x + 11)) 
        else:
            if game.board[i][j] == 'P':
                screen.blit(game.wPawn, (90 * y + 21, 90 * x + 16))
            elif game.board[i][j] == 'K':
                screen.blit(game.wKing, (90 * y + 15, 90 * x + 14))
            elif game.board[i][j] == 'Q':
                screen.blit(game.wQueen, (90 * y + 10, 90 * x + 10))
            elif game.board[i][j] == 'N':
                screen.blit(game.wKnight, (90 * y + 14, 90 * x + 14))
            elif game.board[i][j] == 'B':
                screen.blit(game.wBishop, (90 * y + 14, 90 * x + 14))
            elif game.board[i][j] == 'R':
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

def updateEnPassant(game, selected, position):
    if game.board[position[0]][position[1]] == 'P' and selected[0] - position[0]== 2:
        game.enpassant = (position[0], position[1], 1)
    elif game.board[position[0]][position[1]] == 'p' and position[0] - selected[0] == 2:
        game.enpassant = (position[0], position[1], 0)
    else:
        game.enpassant = (-1, -1, -1)

def updateCastle(game, selected, position):
        if game.board[position[0]][position[1]] == 'K':
            game.wK = (position[0], position[1])
            game.wCastleL = False
            game.wCastleR = False
        elif game.board[position[0]][position[1]] == 'k':
            game.bK = (position[0], position[1])
            game.bCastleL = False
            game.bCastleR = False
        if selected[0] == 0 and selected[1] == 0:
            game.bCastleL = False
        elif selected[0] == 0 and selected[1] == 7:
            game.bCastleR = False
        elif selected[0] == 7 and selected[1] == 0:
            game.wCastleL = False
        elif selected[0] == 7 and selected[1] == 7:
            game.wCastleR = False

def promotePawn(game, position):

    N = 'N'
    B = 'B'
    R = 'R'
    Q = 'Q'
    
    pygame.draw.rect(screen, game.green, (0, 0, 90, 360))

    if position[0] == 0:
        screen.blit(game.wKnight, (15, 16))
        screen.blit(game.wBishop, (15, 106))
        screen.blit(game.wRook, (15, 196))
        screen.blit(game.wQueen, (10, 286))
    else:
        N = 'n'
        B = 'b'
        R = 'r'
        Q = 'q'
        screen.blit(game.bKnight, (15, 16))
        screen.blit(game.bBishop, (15, 106))
        screen.blit(game.bRook, (15, 196))
        screen.blit(game.bQueen, (10, 286))
    
    pygame.display.update()

    running  = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()[1] // 90, pygame.mouse.get_pos()[0] // 90
                if x < 4 and y == 0:
                    running = False
                    if x == 0:
                        game.board[position[0]][position[1]] = N
                    elif x == 1:
                        game.board[position[0]][position[1]] = B
                    elif x == 2:
                        game.board[position[0]][position[1]] = R
                    elif x == 3:
                        game.board[position[0]][position[1]] = Q
    
    draw_entire_board(game)
    drawSquare(game, position[0], position[1], True, False, False)
    pygame.display.update()


def updateSpecial(game, selected, position):
    game.fiftyMove += 1

    if (game.board[selected[0]][selected[1]] == 'P' or game.board[selected[0]][selected[1]] == 'p'):
        game.fiftyMove = 0
    sound = pygame.mixer.Sound('sounds/move.wav')
    if game.board[selected[0]][selected[1]].islower():
        sound = pygame.mixer.Sound('sounds/move2.wav')

    if not game.board[position[0]][position[1]] == '0':
        sound = pygame.mixer.Sound('sounds/capture.wav')
        game.fiftyMove = 0
    if game.board[position[0]][position[1]] == '0' and not position[1] == selected[1]:
        if game.board[selected[0]][selected[1]] == 'P':
            game.board[position[0]+1][position[1]] = '0'
            drawSquare(game, position[0]+1, position[1], True, False, False)
            sound = pygame.mixer.Sound('sounds/capture.wav')
        elif game.board[selected[0]][selected[1]] == 'p':
            game.board[position[0]-1][position[1]] = '0'
            drawSquare(game, position[0]-1, position[1], True, False, False)
            sound = pygame.mixer.Sound('sounds/capture.wav')
    
    if position[1] == 2 or position[1] == 6 and selected[1] == 4:
        if game.board[selected[0]][selected[1]] == 'k' and position[0] == 0:
            if position[1] == 2:
                sound = pygame.mixer.Sound('sounds/castle.wav')
                game.board[0][3] = 'r'
                game.board[0][0] = '0'    
                drawSquare(game, 0, 3, True, False, False)
                drawSquare(game, 0, 0, True, False, False)            
            elif position[1] == 6 and game.bCastleR:
                sound = pygame.mixer.Sound('sounds/castle.wav')
                game.board[0][5] = 'r'
                game.board[0][7] = '0'   
                drawSquare(game, 0, 5, True, False, False)
                drawSquare(game, 0, 7, True, False, False)
        elif game.board[selected[0]][selected[1]] == 'K' and position[0] == 7:
            if position[1] == 2 and game.wCastleL:
                sound = pygame.mixer.Sound('sounds/castle.wav')
                game.board[7][3] = 'R'
                game.board[7][0] = '0'    
                drawSquare(game, 7, 3, True, False, False)
                drawSquare(game, 7, 0, True, False, False)            
            elif position[1] == 6 and game.wCastleR:
                sound = pygame.mixer.Sound('sounds/castle.wav')
                game.board[7][5] = 'R'
                game.board[7][7] = '0'   
                drawSquare(game, 7, 5, True, False, False)
                drawSquare(game, 7, 7, True, False, False)    
    game.board[position[0]][position[1]] = game.board[selected[0]][selected[1]]
    game.board[selected[0]][selected[1]] = '0'

    if game.board[position[0]][position[1]] == 'P' or game.board[position[0]][position[1]] == 'p':
        if position[0] == 0 or position[0] == 7:
            promotePawn(game, position)

    updateCastle(game, selected, position)
    if isWKingChecked(game, 0) or isBKingChecked(game, 1):
        sound = pygame.mixer.Sound('sounds/check.wav')
    
    sound.play()

def points(game):
    game.whitePoints = [0,0,0,0,0]
    game.blackPoints = [0,0,0,0,0]
    for i in range(8):
        for j in range(8):
            if game.board[i][j] == 'P':
                game.whitePoints[0] += 1
            if game.board[i][j] == 'p':
                game.blackPoints[0] += 1
            if game.board[i][j] == 'N':
                game.whitePoints[1] += 1
            if game.board[i][j] == 'n':
                game.blackPoints[1] += 1
            if game.board[i][j] == 'B':
                game.whitePoints[2] += 1
            if game.board[i][j] == 'b':
                game.blackPoints[2] += 1
            if game.board[i][j] == 'R':
                game.whitePoints[3] += 1
            if game.board[i][j] == 'r':
                game.blackPoints[3] += 1
            if game.board[i][j] == 'Q':
                game.whitePoints[4] += 1
            if game.board[i][j] == 'q':
                game.blackPoints[4] += 1
    game.whiteScore = (game.whitePoints[0]) + (game.whitePoints[1] * 3) + (game.whitePoints[2] * 3) + (game.whitePoints[3] * 5) + (game.whitePoints[4] * 9)
    game.blackScore = (game.blackPoints[0]) + (game.blackPoints[1] * 3) + (game.blackPoints[2] * 3) + (game.blackPoints[3] * 5) + (game.blackPoints[4] * 9)

def endGame(game, results):
    sound = pygame.mixer.Sound('sounds/end.wav')
    sound.play()
    pygame.draw.rect(screen, (186, 209, 192), (144, 144, 432, 300))
    text = font.render(game.result.get(results), True, (0, 0 , 0))
    text2 = font.render("Click anywhere to play again", True, (0, 0 , 0))
    if results == 0:
        screen.blit(text, (285, 150))

    elif results == 1:
        screen.blit(text, (285, 150))

    else:
        screen.blit(text, (325, 150))
    screen.blit(text2, (170, 230))
    pygame.display.update()
    running  = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                running = False
    
    game.restart = True

def noMoves(game):
    K = 'K'
    Q = 'Q'
    R = 'R'
    B = 'B'
    N = 'N'
    P = 'P'

    if game.turn:
        K = 'k'
        Q = 'q'
        R = 'r'
        B = 'b'
        N = 'n'
        P = 'p'

    for i in range (8):
        for j in range (8):
            if (game.board[i][j] == K or game.board[i][j] == Q or game.board[i][j] == R or game.board[i][j] == B or game.board[i][j] == N or game.board[i][j] == P) and not getMoves((i, j), game) == []:
                return False
    
    return True

def moveSelected(game, selected, position):
    if position in game.moves:
        updateSpecial(game, selected, position)
        drawSquare(game, selected[0], selected[1], True, False, False)
        drawSquare(game, position[0], position[1], True, False, False)
        updateEnPassant(game, selected, position)
        points(game)
        if addRecord(game):
            endGame(game, 2)
        elif game.fiftyMove == 50:
            endGame(game, 2)
        elif noMoves(game):
            if isWKingChecked(game, 0):
                endGame(game, 1)
            elif isBKingChecked(game, 1):
                endGame(game, 0)
        elif game.whitePoints == [0, 0, 0, 0, 0]:
            if game.blackPoints == [0, 0, 0, 0, 0] or game.blackPoints == [0, 1, 0, 0, 0] or game.blackPoints == [0, 0, 1, 0, 0] or game.blackPoints == [0, 2, 0, 0, 0]:
                endGame(game, 2)
        elif game.whitePoints == [0, 1, 0, 0, 0] or game.blackPoints == [0, 0, 1, 0, 0]:
            if game.blackPoints == [0, 0, 1, 0, 0] or game.blackPoints == [0, 1, 0, 0, 0]:
                endGame(game, 2)
        elif game.blackPoints == [0, 0, 0, 0, 0]:
            if game.whitePoints == [0, 0, 0, 0, 0] or game.whitePoints == [0, 1, 0, 0, 0] or game.whitePoints == [0, 0, 1, 0, 0] or game.whitePoints == [0, 2, 0, 0, 0]:
                endGame(game, 2)
        elif game.blackPoints == [0, 1, 0, 0, 0] or game.blackPoints == [0, 0, 1, 0, 0]:
            if game.whitePoints == [0, 0, 1, 0, 0] or game.whitePoints == [0, 1, 0, 0, 0]:
                endGame(game, 2)
        pygame.display.update()
        return True
    else:
        draw_entire_board(game)
        pygame.display.update()
        return False


