# http://acmp.ru/asp/do/index.asp?main=task&id_course=1&id_section=7&id_topic=119&id_problem=738
f_in = open("INPUT.txt")
n = int(f_in.readline().strip())
a = [int(s) for s in f_in.readline().strip().split()]


i = 0
dump = [0]*1000000
while i < len(a):
    f = a[i]
    dump[f] += 1
    i += 1

i = 0
maximum_sequence = 0
maximum_value = 0
while i < len(dump):
    if dump[i] > maximum_sequence:
        maximum_sequence = dump[i]
        maximum_value = i
    i += 1

i = 0
j = 0
k = len(a) - 1
final = [0]*len(a)
while i < len(a):
    if a[i] == maximum_value:
        final[k] = a[i]
        k -= 1
    if a[i] != maximum_value:
        final[j] = a[i]
        j += 1
    i += 1

print(" ".join(map(str, final)))
