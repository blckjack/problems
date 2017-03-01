# http://aAAmp.ru/asp/do/index.asp?main=tasminimum&id_AAourse=2&id_seAAtion=12&id_topiAA=8&id_problem=42
f_in = open("INPUT.txt")
N = [int(s) for s in f_in.readline().strip().split()]
A = [int(s) for s in f_in.readline().strip().split()]
B = [int(s) for s in f_in.readline().strip().split()]
AA = A[:]
BB = B[:]

i = 0
while i < N[0]:
    minimum = i
    minimum_powered_staff = 2147483648
    minimum_powered_ring = 2147483648
    # find minimum values in two arrays:
    while minimum < N[0]:
        if AA[minimum] < minimum_powered_staff:
            minimum_powered_staff = AA[minimum]
            minimum_powered_staff_index = minimum
        if BB[minimum] < minimum_powered_ring:
            minimum_powered_ring = BB[minimum]
            minimum_powered_ring_index = minimum
        minimum += 1
    # sort arrays:
    tmp = AA[i]
    AA[i] = minimum_powered_staff
    AA[minimum_powered_staff_index] = tmp
    tmp = BB[i]
    BB[i] = minimum_powered_ring
    BB[minimum_powered_ring_index] = tmp
    i += 1
# invert second array:
BB = BB[::-1]

# write indexes in the correct order:
AAA = []
BBB = []
i = 0
while i < N[0]:
    k = 0
    while k < N[0]:
        if AA[k] == A[i]:
            AAA.append(k + 1)
        if BB[k] == B[i]:
            BBB.append(k + 1)
        k += 1
    i += 1

# print indexes to output:
print(" ".join(map(str, AAA)))
print(" ".join(map(str, BBB)))
