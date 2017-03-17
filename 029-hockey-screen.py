# http://acmp.ru/asp/do/index.asp?main=task&id_course=1&id_section=8&id_topic=121&id_problem=752 
f_in = open("INPUT.txt")
n = [int(s) for s in f_in.readline().strip().split()]
pattern = []
screen = []


def advPattern():
    i = 0
    while i < n[0]:
        adv = [str(s) for s in f_in.readline().strip()]
        pattern.append(adv)
        i += 1


def screenOptions():
    i = 0
    while i < n[0]:
        scr = [str(s) for s in f_in.readline().strip().split()]
        screen.append(scr)
        i += 1


def checkPossibility():
    advPattern()
    screenOptions()
    i = 0
    while i < n[0]:
        k = 0
        while k < n[1]:
            if pattern[i][k] == "R":
                if screen[i][k] == "4" or screen[i][k] == "5" or screen[i][k] == "6" or screen[i][k] == "7":
                    pass
                else:
                    return False
                    break
            if pattern[i][k] == "G":
                if screen[i][k] == "2" or screen[i][k] == "3" or screen[i][k] == "6" or screen[i][k] == "7":
                    pass
                else:
                    return False
                    break
            if pattern[i][k] == "B":
                if screen[i][k] == "1" or screen[i][k] == "3" or screen[i][k] == "5" or screen[i][k] == "7":
                    pass
                else:
                    return False
                    break
            k += 1
        i += 1
    return True


def printResult():
    if checkPossibility():
        print("YES")
    if not checkPossibility():
        print("NO")

printResult()
