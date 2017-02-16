# http://acmp.ru/asp/do/index.asp?main=task&id_course=2&id_section=10&id_topic=3&id_problem=13
f_in = open("INPUT.txt")
N = [s for s in f_in.readline().strip().split()]
S = list(N[0])

i = 0
count = 0
C = 0
while i != len(S):
    if S[i] == '0':
        count += 1
        if C < count:
            C = count
    if S[i] == '1':
        if C < count:
            C = count
        count = 0
    i += 1

print (C)


# wrong answer when last symbols is 0

