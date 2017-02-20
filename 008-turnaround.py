# http://acmp.ru/asp/do/index.asp?main=task&id_course=2&id_section=10&id_topic=4&id_problem=16
f_in = open("INPUT.txt")
N = [int(s) for s in f_in.readline().strip().split()]
AA = [int(s) for s in f_in.readline().strip().split()]

AAA = []
i = N[0] - 1
while i > -1:
    AAA.append(str(AA[i]))
    i -= 1
print(' '.join(AAA))
