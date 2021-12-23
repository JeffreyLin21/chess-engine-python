from constants import *

def switchPos(pos1, pos2, tmpBoard):
    tmpBoard[pos2[0]][pos2[1]] = tempBoard[pos1[0]][pos1[1]]
    tmpBoard[pos1[0]][pos1[1]] = '0'
    return tmpBoard


def isWKingChecked(tmpBoard, side):

    target = 'K'
    q = 'q'
    n = 'n'
    b = 'b'
    p = 'p'
    r = 'r'
    if side == 1:
        target = 'k'
        q = 'Q'
        n = 'N'
        b = 'B'
        p = 'P'
        r = 'R'

    i, j = 0, 0
    for i in range(8):
        for j in range(8):
            if tmpBoard[i][j] == target:
                break

    if i > 1:
        if j > 0 and tmpBoard[i-2][j-1] == n:
            return True
        if j < 7 and tmpBoard[i-2][j+1] == n:
            return True
    if i > 0:
        if j > 1 and tmpBoard[i-1][j-2] == n:
            return True
        if j < 6 and tmpBoard[i-1][j+2] == n:
            return True
    if i < 5:
        if j > 0 and tmpBoard[i+2][j-1] == n:
            return True
        if j < 7 and tmpBoard[i+2][j+1] == n:
            return True
    if i < 6:
        if j > 1 and tmpBoard[i+1][j-2] == n:
            return True
        if j < 6 and tmpBoard[i+1][j+2] == n:
            return True

    for k in range (i-1, -1, -1):
        if not board[k][j].isdigit() and board[k][j].islower():
            break
        if board[k][j] == r or board[k][j] == q:
            return True
    
    for k in range (i+1, 8):
        if not board[k][j].isdigit() and board[k][j].islower():
            break
        if board[k][j] == r or board[k][j] == q:
            return True

    for k in range (j-1, -1, -1):
        if not board[i][k].isdigit() and board[i][k].islower():
            break
        if board[i][k] == r or board[i][k] == q:
            return True
    
    for k in range (j+1, 8):
        if not board[i][k].isdigit() and board[i][k].islower():
            break
        if board[i][k] == r or board[i][k] == q:
            return True


    for k in range (1, min(i, j)+1):
        if not board[i-k][j-k].isdigit() and board[i-k][j-k].islower():
            break
        if board[i-k][j-k] == 'b' or board[i-k][j-k] == q or board[i-k][j-k] == p:
            return True  

    for k in range (1, min(i, (7-j))+1):
        if not board[i-k][j+k].isdigit() and board[i-k][j+k].islower():
            break
        if board[i-k][j+k] == 'b' or board[i-k][j+k] == q or board[i-k][j+k] == p:
            return True
    
    for k in range (1, min((7-i), j)+1):
        if not board[i+k][j-k].isdigit() and board[i+k][j-k].islower():
            break
        if board[i+k][j-k] == 'b' or board[i+k][j-k] == q or board[i+k][j-k] == p:
            return True  

    for k in range (1, min((7-i), (7-j))+1):
        if not board[i+k][j+k].isdigit() and board[i+k][j+k].islower():
            break
        if board[i+k][j+k] == 'b' or board[i+k][j+k] == q or board[i+k][j+k] == p:
            return True

    return False
def getWP(position, tmpBoard):
    validMoves = []

    if position[0] > 0 and tmpBoard[position[0]-1][position[1]] == '0':
        tmpBoard = switchPos((position[0], position[1]), (position[0]-1, position[1]), tmpBoard)
        if not isKingChecked(tmpBoard, 0):
            validMoves.append((position[0]-1, position[1]))
            if position[0] == 6 and tmpBoard[position[0]-2][position[1]] == '0':
                tmpBoard = switchPos((position[0], position[1]), (position[0]-2, position[1]), tmpBoard)
                if not isKingChecked(tmpBoard, 0):
                    validMoves.append((position[0]-2, position[1]))

    if position[0] > 0 and position[1] > 0 and tmpBoard[position[0]-1][position[1]-1].islower():
        tmpBoard = switchPos((position[0], position[1]), (position[0]-1, position[1]-1), tmpBoard)
        if not isKingChecked(tmpBoard, 0):
            validMoves.append((position[0]-1, position[1]-1))       

    if position[0] > 0 and position[1] < 7 and tmpBoard[position[0]-1][position[1]+1].islower():
        tmpBoard = switchPos((position[0], position[1]), (position[0]+1, position[1]+1), tmpBoard)
        if not isKingChecked(tmpBoard, 0):
            validMoves.append((position[0]+1, position[1]+1))  

    if not enpassent == (-1, -1) and position[0] == enpassent[0] and (position[1] - 1 == enpassent[1] or position[1] + 1 == enpassent[1]):
        tmpBoard = switchPos((position[0], position[1]), (enpassent[0]-1, enpassent[1]), tmpBoard)
        if not isKingChecked(tmpBoard, 0):
            validMoves.append((enpassent[0]-1, enpassent[1]))       

    return validMoves


