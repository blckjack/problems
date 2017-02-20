#https://acmp.ru/asp/do/index.asp?main=task&id_course=1&id_section=5&id_topic=113&id_problem=695
f_in = open("INPUT.txt")
N = [int(s) for s in f_in.readline().strip().split()]
AA = [int(s) for s in f_in.readline().strip().split()]
AA = AA + [AA[0]] + [AA[1]]

i = 1
max_berry = 0
while i <= (len(AA) - 2):
    berry = AA[i] + AA[i+1] + AA[i-1]
    if berry > max_berry:
        max_berry = berry
    i += 1

print(max_berry)


