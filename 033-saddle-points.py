# http://acmp.ru/asp/do/index.asp?main=task&id_course=1&id_section=8&id_topic=122&id_problem=757
f_in = open("INPUT.txt")
n = [int(s) for s in f_in.readline().strip().split()]
N = n[0]
M = n[1]
a = []
b = []
result = []

i = 0
while i < N:
    n = [int(s) for s in f_in.readline().strip().split()]
    result.append(n)
    i += 1


def minimumLineValue():
    i = 0
    while i < N:
        k = 0
        minimum = 10000000
        while k < M:
            if result[i][k] < minimum:
                minimum = result[i][k]
                min_i = [i, k]
            k += 1

            k = 0
            while k < N:
                i = 0
                while i < M:
                    if minimum == result[k][i]:
                        b.append([k, i])
                    i += 1
                k += 1
        i += 1
    print(b)


def maximumColumnValue():
    k = 0
    while k < M:
        i = 0
        maximum = -1
        while i < N:
            if result[i][k] > maximum:
                maximum = result[i][k]
                max_i = [i, k]
            i += 1

            i = 0
            while i < N:
                k = 0
                while k < M:
                    if maximum == result[i][k]:
                        a.append([i, k])
                    k += 1
                i += 1
        k += 1
    print(a)


def iterateThroughMap():
    minimumLineValue()
    maximumColumnValue()
    count = 0
    i = 0
    while i < len(b):
        k = 0
        while k < len(a):
            if b[i] == a[k]:
                count += 1
            k += 1
        i += 1
    print(count)

iterateThroughMap()
