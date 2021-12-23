import pygame
pygame.init()

white = (238, 238, 210)
green = (118, 150, 86)
selected_green = (186, 202, 43)
selected_white = (246, 246, 105)
high_white = (236,126,106)
high_green = (212,108,81)
move_white = (214,214,189)
move_green = (106,135,77)
selected = (-1, -1)
bK = (0, 4)
wK = (7, 4)
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
turn = False
highlightMode = False
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
    ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
]
enpassent = (-1, -1)
wCastleL = True
wCastleR = True
bCastleL = True
bCastleR = True
initial = '0'
moves = []
