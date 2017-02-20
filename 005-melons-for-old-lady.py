# http://acmp.ru/asp/do/index.asp?main=task&id_course=2&id_section=10&id_topic=3&id_problem=12
f_in = open("INPUT.txt")
N = [int(s) for s in f_in.readline().strip().split()]
AA = [int(s) for s in f_in.readline().strip().split()]


def magaz():
    i = 0
    melon_light = 30000
    melon_heavy = 1
    if AA[i] > 0:
        while i < N[0]:
            if melon_heavy < AA[i]:
                melon_heavy = AA[i]
            if melon_light > AA[i]:
                melon_light = AA[i]
            i += 1
    print(melon_light, melon_heavy)

magaz()
