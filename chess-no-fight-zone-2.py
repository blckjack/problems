#deck = [[0 for x in range(8)] for y in range(8)]



Q = (1, 3)
T = (2, 4)
K = (1, 6)

def countNoFightZone():
    N = 0
    x = 1
    while x < 9:
        y = 1
        while y < 9:
            cc = (x, y)
            if not checkQueen(cc):
                N = N + 1
            y = y + 1
        x = x + 1
    print N


def checkQueen(cc):
    rule = []
    while ***:
        rule.append[()]
    if cc in rule: 
        return True

def checkTower(cc):
    """
    check that tower can reach b from a
    return T or F
    """
    pass

def checkKnight(cc):
    pass

countNoFightZone()