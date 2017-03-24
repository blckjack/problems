# http://acmp.ru/asp/do/index.asp?main=task&id_course=1&id_section=8&id_topic=121&id_problem=753
from copy import deepcopy
f_in = open("INPUT.txt")
n = [int(s) for s in f_in.readline().strip().split()]
N, M, T = n[0], n[1], n[2]
worldMap = [[0 for x in range(M)] for y in range(N)]
universeMap = [[0 for x in range(M)] for y in range(N)]


def readInitialInput(field):
    i = 0
    while i < N:
        c = [str(s) for s in f_in.readline().strip()]
        field[i] = c[:]
        i += 1
    return field


def findNeighbors(field, x, y):
    count = 0
    if 0 < y < M - 1:
        yi = (0, -1, 1)
    elif y > 0:
        yi = (0, -1, -y)
    else:
        yi = (0, 1, M - 1)
    xi = (0, -1, 1) if 0 < x < N - 1 else ((0, -1, -x) if x > 0 else (0, 1, N - 1))
    for a in xi:
        for b in yi:
            if a == b == 0:
                continue
            else:
                if field[x + a][y + b] == '*':
                    count += 1
    return count


def goThroughMap(field):
    i = 0
    while i < N:
        k = 0
        while k < M:
            r = findNeighbors(field, i, k)
            if field[i][k] == '*':
                if r < 2 or 3 < r:
                    universeMap[i][k] = '.'
                else:
                    universeMap[i][k] = '*'
            else:
                if r == 3:
                    universeMap[i][k] = '*'
                else:
                    universeMap[i][k] = '.'
            k += 1
        i += 1


def newGeneration(field):
    readInitialInput(field)
    i = 0
    while i < T:
        goThroughMap(field)
        field = deepcopy(universeMap)
        i += 1
    return field


def printResult(field):
    newGeneration(field)
    i = 0
    while i < N:
        print("".join(map(str, universeMap[i])))
        i += 1

printResult(worldMap)
