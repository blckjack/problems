# http://acmp.ru/asp/do/index.asp?main=task&id_course=1&id_section=8&id_topic=121&id_problem=750
f_in = open("INPUT.txt")
n = [int(s) for s in f_in.readline().strip().split()]
N = n[0]
M = n[1]
sea = []


def fillSea():
    i = 0
    while i < N:
        ship = [str(s) for s in f_in.readline().strip()]
        sea.append(ship)
        i += 1

ocean = [["." for k in range(M+2)] for i in range(N+2)]


def fillOcean():
    fillSea()
    i = 0
    while i < N:
        k = 0
        while k < M:
            ocean[i+1][k+1] = sea[i][k]
            k += 1
        i += 1


def countPositionToFight(f):
    fillOcean()
    count = 0
    i = 1
    while i < N+1:
        k = 1
        while k < M+1:
            if f[i][k] != "*":
                if f[i][k] == f[i+1][k] and f[i][k] == f[i-1][k]:
                    if f[i][k] == f[i][k+1] and f[i][k] == f[i][k-1]:
                        count += 1
            k += 1
        i += 1
    print(count)

countPositionToFight(ocean)
