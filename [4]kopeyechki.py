#http://acmp.ru/asp/do/index.asp?main=task&id_problem=11
import sys

items = sys.stdin.readline().strip().split()
i1 = items.count('1')
i2 = items.count('0')

def rotateKops(i1, i2):
    if i1 > i2:
        print (i2)

    if i1 < i2:
        print (i1)

rotateKops(i1, i2)