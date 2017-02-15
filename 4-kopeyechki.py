# http://acmp.ru/asp/do/index.asp?main=task&id_problem=11
import sys

items = open('INPUT.txt').read().splitlines()
i1 = items.count('1')
i2 = items.count('0')


def rotateKops(i1, i2):
    if i1 > i2:
        print (i2)

    if i1 < i2:
        print (i1)

    if i1 == i2:
        print (i2)

rotateKops(i1, i2)
