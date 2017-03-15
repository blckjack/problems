# http://acmp.ru/asp/do/index.asp?main=task&id_course=1&id_section=7&id_topic=119&id_problem=737
f_in = open("INPUT.txt")
n = int(f_in.readline().strip())
t = [int(s) for s in f_in.readline().strip().split()]


def nearestSpots(t):
    result = sort(t)
    i = 0
    k = 1
    minimum = 1000000000
    while k < len(t):
        difference = abs(result[k] - result[i])
        if difference < minimum:
            minimum = difference
            j = 0
            while j < len(t):
                if t[j] == result[i]:
                    minimum_i = j + 1
                if t[j] == result[k]:
                    minimum_k = j + 1
                j += 1
        k += 1
        i += 1
    print(minimum)
    print(minimum_i, minimum_k)


def sort(t):
    if len(t) < 2:
        return t
    mid = len(t) // 2
    return merge(sort(t[:mid]), sort(t[mid:]))


def merge(t1, t2):
    result = []
    i = 0
    j = i
    while i < len(t1) and j < len(t2):
        if t1[i] < t2[j]:
            result.append(t1[i])
            i += 1
        else:
            result.append(t2[j])
            j += 1
    result += t1[i:]
    result += t2[j:]
    return result

nearestSpots(t)
