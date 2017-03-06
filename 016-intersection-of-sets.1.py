# http://acmp.ru/asp/do/index.asp?main=task&id_course=2&id_section=10&id_topic=4&id_problem=17
f_in = open("INPUT.txt")
n = [int(s) for s in f_in.readline().strip().split()]
first_sequence = [int(s) for s in f_in.readline().strip().split()]
second_sequence = [int(s) for s in f_in.readline().strip().split()]
dump = [0]*300000
result = []

# create origin from first_sequence
i = 0
while i < n[0]:
    f = first_sequence[i]
    dump[f] = 1
    i += 1

# compare origin and second_sequence
i = 0
while i < n[1]:
    s = second_sequence[i]
    if dump[s] == 1:
        result.append(s)
    i += 1

# sort result ->
i = 0
while i < len(result) - 1:
    if result[i] > result[i+1]:
        p = result[i+1]
        result[i+1] = result[i]
        result[i] = p
    i += 1

print(" ".join(map(str, result)))
