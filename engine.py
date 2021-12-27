import math
from tables import *

def switchPos(pos1, pos2, game):

    if game.board[pos1[0]][pos1[1]] == 'K':
        game.wK = (pos2[0], pos2[1])
    elif game.board[pos1[0]][pos1[1]] == 'k':
        game.bK = (pos2[0], pos2[1])

    if game.initial == '0':
        game.initial = game.board[pos2[0]][pos2[1]]
        game.board[pos2[0]][pos2[1]] = game.board[pos1[0]][pos1[1]]
        game.board[pos1[0]][pos1[1]] = '0'
    else:
        game.board[pos2[0]][pos2[1]] = game.board[pos1[0]][pos1[1]]
        game.board[pos1[0]][pos1[1]] = game.initial
        game.initial = '0'      

def isBKingChecked(game, side):
    i, j = game.bK

    if i > 1:
        if j > 0 and game.board[i-2][j-1] == 'N':
            return True
        if j < 7 and game.board[i-2][j+1] == 'N':
            return True
    if i > 0:
        if j > 1 and game.board[i-1][j-2] == 'N':
            return True
        if j < 6 and game.board[i-1][j+2] == 'N':
            return True
    if i < 5:
        if j > 0 and game.board[i+2][j-1] == 'N':
            return True
        if j < 7 and game.board[i+2][j+1] == 'N':
            return True
    if i < 6:
        if j > 1 and game.board[i+1][j-2] == 'N':
            return True
        if j < 6 and game.board[i+1][j+2] == 'N':
            return True
    
    for k in range (i-1, -1, -1):
        if game.board[k][j] == 'R' or game.board[k][j] == 'Q' or (game.board[k][j] == 'K' and k == i-1):
            return True
        if not game.board[k][j].isdigit():
            break

    for k in range (i+1, 8):
        if game.board[k][j] == 'R' or game.board[k][j] == 'Q' or (game.board[k][j] == 'K' and k == i+1):
            return True
        if not game.board[k][j].isdigit():
            break

    for k in range (j-1, -1, -1):
        if game.board[i][k] == 'R' or game.board[i][k] == 'Q' or (game.board[i][k] == 'K' and k == j-1):
            return True
        if not game.board[i][k].isdigit():
            break

    for k in range (j+1, 8):
        if game.board[i][k] == 'R' or game.board[i][k] == 'Q' or (game.board[i][k] == 'K' and k == j+1):
            return True
        if not game.board[i][k].isdigit():
            break

    for k in range (1, min(i, j)+1):
        if game.board[i-k][j-k] == 'B' or game.board[i-k][j-k] == 'Q' or (game.board[i-k][j-k] == 'K' and k == 1):
            return True  
        if not game.board[i-k][j-k].isdigit():
            break

    for k in range (1, min(i, (7-j))+1):
        if game.board[i-k][j+k] == 'B' or game.board[i-k][j+k] == 'Q' or (game.board[i-k][j+k] == 'K' and k == 1):
            return True
        if not game.board[i-k][j+k].isdigit():
            break
    for k in range (1, min((7-i), j)+1):
        if game.board[i+k][j-k] == 'B' or game.board[i+k][j-k] == 'Q' or ((game.board[i+k][j-k] == 'P' or game.board[i+k][j-k] == 'K') and k == 1):
            return True  
        if not game.board[i+k][j-k].isdigit():
            break
        
    for k in range (1, min((7-i), (7-j))+1):
        if game.board[i+k][j+k] == 'B' or game.board[i+k][j+k] == 'Q' or ((game.board[i+k][j+k] == 'P' or game.board[i+k][j+k] == 'K') and k == 1):
            return True
        if not game.board[i+k][j+k].isdigit():
            break
    return False

def isWKingChecked(game, side):

    i, j = game.wK

    if i > 1:
        if j > 0 and game.board[i-2][j-1] =='n':
            return True
        if j < 7 and game.board[i-2][j+1] =='n':
            return True
    if i > 0:
        if j > 1 and game.board[i-1][j-2] =='n':
            return True
        if j < 6 and game.board[i-1][j+2] =='n':
            return True
    if i < 5:
        if j > 0 and game.board[i+2][j-1] =='n':
            return True
        if j < 7 and game.board[i+2][j+1] =='n':
            return True
    if i < 6:
        if j > 1 and game.board[i+1][j-2] =='n':
            return True
        if j < 6 and game.board[i+1][j+2] =='n':
            return True

    for k in range (i-1, -1, -1):
        if game.board[k][j] == 'r' or game.board[k][j] == 'q' or (game.board[k][j] == 'k' and k == i-1):
            return True
        if not game.board[k][j].isdigit():
            break
    
    for k in range (i+1, 8):
        if game.board[k][j] == 'r' or game.board[k][j] == 'q' or (game.board[k][j] == 'k' and k == i+i):
            return True
        if not game.board[k][j].isdigit():
            break
    for k in range (j-1, -1, -1):
        if game.board[i][k] == 'r' or game.board[i][k] == 'q' or (game.board[i][k] == 'k' and k == j-1):
            return True
        if not game.board[i][k].isdigit():
            break   
    for k in range (j+1, 8):
        if game.board[i][k] == 'r' or game.board[i][k] == 'q' or (game.board[i][k] == 'k' and k == j+1):
            return True
        if not game.board[i][k].isdigit():
            break
    for k in range (1, min(i, j)+1):
        if game.board[i-k][j-k] == 'b' or game.board[i-k][j-k] == 'q' or ((game.board[i-k][j-k] == 'p' or game.board[i-k][j-k] == 'k') and k == 1):
            return True  
        if not game.board[i-k][j-k].isdigit():
            break

    for k in range (1, min(i, (7-j))+1):
        if game.board[i-k][j+k] == 'b' or game.board[i-k][j+k] == 'q' or ((game.board[i-k][j+k] == 'p' or game.board[i-k][j+k] == 'k') and k == 1):
            return True
        if not game.board[i-k][j+k].isdigit():
            break

    for k in range (1, min((7-i), j)+1):
        if game.board[i+k][j-k] == 'b' or game.board[i+k][j-k] == 'q' or (game.board[i+k][j-k] == 'k' and k == 1):
            return True  
        if not game.board[i+k][j-k].isdigit():
            break

    for k in range (1, min((7-i), (7-j))+1):
        if game.board[i+k][j+k] == 'b' or game.board[i+k][j+k] == 'q' or (game.board[i+k][j+k] == 'k' and k == 1):
            return True
        if not game.board[i+k][j+k].isdigit():
            break
    return False


