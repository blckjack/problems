# http://acmp.ru/asp/do/index.asp?main=task&id_course=1&id_section=7&id_topic=119&id_problem=737
f_in = open("INPUT.txt")
n = int(f_in.readline().strip())
t = [int(s) for s in f_in.readline().strip().split()]


def nearestSpots(t):
    result = sort(t)
    i = 0
    while i < len(t):
        if t[i] == result[0]:
            k = 0
            while k < len(t):
                if t[k] == result[1]:
                    print(abs(result[1] - result[0]))
                    print(i+1, k+1)
                k += 1
        i += 1


def sort(t):
    if len(t) < 2:
        return t
    mid = len(t) // 2
    return merge(sort(t[:mid]), sort(t[mid:]))


def merge(t1, t2):
    result = []
    i = j = 0
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
