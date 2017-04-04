# http://acmp.ru/asp/do/index.asp?main=task&id_course=1&id_section=8&id_topic=122&id_problem=757
f_in = open("INPUT.txt")
n = [int(s) for s in f_in.readline().strip().split()]
N = n[0]
M = n[1]
result = []

i = 0
while i < N:
    n = [int(s) for s in f_in.readline().strip().split()]
    result.append(n)
    i += 1


def main():
    count = 0
    i = 0
    while i < N:
        k = 0
        while k < M:
            if find_minimal_value(i) == find_maximum_value(k):
                count += 1
            k += 1
        i += 1
    print(count)


def find_minimal_value(i):
    k = 0
    j = 0
    while k < M:
        while j < M:
            if result[i][k] > result[i][j]:
                tmp = result[i][j]
                result[i][j] = result[i][k]
                result[i][k] = tmp
            j += 1
        k += 1
        k = j
    return result[i][0]


def find_maximum_value(k):
    i = 0
    j = 0
    while i < M:
        while j < M:
            if result[i][k] > result[j][k]:
                tmp = result[j][k]
                result[j][k] = result[i][k]
                result[i][k] = tmp
            j += 1
        i += 1
        i = j
    return result[-1][k]


main()
