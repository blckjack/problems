# http://acmp.ru/asp/do/index.asp?main=task&id_course=1&id_section=7&id_topic=118&id_problem=729
f_in = open("INPUT.txt")
n = int(f_in.readline().strip())
A = [int(s) for s in f_in.readline().strip().split()]

i = 0
while i < n:
    k = i
    minimum = 30000
    while k < n:
        if A[k] < minimum:
            minimum = A[k]
            minimum_index = k
        k += 1
    tmp = A[i]
    A[i] = minimum
    A[minimum_index] = tmp
    i += 1

i = 0
count = 0
control_group = n//2 + 1
while i < control_group:
        control_people = A[i]//2 + 1
        count = count + control_people
        i += 1

print(count)