def getBP(position, tmpBoard):
    validMoves = []

    if position[0] < 7 and tmpBoard[position[0]+1][position[1]] == '0':
        tmpBoard = switchPos((position[0], position[1]), (position[0]+1, position[1]), tmpBoard)
        if not isKingChecked(tmpBoard, 1):
            validMoves.append((position[0]+1, position[1]))
            if position[0] == 1 and tmpBoard[position[0]+2][position[1]] == '0':
                tmpBoard = switchPos((position[0], position[1]), (position[0]+2, position[1]), tmpBoard)
                if not isKingChecked(tmpBoard, 1):
                    validMoves.append((position[0]+2, position[1]))

    if position[0] < 7 and position[1] > 0 and not tmpBoard[position[0]+1][position[1]-1].islower():
        tmpBoard = switchPos((position[0], position[1]), (position[0]+1, position[1]-1), tmpBoard)
        if not isKingChecked(tmpBoard, 1):
            validMoves.append((position[0]+1, position[1]-1))       

    if position[0] < 7 and position[1] < 7 and not tmpBoard[position[0]+1][position[1]+1].islower():
        tmpBoard = switchPos((position[0], position[1]), (position[0]+1, position[1]+1), tmpBoard)
        if not isKingChecked(tmpBoard, 1):
            validMoves.append((position[0]+1, position[1]+1))  

    if not enpassent == (-1, -1) and position[0] == enpassent[0] and (position[1] - 1 == enpassent[1] or position[1] + 1 == enpassent[1]):
        tmpBoard = switchPos((position[0], position[1]), (enpassent[0]+1, enpassent[1]), tmpBoard)
        if not isKingChecked(tmpBoard, 1):
            validMoves.append((enpassent[0]+1, enpassent[1]))       

    return validMoves

def getWB(position, tmpBoard):
    validMoves = []
    i, j = position[0], position[1]

    for k in range (1, min(i, j)+1):
        if not board[i-k][j-k].islower():
            break        
        tmpBoard = switchPos((position[0], position[1]), (position[0]-k, position[1]-k), tmpBoard)
        if not isKingChecked(tmpBoard, 0):
            validMoves.append((position[0]-k, position[1]-k))
        if not board[i-k][j-k].isdigit() and board[i-k][j-k].islower():
            break

    for k in range (1, min(i, (7-j))+1):
        if not board[i-k][j+k].islower():
            break  
        tmpBoard = switchPos((position[0], position[1]), (position[0]-k, position[1]+k), tmpBoard)
        if not isKingChecked(tmpBoard, 0):
            validMoves.append((position[0]-k, position[1]+k))
        if not board[i-k][j+k].isdigit() and board[i-k][j+k].islower():
            break
    
    for k in range (1, min((7-i), j)+1):
        if not board[i+k][j-k].islower():
            break  
        tmpBoard = switchPos((position[0], position[1]), (position[0]+k, position[1]-k), tmpBoard)
        if not isKingChecked(tmpBoard, 0):
            validMoves.append((position[0]+k, position[1]-k))
        if not board[i+k][j-k].isdigit() and board[i+k][j-k].islower():
            break

    for k in range (1, min((7-i), (7-j))+1):
        if not board[i+k][j+k].islower():
            break  
        tmpBoard = switchPos((position[0], position[1]), (position[0]+k, position[1]+k), tmpBoard)
        if not isKingChecked(tmpBoard, 0):
            validMoves.append((position[0]+k, position[1]+k))
        if not board[i+k][j+k].isdigit() and board[i+k][j+k].islower():
            break

    return validMoves

