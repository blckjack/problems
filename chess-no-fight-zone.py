deck = [[0 for x in range(8)] for y in range(8)] 


vhRange = range(1, 8)
attackMap = []
def towerRule(x, y):
    for cell in vhRange:
        if x + 1 < 9:
            attackMap.append("*")
        if y + 1 < 9:
            attackMap.append("*")
def queenRule(x, y):
    for cell in vhRange:
        if x + 1 < 9:
            attackMap.append("*")
        if y + 1 < 9:
            attackMap.append("*")
        

def knightRule(x, y):
    knightMap = []

towerRule(3, 2)
print attackMap
