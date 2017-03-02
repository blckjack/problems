# http://acmp.ru/asp/do/index.asp?main=task&id_course=1&id_section=7&id_topic=118&id_problem=728
f_in = open("INPUT.txt")
N = [int(s) for s in f_in.readline().strip().split()]
AA = []
i = 0
while i < N[0]:
    AA.append([int(s) for s in f_in.readline().strip().split()])
    i += 1


# other solution, if we couldn't compare lists easily:
def ordered(a, b):
    if a[0] < b[0]:
        return True
    if a[0] > b[0]:
        return False
    if a[0] == b[0]:
        if a[1] < b[1]:
            return True
        if a[1] > b[1]:
            return False
        if a[1] == b[1]:
            if a[2] < b[2]:
                return True
            if a[2] > b[2]:
                return False
            if a[2] == b[2]:
                return True

i = 0
while i < N[0]:
    minimum = [24, 00, 00]
    k = i
    minimum_index = k
    while k < N[0]:
        if not ordered(AA[i], AA[k]):
            minimum = AA[k]
            minimum_index = k
        k += 1
    tmp = AA[i]
    AA[i] = minimum
    AA[minimum_index] = tmp
    i += 1

# i = 0
# while i < N[0]:
#     k = i
#     minimum = [24, 00, 00]
#     minimum_index = 0
#     while k < N[0]:
#         if AA[k] < minimum:
#             minimum = AA[k]
#             minimum_index = k
#         k += 1
#     tmp = AA[i]
#     AA[i] = minimum
#     AA[minimum_index] = tmp
#     i += 1

k = 0
while k < len(AA):
    print(" ".join(map(str, AA[k])))
    k += 1
