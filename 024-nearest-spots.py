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
    i = 0
    while i < len(t):
        if t[i] == ri:
            minimum_i = i + 1
        if t[i] == rk:
            minimum_k = i + 1
        i += 1

    print(d)
    if ri > rk:
        print(minimum_k, minimum_i)
    if rk > ri:
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