def getBB(position, tmpBoard):
    validMoves = []
    i, j = position[0], position[1]

    for k in range (1, min(i, j)+1):
        if board[i-k][j-k].islower():
            break  
        tmpBoard = switchPos((position[0], position[1]), (position[0]-k, position[1]-k), tmpBoard)
        if not isKingChecked(tmpBoard, 1):
            validMoves.append((position[0]-k, position[1]-k))
        if not board[i-k][j-k].islower():
            break

    for k in range (1, min(i, (7-j))+1):
        if board[i-k][j+k].islower():
            break  
        tmpBoard = switchPos((position[0], position[1]), (position[0]-k, position[1]+k), tmpBoard)
        if not isKingChecked(tmpBoard, 1):
            validMoves.append((position[0]-k, position[1]+k))
        if not board[i-k][j+k].isdigit() and not board[i-k][j+k].islower():
            break
    
    for k in range (1, min((7-i), j)+1):
        if board[i+k][j-k].islower():
            break  
        tmpBoard = switchPos((position[0], position[1]), (position[0]+k, position[1]-k), tmpBoard)
        if not isKingChecked(tmpBoard, 1):
            validMoves.append((position[0]+k, position[1]-k))
        if not board[i+k][j-k].isdigit() and not board[i+k][j-k].islower():
            break

    for k in range (1, min((7-i), (7-j))+1):
        if board[i+k][j+k].islower():
            break  
        tmpBoard = switchPos((position[0], position[1]), (position[0]+k, position[1]+k), tmpBoard)
        if not isKingChecked(tmpBoard, 1):
            validMoves.append((position[0]+k, position[1]+k))
        if not board[i+k][j+k].isdigit() and not board[i+k][j+k].islower():
            break

    return validMoves

def getWN(position, tmpBoard):
    i,j = position[0], position[1]
    if i > 1:
        if j > 0 and board[position[0]-2][position[1]-1].islower() and not board[position[0]-2][position[1]-1].isdigit():
            tmpBoard = switchPos((position[0], position[1]), (position[0]-2, position[1]-1), tmpBoard)
            if not isKingChecked(tmpBoard, 0):
                validMoves.append((position[0]-2, position[1]-1))
        if j < 7 and board[position[0]-2][position[1]+1].islower() and not board[position[0]-2][position[1]+1].isdigit():
            tmpBoard = switchPos((position[0], position[1]), (position[0]-2, position[1]+1), tmpBoard)
            if not isKingChecked(tmpBoard, 0):
                validMoves.append((position[0]-2, position[1]+1))
    if i > 0:
        if j > 1 and board[position[0]-1][position[1]-2].islower() and not board[position[0]-1][position[1]-2].isdigit():
            tmpBoard = switchPos((position[0], position[1]), (position[0]-1, position[1]-2), tmpBoard)
            if not isKingChecked(tmpBoard, 0):
                validMoves.append((position[0]-1, position[1]-2))
        if j < 6 and board[position[0]-1][position[1]+2].islower() and not board[position[0]-1][position[1]+2].isdigit():
            tmpBoard = switchPos((position[0], position[1]), (position[0]-1, position[1]+2), tmpBoard)
            if not isKingChecked(tmpBoard, 0):
                validMoves.append((position[0]-1, position[1]+2))
    if i < 5:
        if j > 0 and board[position[0]+2][position[1]-1].islower() and not board[position[0]+2][position[1]-1].isdigit():
            tmpBoard = switchPos((position[0], position[1]), (position[0]+2, position[1]-1), tmpBoard)
            if not isKingChecked(tmpBoard, 0):
                validMoves.append((position[0]+2, position[1]-1))
        if j < 7 and board[position[0]+2][position[1]+1].islower() and not board[position[0]+2][position[1]+1].isdigit():
            tmpBoard = switchPos((position[0], position[1]), (position[0]+2, position[1]+1), tmpBoard)
            if not isKingChecked(tmpBoard, 0):
                validMoves.append((position[0]+2, position[1]+1))
    if i < 6:
        if j > 1  and board[position[0]+1][position[1]-2].islower() and not board[position[0]+1][position[1]-2].isdigit():
            tmpBoard = switchPos((position[0], position[1]), (position[0]+1, position[1]-2), tmpBoard)
            if not isKingChecked(tmpBoard, 0):
                validMoves.append((position[0]+1, position[1]-2))
        if j < 6 and board[position[0]+1][position[1]+2].islower() and not board[position[0]+1][position[1]+2].isdigit():
            tmpBoard = switchPos((position[0], position[1]), (position[0]+1, position[1]+2), tmpBoard)
            if not isKingChecked(tmpBoard, 0):
                validMoves.append((position[0]+1, position[1]+2))

    return validMoves

