#http://acmp.ru/asp/do/index.asp?main=task&id_problem=726
f_in = open("INPUT.txt")
N = [int(s) for s in f_in.readline().strip().split()]
AA = [int(s) for s in f_in.readline().strip().split()]

i = 0
while i < len(AA) - 1:
    if AA[i] > AA[i+1]:
        p = AA[i+1]
        AA[i+1] = AA[i]
        AA[i] = p
        i = -1
    i += 1

print(" ".join(map(str, AA)))
