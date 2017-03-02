# http://acmp.ru/asp/do/index.asp?main=task&id_course=1&id_section=7&id_topic=118&id_problem=728
f_in = open("INPUT.txt")
N = [int(s) for s in f_in.readline().strip().split()]
AA = []
i = 0
while i < N[0]:
    AA.append([int(s) for s in f_in.readline().strip().split()])
    i += 1


# they solution, if we couldn't compare lists easily:
def ordered(a, b):
    if len(a) == len(b):
        i = 0
        while i < len(a):
            if a > b:
                return False
            i += 1
    return True

i = 0
while i < N[0]:
    k = i
    minimum = [24, 00, 00]
    while k < N[0]:
        if ordered(AA[i], AA[k]) is False:
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
