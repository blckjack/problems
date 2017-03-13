# http://acmp.ru/asp/do/index.asp?main=task&id_course=1&id_section=7&id_topic=119&id_problem=737
f_in = open("INPUT.txt")
n = int(f_in.readline().strip())
t = [int(s) for s in f_in.readline().strip().split()]


# TODOTHISUGLYCODEBELOW :(
def nearestSpots(t):
    result = sort(t)
    i = len(result) - 1
    k = i - 1
    minimum = 10000000000
    while 0 < i:
        d = result[i] - result[k]
        if d <= minimum:
            minimum = d
            ri = result[i]
            rk = result[k]
        k -= 1
        i -= 1

    print(d)


def sort(t):
    if len(t) < 2:
        return t
    mid = len(t) // 2
    return merge(sort(t[:mid]), sort(t[mid:]))


def merge(t1, t2):
    result = []
    i = 0
    k = i
    while i < len(t1) and k < len(t2):
        if t1[i] < t2[k]:
            result.append(t1[i])
            i += 1
        else:
            result.append(t2[k])
            k += 1
    result += t1[i:]
    result += t2[k:]
    return result

nearestSpots(t)
