# http://acmp.ru/asp/do/index.asp?main=task&id_course=1&id_section=8&id_topic=121&id_problem=753
import pprint
f_in = open("INPUT.txt")
n = [int(s) for s in f_in.readline().strip().split()]
N, M, T = n[0]+2, n[1]+2, n[2]+1
worldMap = [[0 for x in range(M)] for y in range(N)]
universeMap = worldMap[:]
# N, M, T = 5, 5, 5


def readInitialInput():  # works perfectly
    i = 1
    while i < N - 1:
        c = [str(s) for s in f_in.readline().strip()]
        k = 1
        while k < M - 1:
            worldMap[i][k] = c[k-1]
            k += 1
        i += 1
    return worldMap
readInitialInput()


def extendMap(a):  # works ok
    i = 0
    while i < N:
        k = 0
        while k < M:
            if k == M - 1:
                a[i][k] = a[i][1]
                a[i][0] = a[i][M-2]
            k += 1
        if i == N - 1:
            a[i] = a[1][:]
            a[0] = a[N-2][:]
        i += 1


def countCells(i, k):  # works perfectly
    count = 0
    if worldMap[i+1][k+1] == '*':
        count += 1
    if worldMap[i+1][k-1] == '*':
        count += 1
    if worldMap[i-1][k-1] == '*':
        count += 1
    if worldMap[i-1][k+1] == '*':
        count += 1
    if worldMap[i][k+1] == '*':
        count += 1
    if worldMap[i+1][k] == '*':
        count += 1
    if worldMap[i][k-1] == '*':
        count += 1
    if worldMap[i-1][k] == '*':
        count += 1
    return count


def rewriteCells(a):
    extendMap(a)
    i = 1
    while i < N - 1:
        k = 1
        while k < M - 1:
            c = countCells(i, k)
            if a[i][k] == '*':
                if c == 2 or c == 3:
                    universeMap[i][k] = '*'
                else:
                    universeMap[i][k] = '.'
            else:
                if c == 3:
                    universeMap[i][k] = '*'
                else:
                    universeMap[i][k] = '.'
            k += 1
        i += 1
    pprint.pprint(universeMap)

j = 1
while j < T:
    rewriteCells(worldMap)
    j += 1
