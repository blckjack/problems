Q = (4, 1)
T = (4, 3)
K = (5, 5)

def countNoFightZone():
    N = 0
    x = 1
    while x < 9:
        y = 1
        while y < 9:
            cc = (x, y)
            if checkQueen(Q, cc):
                N += 1
            if checkKnight(K, cc):
                N += 1
            if checkTower(T, cc):
                N += 1
            y = y + 1
        x = x + 1
    print N


def checkQueen(Q, cc):
    if checkBishop(Q, cc) == True or checkTower(Q, cc) == True:
        return True
    else:
        return False

def checkTower(T, cc):
    x = T[0]
    y = T[1]

    while y < 8:
        y += 1
        if x == cc[0] and y == cc[1]:
            return True
    x = T[0]
    y = T[1]
    while x < 8:
        x += 1
        if x == cc[0] and y == cc[1]:
            return True
    x = T[0]
    y = T[1]
    while 1 < y:
        y -= 1
        if x == cc[0] and y == cc[1]:
            return True
    x = T[0]
    y = T[1]
    while 1 < x:
        x -= 1
        if x == cc[0] and y == cc[1]:
            return True

def checkBishop(B, cc):

    x = B[0]
    y = B[1]
    while y < 8 and x < 8:
        y += 1
        x += 1
        if x == cc[0] and y == cc[1]:
            return True

    x = B[0]
    y = B[1]
    while y < 8 and 0 < x:
        y += 1
        x -= 1
        if x == cc[0] and y == cc[1]:
            return True

    x = B[0]
    y = B[1]
    while 0 < y and x < 8:
        y -= 1
        x += 1
        if x == cc[0] and y == cc[1]:
            return True

    x = B[0]
    y = B[1]
    while 0 < y and 0 < x:
        y -= 1
        x -= 1
        if x == cc[0] and y == cc[1]:
            return True

def checkKnight(K, cc):

    x = K[0]
    y = K[1]
    if y < 8 and x < 8:
        x +=2 
        y +=1
        if x == cc[0] and y == cc[1]:
            return True
    x = K[0]
    y = K[1]
    if y < 8 and x < 8:
        x +=1 
        y +=2
        if x == cc[0] and y == cc[1]:
            return True

    x = K[0]
    y = K[1]
    if 0 < y and x < 8:
        x +=1 
        y -=2
        if x == cc[0] and y == cc[1]:
            return True

    x = K[0]
    y = K[1]
    if 0 < y and x < 8:
        x +=2 
        y -=1
        if x == cc[0] and y == cc[1]:
            return True

    x = K[0]
    y = K[1]
    if y < 8 and 0 < x:
        x -=2 
        y +=1
        if x == cc[0] and y == cc[1]:
            return True

    x = K[0]
    y = K[1]
    if y < 8 and 0 < x:
        x -=1 
        y +=2
        if x == cc[0] and y == cc[1]:
            return True

    x = K[0]
    y = K[1]
    if 0 < x and 0 < x:
        x -=1 
        y -=2
        if x == cc[0] and y == cc[1]:
            return True

    x = K[0]
    y = K[1]
    if 0 < x and 0 < x:
        x -=2 
        y -=1
        if x == cc[0] and y == cc[1]:
            return True

countNoFightZone()
