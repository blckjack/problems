# http://acmp.ru/asp/do/index.asp?main=task&id_course=1&id_section=7&id_topic=119&id_problem=735
f_in = open("INPUT.txt")
n = int(f_in.readline().strip())
temperatures = [int(s) for s in f_in.readline().strip().split()]
sorted_temperatures = [0]*len(temperatures)
count = [0]*201

i = 0
while i < n:
    # { i }
    ti = temperatures[i]
    if -101 < ti and ti < 101:
        if ti > 0:
            count[100 + ti] += 1
        if ti < 0:
            count[100 + ti] += 1  # -
        if ti == 0:
            count[100] += 1
    i += 1

i = 0
k = i
while i < len(count):
    while count[i] != 0:
        sorted_temperatures[k] = (i - 100)
        count[i] -= 1
        k += 1
    i += 1

print(" ".join(map(str, sorted_temperatures)))