def getWP(position, game):
    validMoves = []

    if position[0] > 0 and game.board[position[0]-1][position[1]] == '0':
        switchPos((position[0], position[1]), (position[0]-1, position[1]), game)
        if not isWKingChecked(game, 0):
            validMoves.append((position[0]-1, position[1]))
            if position[0] == 6 and game.board[position[0]-2][position[1]] == '0':
                switchPos((position[0], position[1]), (position[0]-2, position[1]), game)
                if not isWKingChecked(game, 0):
                    validMoves.append((position[0]-2, position[1]))
                switchPos((position[0]-2, position[1]), (position[0], position[1]), game)
        switchPos((position[0]-1, position[1]), (position[0], position[1]), game)

    if position[0] > 0 and position[1] > 0 and game.board[position[0]-1][position[1]-1].islower():
        switchPos((position[0], position[1]), (position[0]-1, position[1]-1), game)
        if not isWKingChecked(game, 0):
            validMoves.append((position[0]-1, position[1]-1))       
        switchPos((position[0]-1, position[1]-1), (position[0], position[1]), game)

    if position[0] > 0 and position[1] < 7 and game.board[position[0]-1][position[1]+1].islower():
        switchPos((position[0], position[1]), (position[0]-1, position[1]+1), game)
        if not isWKingChecked(game, 0):
            validMoves.append((position[0]-1, position[1]+1))  
        switchPos((position[0]-1, position[1]+1), (position[0], position[1]), game)
    if not game.enpassant == (-1, -1, -1) and position[0] == game.enpassant[0] and (position[1] - 1 == game.enpassant[1] or position[1] + 1 == game.enpassant[1]) and game.enpassant[2] == 0:
        switchPos((position[0], position[1]), (game.enpassant[0]-1, game.enpassant[1]), game)
        if not isWKingChecked(game, 0):
            validMoves.append((game.enpassant[0]-1, game.enpassant[1]))       
        switchPos((game.enpassant[0]-1, game.enpassant[1]), (position[0], position[1]), game)
    return validMoves


def getBP(position, game):
    validMoves = []

    if position[0] < 7 and game.board[position[0]+1][position[1]] == '0':
        switchPos((position[0], position[1]), (position[0]+1, position[1]), game)
        if not isBKingChecked(game, 1):
            validMoves.append((position[0]+1, position[1]))
            if position[0] == 1 and game.board[position[0]+2][position[1]] == '0':
                switchPos((position[0], position[1]), (position[0]+2, position[1]), game)
                if not isBKingChecked(game, 1):
                    validMoves.append((position[0]+2, position[1]))
                switchPos((position[0]+2, position[1]), (position[0], position[1]), game)
        switchPos((position[0]+1, position[1]), (position[0], position[1]), game)

    if position[0] < 7 and position[1] > 0 and not game.board[position[0]+1][position[1]-1].islower() and not game.board[position[0]+1][position[1]-1].isdigit():
        switchPos((position[0], position[1]), (position[0]+1, position[1]-1), game)
        if not isBKingChecked(game, 1):
            validMoves.append((position[0]+1, position[1]-1))       
        switchPos((position[0]+1, position[1]-1), (position[0], position[1]),  game)

    if position[0] < 7 and position[1] < 7 and not game.board[position[0]+1][position[1]+1].islower() and not game.board[position[0]+1][position[1]+1].isdigit():
        switchPos((position[0], position[1]), (position[0]+1, position[1]+1), game)
        if not isBKingChecked(game, 1):
            validMoves.append((position[0]+1, position[1]+1))  
        switchPos((position[0]+1, position[1]+1), (position[0], position[1]), game)
    if not game.enpassant == (-1, -1, -1) and position[0] == game.enpassant[0] and (position[1] - 1 == game.enpassant[1] or position[1] + 1 == game.enpassant[1]) and game.enpassant[2] == 1:
        switchPos((position[0], position[1]), (game.enpassant[0]+1, game.enpassant[1]), game)
        if not isBKingChecked(game, 1):
            validMoves.append((game.enpassant[0]+1, game.enpassant[1]))       
        switchPos((game.enpassant[0]+1, game.enpassant[1]), (position[0], position[1]), game)
    return validMoves

