#http://acmp.ru/index.asp?main=task&id_task=19
import sys

QTK = sys.stdin.readline().strip().split()

Q,T,K = map(lambda C: (ord(C[0])-ord("A")+1, int(C[1])), QTK)


def countNoFightZone():
    N = 0
    x = 1
    while x < 9:
        y = 1
        while y < 9:
            target = (x, y)
            if checkKnight(K, target) or checkQueen(Q, target) or checkTower(T, target):
                if Q != target and T != target and K != target:
                    N += 1
            y = y + 1
        x = x + 1
    print (N)


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
    places = [(1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1)]
    for place in places:
        if (x + place[0], y + place[1]) == target:
            return True
    return False

countNoFightZone()
