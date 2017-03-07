# http://acmp.ru/asp/do/index.asp?main=task&id_course=1&id_sect[i]on=7&id_topic=119&id_problem=735
f_in = open("INPUT.txt")
n = int(f_in.readline().strip())
t = [int(s) for s in f_in.readline().strip().split()]
sorted_t = [0]*len(t)
count = [0]*201

i = 0
while i < n:
    # { i }
    if -101 < t[i] and t[i] < 101:
        if t[i] > 0:
            count[100 + t[i]] += 1
        if t[i] < 0:
            count[100 + t[i]] += 1  # -
        if t[i] == 0:
            count[100] += 1
    i += 1

i = 0
k = i
while i < len(count):
    while count[i] != 0:
        sorted_t[k] = (i - 100)
        count[i] -= 1
        k += 1
    i += 1

print(" ".join(map(str, sorted_t)))
