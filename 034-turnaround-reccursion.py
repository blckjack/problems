# http://acmp.ru/asp/do/index.asp?main=task&id_course=2&id_section=10&id_topic=4&id_problem=16
f_in = open("INPUT.txt")
N = int(f_in.readline().strip())
a = [int(s) for s in f_in.readline().strip().split()]

i = 0
j = 1


def turnaround(i, j):
    while i < N//2:
        if i != N-j:
            tmp = a[i]
            a[i] = a[N-j]
            a[N-j] = tmp
            i += 1
            j += 1
            return turnaround(i, j)

turnaround(i, j)
print(" ".join(map(str, a)))