def getBN(position, tmpBoard):
    i,j = position[0], position[1]
    if i > 1:
        if j > 0 and not board[position[0]-2][position[1]-1].islower():
            tmpBoard = switchPos((position[0], position[1]), (position[0]-2, position[1]-1), tmpBoard)
            if not isKingChecked(tmpBoard, 1):
                validMoves.append((position[0]-2, position[1]-1))
        if j < 7 and not board[position[0]-2][position[1]+1].islower():
            tmpBoard = switchPos((position[0], position[1]), (position[0]-2, position[1]+1), tmpBoard)
            if not isKingChecked(tmpBoard, 1):
                validMoves.append((position[0]-2, position[1]+1))
    if i > 0:
        if j > 1 and not board[position[0]-1][position[1]-2].islower():
            tmpBoard = switchPos((position[0], position[1]), (position[0]-1, position[1]-2), tmpBoard)
            if not isKingChecked(tmpBoard, 1):
                validMoves.append((position[0]-1, position[1]-2))
        if j < 6 and not board[position[0]-1][position[1]+2].islower():
            tmpBoard = switchPos((position[0], position[1]), (position[0]-1, position[1]+2), tmpBoard)
            if not isKingChecked(tmpBoard, 1):
                validMoves.append((position[0]-1, position[1]+2))
    if i < 5:
        if j > 0 and not board[position[0]+2][position[1]-1].islower():
            tmpBoard = switchPos((position[0], position[1]), (position[0]+2, position[1]-1), tmpBoard)
            if not isKingChecked(tmpBoard, 1):
                validMoves.append((position[0]+2, position[1]-1))
        if j < 7 and not board[position[0]+2][position[1]+1].islower():
            tmpBoard = switchPos((position[0], position[1]), (position[0]+2, position[1]+1), tmpBoard)
            if not isKingChecked(tmpBoard, 1):
                validMoves.append((position[0]+2, position[1]+1))
    if i < 6:
        if j > 1 and not board[position[0]+1][position[1]-2].islower():
            tmpBoard = switchPos((position[0], position[1]), (position[0]+1, position[1]-2), tmpBoard)
            if not isKingChecked(tmpBoard, 1):
                validMoves.append((position[0]+1, position[1]-2))
        if j < 6 and not board[position[0]+1][position[1]+2].islower():
            tmpBoard = switchPos((position[0], position[1]), (position[0]+1, position[1]+2), tmpBoard)
            if not isKingChecked(tmpBoard, 1):
                validMoves.append((position[0]+1, position[1]+2))

    return validMoves

def getWR(position, tmpBoard):
    validMoves = []
    i,j = position[0], position[1]
    for k in range (i-1, -1, -1):
        if not board[k][j].islower():
            break
        tmpBoard = switchPos((position[0], position[1]), (k, position[1]), tmpBoard)
        if not isKingChecked(tmpBoard, 0):
            validMoves.append((k, position[1]))
        if board[k][j].islower():
            break
    
    for k in range (i+1, 8):
        if not board[k][j].islower():
            break
        tmpBoard = switchPos((position[0], position[1]), (k, position[1]), tmpBoard)
        if not isKingChecked(tmpBoard, 0):
            validMoves.append((k, position[1]))
        if board[k][j].islower():
            break

    for k in range (j-1, -1, -1):
        if not board[i][k].islower():
            break
        tmpBoard = switchPos((position[0], position[1]), (position[0], k), tmpBoard)
        if not isKingChecked(tmpBoard, 0):
            validMoves.append((position[0], k))
        if board[i][k].islower():
            break
    
    for k in range (j+1, 8):
        if not board[i][k].islower():
            break
        tmpBoard = switchPos((position[0], position[1]), (position[0], k), tmpBoard)
        if not isKingChecked(tmpBoard, 0):
            validMoves.append((position[0], k))
        if board[i][k].islower():
            break

    return validMoves