def getWB(position, game):
    validMoves = []
    i, j = position[0], position[1]

    for k in range (1, min(i, j)+1):
        if not game.board[i-k][j-k].islower() and not game.board[i-k][j-k].isdigit():
            break        
        switchPos((position[0], position[1]), (position[0]-k, position[1]-k), game)
        if not isWKingChecked(game, 0):
            validMoves.append((position[0]-k, position[1]-k))
        switchPos((position[0]-k, position[1]-k), (position[0], position[1]), game)
        if game.board[i-k][j-k].islower():
            break

    for k in range (1, min(i, (7-j))+1):
        if not game.board[i-k][j+k].islower() and not game.board[i-k][j+k].isdigit():
            break  
        switchPos((position[0], position[1]), (position[0]-k, position[1]+k), game)
        if not isWKingChecked(game, 0):
            validMoves.append((position[0]-k, position[1]+k))
        switchPos((position[0]-k, position[1]+k), (position[0], position[1]), game)
        if game.board[i-k][j+k].islower():
            break
        
    for k in range (1, min((7-i), j)+1):
        if not game.board[i+k][j-k].islower() and not game.board[i+k][j-k].isdigit():
            break  
        switchPos((position[0], position[1]), (position[0]+k, position[1]-k), game)
        if not isWKingChecked(game, 0):
            validMoves.append((position[0]+k, position[1]-k))
        switchPos((position[0]+k, position[1]-k), (position[0], position[1]), game)
        if game.board[i+k][j-k].islower():
            break
        
    for k in range (1, min((7-i), (7-j))+1):
        if not game.board[i+k][j+k].islower() and not game.board[i+k][j+k].isdigit():
            break  
        switchPos((position[0], position[1]), (position[0]+k, position[1]+k), game)
        if not isWKingChecked(game, 0):
            validMoves.append((position[0]+k, position[1]+k))
        switchPos((position[0]+k, position[1]+k), (position[0], position[1]), game)
        if game.board[i+k][j+k].islower():
            break
        
    return validMoves

def getBB(position, game):
    validMoves = []
    i, j = position[0], position[1]

    for k in range (1, min(i, j)+1):
        if game.board[i-k][j-k].islower():
            break  
        switchPos((position[0], position[1]), (position[0]-k, position[1]-k), game)
        if not isBKingChecked(game, 1):
            validMoves.append((position[0]-k, position[1]-k))
        switchPos((position[0]-k, position[1]-k), (position[0], position[1]), game)
        if not game.board[i-k][j-k].islower() and not game.board[i-k][j-k].isdigit():
            break
        
    for k in range (1, min(i, (7-j))+1):
        if game.board[i-k][j+k].islower():
            break  
        switchPos((position[0], position[1]), (position[0]-k, position[1]+k), game)
        if not isBKingChecked(game, 1):
            validMoves.append((position[0]-k, position[1]+k))
        switchPos((position[0]-k, position[1]+k), (position[0], position[1]), game)
        if not game.board[i-k][j+k].isdigit() and not game.board[i-k][j+k].islower():
            break
        
    for k in range (1, min((7-i), j)+1):
        if game.board[i+k][j-k].islower():
            break  
        switchPos((position[0], position[1]), (position[0]+k, position[1]-k), game)
        if not isBKingChecked(game, 1):
            validMoves.append((position[0]+k, position[1]-k))
        switchPos((position[0]+k, position[1]-k), (position[0], position[1]), game)
        if not game.board[i+k][j-k].isdigit() and not game.board[i+k][j-k].islower():
            break
        

    for k in range (1, min((7-i), (7-j))+1):
        if game.board[i+k][j+k].islower():
            break  
        switchPos((position[0], position[1]), (position[0]+k, position[1]+k), game)
        if not isBKingChecked(game, 1):
            validMoves.append((position[0]+k, position[1]+k))
        switchPos((position[0]+k, position[1]+k), (position[0], position[1]), game)
        if not game.board[i+k][j+k].isdigit() and not game.board[i+k][j+k].islower():
            break
        
    return validMoves

def getWN(position, game):
    validMoves = []
    i,j = position[0], position[1]
    if i > 1:
        if j > 0 and(game.board[position[0]-2][position[1]-1].islower() or game.board[position[0]-2][position[1]-1].isdigit()):
            switchPos((position[0], position[1]), (position[0]-2, position[1]-1), game)
            if not isWKingChecked(game, 0):
                validMoves.append((position[0]-2, position[1]-1))
            switchPos((position[0]-2, position[1]-1),(position[0], position[1]), game)
        if j < 7 and(game.board[position[0]-2][position[1]+1].islower() or game.board[position[0]-2][position[1]+1].isdigit()):
            switchPos((position[0], position[1]), (position[0]-2, position[1]+1), game)
            if not isWKingChecked(game, 0):
                validMoves.append((position[0]-2, position[1]+1))
            switchPos((position[0]-2, position[1]+1), (position[0], position[1]), game)
    if i > 0:
        if j > 1 and(game.board[position[0]-1][position[1]-2].islower() or game.board[position[0]-1][position[1]-2].isdigit()):
            switchPos((position[0], position[1]), (position[0]-1, position[1]-2), game)
            if not isWKingChecked(game, 0):
                validMoves.append((position[0]-1, position[1]-2))
            switchPos((position[0]-1, position[1]-2), (position[0], position[1]), game)
        if j < 6 and(game.board[position[0]-1][position[1]+2].islower() or game.board[position[0]-1][position[1]+2].isdigit()):
            switchPos((position[0], position[1]), (position[0]-1, position[1]+2), game)
            if not isWKingChecked(game, 0):
                validMoves.append((position[0]-1, position[1]+2))
            switchPos((position[0]-1, position[1]+2), (position[0], position[1]), game)
    if i < 6:
        if j > 0 and(game.board[position[0]+2][position[1]-1].islower() or game.board[position[0]+2][position[1]-1].isdigit()):
            switchPos((position[0], position[1]), (position[0]+2, position[1]-1), game)
            if not isWKingChecked(game, 0):
                validMoves.append((position[0]+2, position[1]-1))
            switchPos((position[0]+2, position[1]-1), (position[0], position[1]), game)
        if j < 7 and(game.board[position[0]+2][position[1]+1].islower() or game.board[position[0]+2][position[1]+1].isdigit()):
            switchPos((position[0], position[1]), (position[0]+2, position[1]+1), game)
            if not isWKingChecked(game, 0):
                validMoves.append((position[0]+2, position[1]+1))
            switchPos((position[0]+2, position[1]+1), (position[0], position[1]), game)
    if i < 7:
        if j > 1  and(game.board[position[0]+1][position[1]-2].islower() or game.board[position[0]+1][position[1]-2].isdigit()):
            switchPos((position[0], position[1]), (position[0]+1, position[1]-2), game)
            if not isWKingChecked(game, 0):
                validMoves.append((position[0]+1, position[1]-2))
            switchPos((position[0]+1, position[1]-2), (position[0], position[1]), game)
        if j < 6 and(game.board[position[0]+1][position[1]+2].islower() or game.board[position[0]+1][position[1]+2].isdigit()):
            switchPos((position[0], position[1]), (position[0]+1, position[1]+2), game)
            if not isWKingChecked(game, 0):
                validMoves.append((position[0]+1, position[1]+2))
            switchPos((position[0]+1, position[1]+2), (position[0], position[1]), game)

    return validMoves

