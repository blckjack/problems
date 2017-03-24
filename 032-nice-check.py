# http://acmp.ru/asp/do/index.asp?main=task&id_course=1&id_section=8&id_topic=122&id_problem=756
f_in = open("INPUT.txt")
t = [int(s) for s in f_in.readline().strip().split()]


def cute(pattern, N, M):
    i = 0
    while i < N - 1:
        k = 0
        while k < M - 1:
            if pattern[i][k] == pattern[i+1][k] and pattern[i][k] == pattern[i][k+1] and pattern[i][k] == pattern[i+1][k+1]:
                return False
                break
            k += 1
        i += 1
    return True


def result(pattern, N, M):
    if cute(pattern, N, M):
        print('YES')
    if not cute(pattern, N, M):
        print('NO')

i = 0  # outer loop
while i < t[0]:
    n = [int(s) for s in f_in.readline().strip().split()]
    k = 0
    pattern = []
    while k < n[0]:
        kk = ([int(s) for s in f_in.readline().strip().split()])
        pattern.append(kk)
        k += 1
    N = n[0]
    M = n[1]
    result(pattern, N, M)
    i += 1


