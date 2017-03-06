# http://acmp.ru/asp/do/index.asp?main=task&id_course=1&id_section=7&id_topic=119&id_problem=735
f_in = open("INPUT.txt")
n = int(f_in.readline().strip())
temperatues = [int(s) for s in f_in.readline().strip().split()]
count = []
sorted_temperatues = []

# build an empty array
k = 0
while k < 201:
    count.append(0)
    k += 1

# fill in empty array with counts of integers
i = 0
while i < n:
    if temperatues[i] > 0:
        temperatue = 100
        while temperatue < 201:
            if temperatues[i] == temperatue - 100:
                count[temperatue] += 1
            temperatue += 1
    if temperatues[i] < 0:
        temperatue = 0
        while temperatue < 101:
            if temperatues[i] == 0 - temperatue:
                count[100 - temperatue] += 1
            temperatue += 1
    if temperatues[i] == 0:
        count[100] += 1
    i += 1

# sort array "temperatues"
i = 0
while i < 201:
    while count[i] != 0:
        sorted_temperatues.append(i - 100)
        count[i] -= 1
    i += 1

print(" ".join(map(str, sorted_temperatues)))