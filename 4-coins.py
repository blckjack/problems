# http://acmp.ru/asp/do/index.asp?main=topic&id_course=2&id_section=10&id_topic=3
import sys
f_in = open("INPUT.txt")
N = [int(s) for s in f_in.readline().strip().split()]
AA = [int(s) for s in f_in.readline().strip().split()]

i = 0
i1 = 0
i2 = 0
while i < N[0]:
    if AA[i] == 1:
        i1 += 1
    else:
        i2 += 1
    i += 1


def rotateKops(i1, i2):
    if i1 > i2:
        print (i2)

    if i1 < i2:
        print (i1)

    if i1 == i2:
        print (i2)

rotateKops(i1, i2)