def getBR(position, tmpBoard):
    validMoves = []
    i,j = position[0], position[1]
    for k in range (i-1, -1, -1):
        if board[k][j].islower() and not board[k][j].isdigit():
            break
        tmpBoard = switchPos((position[0], position[1]), (k, position[1]), tmpBoard)
        if not isKingChecked(tmpBoard, 1):
            validMoves.append((k, position[1]))
        if board[k][j].islower():
            break
    
    for k in range (i+1, 8):
        if board[k][j].islower() and not board[k][j].isdigit():
            break
        tmpBoard = switchPos((position[0], position[1]), (k, position[1]), tmpBoard)
        if not isKingChecked(tmpBoard, 1):
            validMoves.append((k, position[1]))
        if board[k][j].islower():
            break

    for k in range (j-1, -1, -1):
        if board[i][k].islower() and not board[i][k].isdigit():
            break
        tmpBoard = switchPos((position[0], position[1]), (position[0], k), tmpBoard)
        if not isKingChecked(tmpBoard, 1):
            validMoves.append((position[0], k))
        if board[i][k].islower():
            break
    
    for k in range (j+1, 8):
        if board[i][k].islower() and not board[i][k].isdigit():
            break
        tmpBoard = switchPos((position[0], position[1]), (position[0], k), tmpBoard)
        if not isKingChecked(tmpBoard, 1):
            validMoves.append((position[0], k))
        if board[i][k].islower():
            break
    return validMoves

def getWQ(position, tmpBoard):
    validMoves = []
    validMoves.append(getWB(position, tmpBoard))
    validMoves.append(getWR(position, tmpBoard))
    return validMoves

def getBQ(position, tmpBoard):
    validMoves = []
    validMoves.append(getBB(position, tmpBoard))
    validMoves.append(getBR(position, tmpBoard))
    return validMoves

def getWK(position, tmpBoard):
    validMoves = []

    if position[0] > 0:
        if board[position[0]-1][position[1]].islower() and not board[position[0]-1][position[1]].isdigit():
            tmpBoard = switchPos((position[0], position[1]), (position[0]-1, position[1]), tmpBoard)
            if not isKingChecked(tmpBoard, 0):
                validMoves.append((position[0]-1, position[1]))    
        if position[1] > 0 and board[position[0]-1][position[1]-1].islower() and not board[position[0]-1][position[1]-1].isdigit():
            tmpBoard = switchPos((position[0], position[1]), (position[0]-1, position[1]-1), tmpBoard)
            if not isKingChecked(tmpBoard, 0):
                validMoves.append((position[0]-1, position[1]-1))           
        if position[1] < 7 and board[position[0]-1][position[1]+1].islower() and not board[position[0]-1][position[1]+1].isdigit():
            tmpBoard = switchPos((position[0], position[1]), (position[0]-1, position[1]+1), tmpBoard)
            if not isKingChecked(tmpBoard, 0):
                validMoves.append((position[0]-1, position[1]+1))  

    if position[0] < 7:
        if board[position[0]+1][position[1]].islower() and not board[position[0]+1][position[1]].isdigit():
            tmpBoard = switchPos((position[0], position[1]), (position[0]+1, position[1]), tmpBoard)
            if not isKingChecked(tmpBoard, 0):
                validMoves.append((position[0]+1, position[1]))   
        if position[1] > 0 and board[position[0]+1][position[1]-1].islower() and not board[position[0]-1][position[1]-1].isdigit():
            tmpBoard = switchPos((position[0], position[1]), (position[0]-1, position[1]-1), tmpBoard)
            if not isKingChecked(tmpBoard, 0):
                validMoves.append((position[0]+1, position[1]-1))           
        if position[1] < 7 and board[position[0]+1][position[1]+1].islower() and not board[position[0]-1][position[1]+1].isdigit():
            tmpBoard = switchPos((position[0], position[1]), (position[0]-1, position[1]+1), tmpBoard)
            if not isKingChecked(tmpBoard, 0):
                validMoves.append((position[0]+1, position[1]+1))  

    if position[1] > 0:
        if board[position[0]][position[1]-1].islower() and not board[position[0]][position[1]-1].isdigit():
            tmpBoard = switchPos((position[0], position[1]), (position[0], position[1]-1), tmpBoard)
            if not isKingChecked(tmpBoard, 0):
                validMoves.append((position[0], position[1]-1))            
    if position[1] < 7:
        if board[position[0]][position[1]+1].islower() and not board[position[0]][position[1]+1].isdigit():
            tmpBoard = switchPos((position[0], position[1]), (position[0], position[1]+1), tmpBoard)
            if not isKingChecked(tmpBoard, 0):
                validMoves.append((position[0], position[1]+1))    
    if wCastleL:
        validMoves.append(1, -1)
    if wCastleR:
        validMoves.append(-1, 1)
    return validMoves

