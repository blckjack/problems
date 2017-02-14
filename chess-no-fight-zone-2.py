Q = (4, 1)
T = (4, 3)
K = (5, 5)

def countNoFightZone():
    N = 0
    x = 1
    while x < 9:
        y = 1
        while y < 9:
            target = (x, y)
            if checkKnight(K, target) or checkQueen(Q, target) or checkTower(T, target):
                N += 1
            y = y + 1
        x = x + 1
    print N


def checkQueen(Q, target):
    if checkBishop(Q, target) == True or checkTower(Q, target) == True:
        return True
    else:
        return False

def checkTower(T, target):
    x = T[0]
    y = T[1]

    while y < 8:
        y += 1
        if (x, y) == target:
            return True
    x = T[0]
    y = T[1]
    while x < 8:
        x += 1
        if (x, y) == target:
            return True
    x = T[0]
    y = T[1]
    while 1 < y:
        y -= 1
        if (x, y) == target:
            return True
    x = T[0]
    y = T[1]
    while 1 < x:
        x -= 1
        if (x, y) == target:
            return True

def checkBishop(B, target):

    x = B[0]
    y = B[1]
    while y < 8 and x < 8:
        y += 1
        x += 1
        if (x, y) == target:
            return True

    x = B[0]
    y = B[1]
    while y < 8 and 0 < x:
        y += 1
        x -= 1
        if (x, y) == target:
            return True

    x = B[0]
    y = B[1]
    while 0 < y and x < 8:
        y -= 1
        x += 1
        if (x, y) == target:
            return True

    x = B[0]
    y = B[1]
    while 0 < y and 0 < x:
        y -= 1
        x -= 1
        if (x, y) == target:
            return True

def checkKnight(K, target):
    x = K[0]
    y = K[1]
    
    if (x+2, y+1) == target:
        return True

    if (x+1, y+2) == target:
        return True

    if (x+1, y-2) == target:
        return True

    if (x+2, y-1) == target:
        return True

    if (x-2, y+1) == target:
        return True

    if (x-1, y+2) == target:
        return True

    if (x-1, y-2) == target:
        return True

    if (x-2, y-1) == target:
        return True
    return False

countNoFightZone()
