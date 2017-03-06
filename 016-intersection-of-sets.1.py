# http://acmp.ru/asp/do/index.asp?main=task&id_course=2&id_section=10&id_topic=4&id_problem=17
f_in = open("INPUT.txt")
n = [int(s) for s in f_in.readline().strip().split()]
first_sequence = [int(s) for s in f_in.readline().strip().split()]
second_sequence = [int(s) for s in f_in.readline().strip().split()]
final_sequence = first_sequence + second_sequence
count = []

# create empty array
i = 0
while i < 10:
    count.append(0)
    i += 1

# merge arrays, and create a single sequence
i = 0
while i < len(second_sequence):
    first_sequence.append(second_sequence[i])
    i += 1

# find the repeated values
i = 0
while i < len(first_sequence):
    k = 0
    while k < len(first_sequence):
        if first_sequence[i] == k:
            count[k] += 1
        k += 1
    i += 1

print(first_sequence, count)
