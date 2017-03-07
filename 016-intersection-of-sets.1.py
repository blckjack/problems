from random import randint

# http://acmp.ru/asp/do/index.asp?main=task&id_course=2&id_section=10&id_topic=4&id_problem=17
# f_in = open("INPUT.txt")
# n = [int(s) for s in f_in.readline().strip().split()]
# first_sequence = [int(s) for s in f_in.readline().strip().split()]
# second_sequence = [int(s) for s in f_in.readline().strip().split()]
# dump = [0]*100000
# result = []

# n = [11, 6]
# first_sequence = [2, 4, 10000, 8, 10, 12, 0, 8, 6, 4, 2]
# second_sequence = [3, 6, 9, 10000, 15, 1, 0]
#dump = [0]*100000
# result = []


def sort(A):
    permutation_found = True
    while permutation_found:
        k = 0
        permutation_found = False
        while k < len(A)-1:
            if A[k] > A[k+1]:
                A[k], A[k+1] = A[k+1], A[k]
                permutation_found = True
            k += 1


def intersect(A, B, M):
    R = []
    dump = [0]*(M+1)
    # create pattern from first_sequence
    i = 0
    while i < len(A):
        f = A[i]
        dump[f] = 1
        i += 1

    # compare pattern and second_sequence
    i = 0
    while i < len(B):
        s = B[i]
        if dump[s] == 1:
            R.append(s)
            dump[s] = 0
        i += 1

    sort(R)
    return R


def generate_test(n, m, M):
    A = [0]*n
    B = [0]*m
    i = 0
    while i < n:
        A[i] = randint(0, M)
        i += 1
    i = 0
    while i < m:
        B[i] = randint(0, M)
        i += 1
    return A, B


def test(N):
    i = 0
    M = 10
    while i < N:
        A, B = generate_test(10, 50, M)
        R1 = intersect(A, B, M)
        R2 = sorted(list(set(A).intersection(set(B))))
        if R1 != R2:
            print("A", A)
            print("B", B)
            print("R", R1)
            print("expected", R2)
        i += 1

test(20)