def getBN(position, game):
    validMoves = []
    i,j = position[0], position[1]
    if i > 1:
        if j > 0 and (not game.board[position[0]-2][position[1]-1].islower()):
            switchPos((position[0], position[1]), (position[0]-2, position[1]-1), game)
            if not isBKingChecked(game, 1):
                validMoves.append((position[0]-2, position[1]-1))
            switchPos((position[0]-2, position[1]-1), (position[0], position[1]), game)
        if j < 7 and (not game.board[position[0]-2][position[1]+1].islower()):
            switchPos((position[0], position[1]), (position[0]-2, position[1]+1), game)
            if not isBKingChecked(game, 1):
                validMoves.append((position[0]-2, position[1]+1))
            switchPos((position[0]-2, position[1]+1), (position[0], position[1]), game)
    if i > 0:
        if j > 1 and (not game.board[position[0]-1][position[1]-2].islower()):
            switchPos((position[0], position[1]), (position[0]-1, position[1]-2), game)
            if not isBKingChecked(game, 1):
                validMoves.append((position[0]-1, position[1]-2))
            switchPos((position[0]-1, position[1]-2), (position[0], position[1]), game)
        if j < 6 and (not game.board[position[0]-1][position[1]+2].islower()):
            switchPos((position[0], position[1]), (position[0]-1, position[1]+2), game)
            if not isBKingChecked(game, 1):
                validMoves.append((position[0]-1, position[1]+2))
            switchPos((position[0]-1, position[1]+2), (position[0], position[1]), game)
    if i < 6:
        if j > 0 and (not game.board[position[0]+2][position[1]-1].islower()):
            switchPos((position[0], position[1]), (position[0]+2, position[1]-1), game)
            if not isBKingChecked(game, 1):
                validMoves.append((position[0]+2, position[1]-1))
            switchPos((position[0]+2, position[1]-1), (position[0], position[1]), game)
        if j < 7 and (not game.board[position[0]+2][position[1]+1].islower()):
            switchPos((position[0], position[1]), (position[0]+2, position[1]+1), game)
            if not isBKingChecked(game, 1):
                validMoves.append((position[0]+2, position[1]+1))
            switchPos((position[0]+2, position[1]+1), (position[0], position[1]), game)
    if i < 7:
        if j > 1 and (not game.board[position[0]+1][position[1]-2].islower()):
            switchPos((position[0], position[1]), (position[0]+1, position[1]-2), game)
            if not isBKingChecked(game, 1):
                validMoves.append((position[0]+1, position[1]-2))
            switchPos((position[0]+1, position[1]-2), (position[0], position[1]), game)
        if j < 6 and (not game.board[position[0]+1][position[1]+2].islower()):
            switchPos((position[0], position[1]), (position[0]+1, position[1]+2), game)
            if not isBKingChecked(game, 1):
                validMoves.append((position[0]+1, position[1]+2))
            switchPos((position[0]+1, position[1]+2), (position[0], position[1]), game)
    return validMoves

def getWR(position, game):
    validMoves = []
    i,j = position[0], position[1]
    for k in range (i-1, -1, -1):
        if not game.board[k][j].islower() and not game.board[k][j].isdigit():
            break
        switchPos((position[0], position[1]), (k, position[1]), game)
        if not isWKingChecked(game, 0):
            validMoves.append((k, position[1]))
        switchPos((k, position[1]), (position[0], position[1]), game)
        if game.board[k][j].islower():
            break
        
    
    for k in range (i+1, 8):
        if not game.board[k][j].islower() and not game.board[k][j].isdigit():
            break
        switchPos((position[0], position[1]), (k, position[1]), game)
        if not isWKingChecked(game, 0):
            validMoves.append((k, position[1]))
        switchPos((k, position[1]), (position[0], position[1]), game)
        if game.board[k][j].islower():
            break
        

    for k in range (j-1, -1, -1):
        if not game.board[i][k].islower() and not game.board[i][k].isdigit():
            break
        switchPos((position[0], position[1]), (position[0], k), game)
        if not isWKingChecked(game, 0):
            validMoves.append((position[0], k))
        switchPos((position[0], k), (position[0], position[1]),  game)
        if game.board[i][k].islower():
            break
        
    
    for k in range (j+1, 8):
        if not game.board[i][k].islower() and not game.board[i][k].isdigit():
            break
        switchPos((position[0], position[1]), (position[0], k), game)
        if not isWKingChecked(game, 0):
            validMoves.append((position[0], k))
        switchPos((position[0], k), (position[0], position[1]), game)
        if game.board[i][k].islower():
            break
        

    return validMoves

