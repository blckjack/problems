# http://acmp.ru/asp/do/index.asp?main=task&id_course=1&id_section=8&id_topic=121&id_problem=751
f_in = open("INPUT.txt")
n = [int(s) for s in f_in.readline().strip().split()]
worldMap = []


def drawMap():
    i = 0
    while i < n[0]:
        c = [str(s) for s in f_in.readline().strip()]
        worldMap.append(c)
        i += 1
    return worldMap


def countCities():
    drawMap()
    i = 0
    count = 0
    while i < len(worldMap):
        k = 0
        while k < len(worldMap[i]):
            if worldMap[i][k] == 'C':
                count += 1
            k += 1
        i += 1
    return count


def goThroughTheMap():
    count = countCities()
    semi_count = count / 2
    i = 0
    while i < len(worldMap):
        k = 0
        while k < len(worldMap[i]):
            if count > semi_count:
                if worldMap[i][k] == 'C':
                    count -= 1
                worldMap[i][k] = '1'
            else:
                worldMap[i][k] = '2'
            k += 1
        i += 1


def printResult():
    goThroughTheMap()
    for i in worldMap:
        print("".join(map(str, i)))

printResult()