def getBK(position, tmpBoard):
    validMoves = []

    if position[0] > 0:
        if board[position[0]-1][position[1]].islower() and not board[position[0]-1][position[1]].isdigit():
            tmpBoard = switchPos((position[0], position[1]), (position[0]-1, position[1]), tmpBoard)
            if not isKingChecked(tmpBoard, 1):
                validMoves.append((position[0]-1, position[1]))    
        if position[1] > 0 and board[position[0]-1][position[1]-1].islower() and not board[position[0]-1][position[1]-1].isdigit():
            tmpBoard = switchPos((position[0], position[1]), (position[0]-1, position[1]-1), tmpBoard)
            if not isKingChecked(tmpBoard, 1):
                validMoves.append((position[0]-1, position[1]-1))           
        if position[1] < 7 and board[position[0]-1][position[1]+1].islower() and not board[position[0]-1][position[1]+1].isdigit():
            tmpBoard = switchPos((position[0], position[1]), (position[0]-1, position[1]+1), tmpBoard)
            if not isKingChecked(tmpBoard, 1):
                validMoves.append((position[0]-1, position[1]+1))  

    if position[0] < 7:
        if board[position[0]+1][position[1]].islower() and not board[position[0]+1][position[1]].isdigit():
            tmpBoard = switchPos((position[0], position[1]), (position[0]+1, position[1]), tmpBoard)
            if not isKingChecked(tmpBoard, 1):
                validMoves.append((position[0]+1, position[1]))   
        if position[1] > 0 and board[position[0]+1][position[1]-1].islower() and not board[position[0]-1][position[1]-1].isdigit():
            tmpBoard = switchPos((position[0], position[1]), (position[0]-1, position[1]-1), tmpBoard)
            if not isKingChecked(tmpBoard, 1):
                validMoves.append((position[0]+1, position[1]-1))           
        if position[1] < 7 and board[position[0]+1][position[1]+1].islower() and not board[position[0]-1][position[1]+1].isdigit():
            tmpBoard = switchPos((position[0], position[1]), (position[0]-1, position[1]+1), tmpBoard)
            if not isKingChecked(tmpBoard, 1):
                validMoves.append((position[0]+1, position[1]+1))  

    if position[1] > 0:
        if board[position[0]][position[1]-1].islower() and not board[position[0]][position[1]-1].isdigit():
            tmpBoard = switchPos((position[0], position[1]), (position[0], position[1]-1), tmpBoard)
            if not isKingChecked(tmpBoard, 1):
                validMoves.append((position[0], position[1]-1))            
    if position[1] < 7:
        if board[position[0]][position[1]+1].islower() and not board[position[0]][position[1]+1].isdigit():
            tmpBoard = switchPos((position[0], position[1]), (position[0], position[1]+1), tmpBoard)
            if not isKingChecked(tmpBoard, 1):
                validMoves.append((position[0], position[1]+1))    
    if bCastleL:
        validMoves.append(1, -1)
    if bCastleR:
        validMoves.append(-1, 1)
    return validMoves

def getMoves(position, tmpBoard):
    tmp = tmpBoard[position[0]][position[1]]
    if tmp == 'p':
        return getBP(position, tmpBoard)
    elif tmp == 'P':
        return getWP(position, tmpBoard)
    elif tmp == 'n':
        return getBN(position, tmpBoard)
    elif tmp == 'N':
        return getWN(position, tmpBoard)
    elif tmp == 'b':
        return getBB(position, tmpBoard)
    elif tmp == 'B':
        return getWB(position, tmpBoard)
    elif tmp == 'r':
        return getBR(position, tmpBoard)
    elif tmp == 'R':
        return getWR(position, tmpBoard)
    elif tmp == 'q':
        return getBQ(position, tmpBoard)
    elif tmp == 'Q':
        return getWQ(position, tmpBoard)
    elif tmp == 'k':
        return getBK(position, tmpBoard)
    elif tmp == 'K':
        return getWK(position, tmpBoard)
    return