def getBR(position, game):
    validMoves = []
    i,j = position[0], position[1]
    for k in range (i-1, -1, -1):
        if game.board[k][j].islower():
            break
        switchPos((position[0], position[1]), (k, position[1]), game)
        if not isBKingChecked(game, 1):
            validMoves.append((k, position[1]))
        switchPos((k, position[1]), (position[0], position[1]), game)
        if not game.board[k][j].islower() and not game.board[k][j].isdigit():
            break
        
    
    for k in range (i+1, 8):
        if game.board[k][j].islower():
            break
        switchPos((position[0], position[1]), (k, position[1]), game)
        if not isBKingChecked(game, 1):
            validMoves.append((k, position[1]))
        switchPos((k, position[1]), (position[0], position[1]), game)
        if not game.board[k][j].islower() and not game.board[k][j].isdigit():
            break
        

    for k in range (j-1, -1, -1):
        if game.board[i][k].islower():
            break
        switchPos((position[0], position[1]), (position[0], k), game)
        if not isBKingChecked(game, 1):
            validMoves.append((position[0], k))
        switchPos((position[0], k), (position[0], position[1]), game)
        if not game.board[i][k].islower() and not game.board[i][k].isdigit():
            break
        
    for k in range (j+1, 8):
        if game.board[i][k].islower():
            break
        switchPos((position[0], position[1]), (position[0], k), game)
        if not isBKingChecked(game, 1):
            validMoves.append((position[0], k))
        switchPos((position[0], k), (position[0], position[1]), game)
        if not game.board[i][k].islower() and not game.board[i][k].isdigit():
            break
        
    return validMoves

def getWQ(position, game):
    validMoves = []
    validMoves.extend(getWB(position, game))
    validMoves.extend(getWR(position, game))
    return validMoves

def getBQ(position, game):
    validMoves = []
    validMoves.extend(getBB(position, game))
    validMoves.extend(getBR(position, game))
    return validMoves

def getWK(position, game):
    validMoves = []

    if position[0] > 0:
        if game.board[position[0]-1][position[1]].islower() or game.board[position[0]-1][position[1]].isdigit():
            switchPos((position[0], position[1]), (position[0]-1, position[1]), game)
            if not isWKingChecked(game, 0):
                validMoves.append((position[0]-1, position[1]))    
            switchPos((position[0]-1, position[1]), (position[0], position[1]), game)
        if position[1] > 0 and(game.board[position[0]-1][position[1]-1].islower() or game.board[position[0]-1][position[1]-1].isdigit()):
            switchPos((position[0], position[1]), (position[0]-1, position[1]-1), game)
            if not isWKingChecked(game, 0):
                validMoves.append((position[0]-1, position[1]-1))           
            switchPos((position[0]-1, position[1]-1), (position[0], position[1]), game)
        if position[1] < 7 and(game.board[position[0]-1][position[1]+1].islower() or game.board[position[0]-1][position[1]+1].isdigit()):
            switchPos((position[0], position[1]), (position[0]-1, position[1]+1), game)
            if not isWKingChecked(game, 0):
                validMoves.append((position[0]-1, position[1]+1))  
            switchPos((position[0]-1, position[1]+1), (position[0], position[1]), game)

    if position[0] < 7:
        if game.board[position[0]+1][position[1]].islower() or game.board[position[0]+1][position[1]].isdigit():
            switchPos((position[0], position[1]), (position[0]+1, position[1]), game)
            if not isWKingChecked(game, 0):
                validMoves.append((position[0]+1, position[1]))   
            switchPos((position[0]+1, position[1]), (position[0], position[1]), game)
        if position[1] > 0 and(game.board[position[0]+1][position[1]-1].islower() or game.board[position[0]+1][position[1]-1].isdigit()):
            switchPos((position[0], position[1]), (position[0]+1, position[1]-1), game)
            if not isWKingChecked(game, 0):
                validMoves.append((position[0]+1, position[1]-1))      
            switchPos((position[0]+1, position[1]-1), (position[0], position[1]), game)     
        if position[1] < 7 and(game.board[position[0]+1][position[1]+1].islower() or game.board[position[0]+1][position[1]+1].isdigit()):
            switchPos((position[0], position[1]), (position[0]+1, position[1]+1), game)
            if not isWKingChecked(game, 0):
                validMoves.append((position[0]+1, position[1]+1))  
            switchPos((position[0]+1, position[1]+1), (position[0], position[1]), game)
    if position[1] > 0:
        if game.board[position[0]][position[1]-1].islower() or game.board[position[0]][position[1]-1].isdigit():
            switchPos((position[0], position[1]), (position[0], position[1]-1), game)
            if not isWKingChecked(game, 0):
                validMoves.append((position[0], position[1]-1))      
            switchPos((position[0], position[1]-1), (position[0], position[1]), game)      
    if position[1] < 7:
        if game.board[position[0]][position[1]+1].islower() or game.board[position[0]][position[1]+1].isdigit():
            switchPos((position[0], position[1]), (position[0], position[1]+1), game)
            if not isWKingChecked(game, 0):
                validMoves.append((position[0], position[1]+1)) 
            switchPos((position[0], position[1]+1), (position[0], position[1]), game)   
    
    if not isWKingChecked(game, 0) and game.wK == (7, 4):
        if game.wCastleL and game.board[7][3] == '0' and game.board[7][2] == '0' and game.board[7][1] == '0':
            switchPos((7, 4), (7, 3), game)
            if not isWKingChecked(game, 1):
                switchPos((7, 3), (7, 2), game)
                if not isWKingChecked(game, 0):
                    validMoves.append((7, 2))
                switchPos((7, 2), (7, 4), game)
            else:
                switchPos((7, 3), (7, 4), game)
            
        if game.wCastleR and game.board[7][5] == '0' and game.board[7][6] == '0':
            switchPos((7, 4), (7, 5), game)
            if not isWKingChecked(game, 0):
                switchPos((7, 5), (7, 6), game)
                if not isWKingChecked(game, 0):
                    validMoves.append((7, 6))
                switchPos((7, 6), (7, 4), game)
            else:
                switchPos((7, 5), (7, 4), game)
    return validMoves

def getBK(position, game):
    validMoves = []

    if position[0] > 0:
        if not game.board[position[0]-1][position[1]].islower():
            switchPos((position[0], position[1]), (position[0]-1, position[1]), game)
            if not isBKingChecked(game, 1):
                validMoves.append((position[0]-1, position[1]))   
            switchPos((position[0]-1, position[1]), (position[0], position[1]), game) 
        if position[1] > 0 and not game.board[position[0]-1][position[1]-1].islower():
            switchPos((position[0], position[1]), (position[0]-1, position[1]-1), game)
            if not isBKingChecked(game, 1):
                validMoves.append((position[0]-1, position[1]-1))    
            switchPos((position[0]-1, position[1]-1), (position[0], position[1]), game)       
        if position[1] < 7 and not game.board[position[0]-1][position[1]+1].islower():
            switchPos((position[0], position[1]), (position[0]-1, position[1]+1), game)
            if not isBKingChecked(game, 1):
                validMoves.append((position[0]-1, position[1]+1))  
            switchPos((position[0]-1, position[1]+1), (position[0], position[1]), game)
    if position[0] < 7:
        if not game.board[position[0]+1][position[1]].islower():
            switchPos((position[0], position[1]), (position[0]+1, position[1]), game)
            if not isBKingChecked(game, 1):
                validMoves.append((position[0]+1, position[1]))   
            switchPos((position[0]+1, position[1]), (position[0], position[1]), game)
        if position[1] > 0 and not game.board[position[0]+1][position[1]-1].islower():
            switchPos((position[0], position[1]), (position[0]+1, position[1]-1), game)
            if not isBKingChecked(game, 1):
                validMoves.append((position[0]+1, position[1]-1))      
            switchPos((position[0]+1, position[1]-1), (position[0], position[1]), game)     
        if position[1] < 7 and not game.board[position[0]+1][position[1]+1].islower():
            switchPos((position[0], position[1]), (position[0]+1, position[1]+1), game)
            if not isBKingChecked(game, 1):
                validMoves.append((position[0]+1, position[1]+1))  
            switchPos((position[0]+1, position[1]+1), (position[0], position[1]), game)

    if position[1] > 0:
        if not game.board[position[0]][position[1]-1].islower():
            switchPos((position[0], position[1]), (position[0], position[1]-1), game)
            if not isBKingChecked(game, 1):
                validMoves.append((position[0], position[1]-1))     
            switchPos((position[0], position[1]-1), (position[0], position[1]), game)       
    if position[1] < 7:
        if not game.board[position[0]][position[1]+1].islower():
            switchPos((position[0], position[1]), (position[0], position[1]+1), game)
            if not isBKingChecked(game, 1):
                validMoves.append((position[0], position[1]+1))    
            switchPos((position[0], position[1]+1), (position[0], position[1]), game)

    if not isBKingChecked(game, 0) and game.bK == (0, 4):
        if game.bCastleL and game.board[0][3] == '0' and game.board[0][2] == '0' and game.board[0][1] == '0':
            switchPos((0, 4), (0, 3), game)
            if not isBKingChecked(game, 0):
                switchPos((0, 3), (0, 2), game)
                if not isBKingChecked(game, 0):
                    validMoves.append((0, 2))
                switchPos((0, 2), (0, 4), game)
            else:
                switchPos((0, 3), (0, 4), game)
            
        if game.bCastleR and game.board[0][5] == '0' and game.board[0][6] == '0':
            switchPos((0, 4), (0, 5), game)
            if not isBKingChecked(game, 0):
                switchPos((0, 5), (0, 6), game)
                if not isBKingChecked(game, 0):
                    validMoves.append((0, 6))
                switchPos((0, 6), (0, 4), game)
            else:
                switchPos((0, 5), (0, 4), game)

    return validMoves

def getMoves(position, game):
    tmp = game.board[position[0]][position[1]]
    if tmp == 'p':
        return getBP(position, game)
    elif tmp == 'P':
        return getWP(position, game)
    elif tmp == 'n':
        return getBN(position, game)
    elif tmp == 'N':
        return getWN(position, game)
    elif tmp == 'b':
        return getBB(position, game)
    elif tmp == 'B':
        return getWB(position, game)
    elif tmp == 'r':
        return getBR(position, game)
    elif tmp == 'R':
        return getWR(position, game)
    elif tmp == 'q':
        return getBQ(position, game)
    elif tmp == 'Q':
        return getWQ(position, game)
    elif tmp == 'k':
        return getBK(position, game)
    elif tmp == 'K':
        return getWK(position, game)
    return

def calculateBoard(game):

    if isWKingChecked(game, 0):
        return -100000

    if isBKingChecked(game, 0):
        return 100000

    sum = 0
    for i in range (8):
        for j in range (8):
            if game.board[i][j] == 'P':
                if game.whiteScore < 14 and game.blackScore < 14:
                    sum += mid_value[0] + mid_pawn_table[i*j]
                else:
                    sum += end_value[0] + end_pawn_table[i*j]
            elif game.board[i][j] == 'N':
                if game.whiteScore < 14 and game.blackScore < 14:
                    sum += mid_value[1] + mid_knight_table[i*j]
                else:
                    sum += end_value[1] + end_knight_table[i*j]
            elif game.board[i][j] == 'B':
                if game.whiteScore < 14 and game.blackScore < 14:
                    sum += mid_value[2] + mid_bishop_table[i*j]
                else:
                    sum += mid_value[2] + end_bishop_table[i*j]
            elif game.board[i][j] == 'R':
                if game.whiteScore < 14 and game.blackScore < 14:
                    sum += mid_value[3] + mid_rook_table[i*j]
                else:
                    sum += mid_value[3] + end_rook_table[i*j]
            elif game.board[i][j] == 'Q':
                if game.whiteScore < 14 and game.blackScore < 14:
                    sum += mid_value[4] + mid_queen_table[i*j]
                else:
                    sum += mid_value[4] + end_queen_table[i*j]
            elif game.board[i][j] == 'K':
                if game.whiteScore < 14 and game.blackScore < 14:
                    sum += mid_king_table[i*j]
                else:
                    sum += end_king_table[i*j]
            elif game.board[i][j] == 'p':
                if game.whiteScore < 14 and game.blackScore < 14:
                    sum = sum - mid_value[0] - mid_pawn_table[flip[i*j]]
                else:
                    sum = sum - end_value[0] - end_pawn_table[flip[i*j]]
            elif game.board[i][j] == 'n':
                if game.whiteScore < 14 and game.blackScore < 14:
                    sum = sum - mid_value[1] - mid_knight_table[flip[i*j]]
                else:
                    sum = sum - end_value[1] - end_knight_table[flip[i*j]]
            elif game.board[i][j] == 'b':
                if game.whiteScore < 14 and game.blackScore < 14:
                    sum = sum - mid_value[2] - mid_bishop_table[flip[i*j]]
                else:
                    sum = sum - mid_value[2] - end_bishop_table[flip[i*j]]
            elif game.board[i][j] == 'r':
                if game.whiteScore < 14 and game.blackScore < 14:
                    sum = sum - mid_value[3] - mid_rook_table[flip[i*j]]
                else:
                    sum = sum - mid_value[3] - end_rook_table[flip[i*j]]
            elif game.board[i][j] == 'q':
                if game.whiteScore < 14 and game.blackScore < 14:
                    sum = sum - mid_value[4] - mid_queen_table[flip[i*j]]
                else:
                    sum = sum - mid_value[4] - end_queen_table[flip[i*j]]
            elif game.board[i][j] == 'k':
                if game.whiteScore < 14 and game.blackScore < 14:
                    sum = sum - mid_king_table[flip[i*j]]
                else:
                    sum = sum - end_king_table[flip[i*j]]
    return sum

def computeMove(game, depth, isMaximizingPlayer, alpha, beta):
    if depth == 0:
        return calculateBoard(game)

    if isMaximizingPlayer:
        bestVal = -1000000
        for i in range (8):
            for j in range (8):
                if not game.board[i][j] == '0' and not game.board[i][j].islower():
                    for move in getMoves( (i, j), game):
                        switchPos((i, j), move, game)

                        if game.board[move[0]][move[1]] == 'P' and move[0] == 0:
                            game.board[move[0]][move[1]] = 'N'
                            val = computeMove(game, depth - 1, False, alpha, beta)
                            if val > bestVal:
                                bestVal = val
                                game.bestMove = (i, j, move[0], move[1], 'N')
                            alpha = max( alpha, bestVal)
                            if beta <= alpha:
                                bestVal = val
                                game.board[move[0]][move[1]] = 'p'
                                switchPos(move, (i, j), game)
                                return bestVal
                            game.board[move[0]][move[1]] = 'B'
                            val = computeMove(game, depth - 1, False, alpha, beta)
                            if val > bestVal:
                                game.bestMove = (i, j, move[0], move[1], 'B')
                            alpha = max( alpha, bestVal)
                            if beta <= alpha:
                                bestVal = val
                                game.board[move[0]][move[1]] = 'p'
                                switchPos(move, (i, j), game)
                                return bestVal
                            game.board[move[0]][move[1]] = 'R'
                            val = computeMove(game, depth - 1, False, alpha, beta)
                            if val > bestVal:
                                bestVal = val
                                game.bestMove = (i, j, move[0], move[1], 'R')
                            alpha = max( alpha, bestVal)
                            if beta <= alpha:
                                game.board[move[0]][move[1]] = 'p'
                                switchPos(move, (i, j), game)
                                return bestVal
                            game.board[move[0]][move[1]] = 'Q'
                            val = computeMove(game, depth - 1, False, alpha, beta)
                            if val > bestVal:
                                bestVal = val
                                game.bestMove = (i, j, move[0], move[1], 'Q')
                            alpha = max( alpha, bestVal)
                            if beta <= alpha:
                                game.board[move[0]][move[1]] = 'p'
                                switchPos(move, (i, j), game)
                                return bestVal
                            game.board[move[0]][move[1]] = 'P'

                        elif game.board[move[0]][move[1]] == 'p' and move[0] == 7:
                            game.board[move[0]][move[1]] = 'n'
                            val = computeMove(game, depth - 1, False, alpha, beta)
                            if val > bestVal:
                                bestVal = val
                                game.bestMove = (i, j, move[0], move[1], 'n')
                            alpha = max( alpha, bestVal)
                            if beta <= alpha:
                                game.board[move[0]][move[1]] = 'p'
                                switchPos(move, (i, j), game)
                                return bestVal
                            game.board[move[0]][move[1]] = 'b'
                            val = computeMove(game, depth - 1, False, alpha, beta)
                            if val > bestVal:
                                bestVal = val
                                game.bestMove = (i, j, move[0], move[1], 'b')
                            alpha = max( alpha, bestVal)
                            if beta <= alpha:
                                game.board[move[0]][move[1]] = 'p'
                                switchPos(move, (i, j), game)
                                return bestVal
                            game.board[move[0]][move[1]] = 'r'
                            val = computeMove(game, depth - 1, False, alpha, beta)
                            if val > bestVal:
                                bestVal = val
                                game.bestMove = (i, j, move[0], move[1], 'r')
                            alpha = max( alpha, bestVal)
                            if beta <= alpha:
                                game.board[move[0]][move[1]] = 'p'
                                switchPos(move, (i, j), game)
                                return bestVal
                            game.board[move[0]][move[1]] = 'q'
                            val = computeMove(game, depth - 1, False, alpha, beta)
                            if val > bestVal:
                                bestVal = val
                                game.bestMove = (i, j, move[0], move[1], 'q')
                            alpha = max( alpha, bestVal)
                            if beta <= alpha:
                                game.board[move[0]][move[1]] = 'p'
                                switchPos(move, (i, j), game)
                                return bestVal                                
                            game.board[move[0]][move[1]] = 'p'
                        else:
                            val = computeMove(game, depth - 1, False, alpha, beta)
                            if val > bestVal:
                                bestVal = val
                                game.bestMove = (i, j, move[0], move[1], -1)
                            alpha = max( alpha, bestVal)
                            if beta <= alpha:
                                switchPos(move, (i, j), game)
                                return bestVal
                        switchPos(move, (i, j), game)

        return bestVal
    
    else:
        bestVal = 1000000
        for i in range (8):
            for j in range (8):
                if game.board[i][j].islower():
                    for move in getMoves( (i, j), game):
                        switchPos((i, j), move, game)

                        if game.board[move[0]][move[1]] == 'P' and move[0] == 0:
                            game.board[move[0]][move[1]] = 'N'
                            val = computeMove(game, depth - 1, False, alpha, beta)
                            if val < bestVal:
                                bestVal = val
                                game.bestMove = (i, j, move[0], move[1], 'N')
                            beta = min( beta, bestVal)
                            if beta <= alpha:
                                game.board[move[0]][move[1]] = 'p'
                                switchPos(move, (i, j), game)
                                return bestVal
                            game.board[move[0]][move[1]] = 'B'
                            val = computeMove(game, depth - 1, False, alpha, beta)
                            if val < bestVal:
                                bestVal = val
                                game.bestMove = (i, j, move[0], move[1], 'B')
                            beta = min( beta, bestVal)
                            if beta <= alpha:
                                game.board[move[0]][move[1]] = 'p'
                                switchPos(move, (i, j), game)
                                return bestVal
                            game.board[move[0]][move[1]] = 'R'
                            val = computeMove(game, depth - 1, False, alpha, beta)
                            if val < bestVal:
                                bestVal = val
                                game.bestMove = (i, j, move[0], move[1], 'R')
                            beta = min( beta, bestVal)
                            if beta <= alpha:
                                game.board[move[0]][move[1]] = 'p'
                                switchPos(move, (i, j), game)
                                return bestVal
                            game.board[move[0]][move[1]] = 'Q'
                            val = computeMove(game, depth - 1, False, alpha, beta)
                            if val < bestVal:
                                bestVal = val
                                game.bestMove = (i, j, move[0], move[1], 'Q')
                            beta = min( beta, bestVal)
                            if beta <= alpha:
                                game.board[move[0]][move[1]] = 'p'
                                switchPos(move, (i, j), game)
                                return bestVal
                            game.board[move[0]][move[1]] = 'P'

                        elif game.board[move[0]][move[1]] == 'p' and move[0] == 7:
                            game.board[move[0]][move[1]] = 'n'
                            val = computeMove(game, depth - 1, False, alpha, beta)
                            if val < bestVal:
                                bestVal = val
                                game.bestMove = (i, j, move[0], move[1], 'n')
                            beta = min( beta, bestVal)
                            if beta <= alpha:
                                game.board[move[0]][move[1]] = 'p'
                                switchPos(move, (i, j), game)
                                return bestVal
                            game.board[move[0]][move[1]] = 'b'
                            val = computeMove(game, depth - 1, False, alpha, beta)
                            if val < bestVal:
                                bestVal = val
                                game.bestMove = (i, j, move[0], move[1], 'b')
                            beta = min( beta, bestVal)
                            if beta <= alpha:
                                game.board[move[0]][move[1]] = 'p'
                                switchPos(move, (i, j), game)
                                return bestVal
                            game.board[move[0]][move[1]] = 'r'
                            val = computeMove(game, depth - 1, False, alpha, beta)
                            if val < bestVal:
                                bestVal = val
                                game.bestMove = (i, j, move[0], move[1], 'r')
                            beta = min( beta, bestVal)
                            if beta <= alpha:
                                game.board[move[0]][move[1]] = 'p'
                                switchPos(move, (i, j), game)
                                return bestVal
                            game.board[move[0]][move[1]] = 'q'
                            val = computeMove(game, depth - 1, False, alpha, beta)
                            if val < bestVal:
                                bestVal = val
                                game.bestMove = (i, j, move[0], move[1], 'q')
                            beta = min( beta, bestVal)
                            if beta <= alpha:
                                game.board[move[0]][move[1]] = 'p'
                                switchPos(move, (i, j), game)
                                return bestVal                                
                            game.board[move[0]][move[1]] = 'p'
                        else:
                            val = computeMove(game, depth - 1, False, alpha, beta)
                            if val < bestVal:
                                bestVal = val
                                game.bestMove = (i, j, move[0], move[1], -1)
                            beta = min( beta, bestVal)
                            if beta <= alpha:
                                switchPos(move, (i, j), game)
                                return bestVal
                        switchPos(move, (i, j), game)
        return bestVal