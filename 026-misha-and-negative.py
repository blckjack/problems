# http://acmp.ru/asp/do/index.asp?main=task&id_course=1&id_section=8&id_topic=121&id_problem=749
f_in = open("INPUT.txt")
n = [int(s) for s in f_in.readline().strip().split()]

# create an array of cells before state
i = 0
before = []
while i < n[0]:
    a = [str(s) for s in f_in.readline().strip().split()]
    before.append(a)
    i += 1


a_before = []
for i in before:
    for s in i:
        for l in s:
            a_before.append(l)

# create an array of cells after state
i = 0
after = []
while i < n[0]+1:
    b = [str(s) for s in f_in.readline().strip().split()]
    after.append(b)
    i += 1

a_after = []
for i in after:
    for s in i:
        for l in s:
            a_after.append(l)

# count Misha's errors
i = 0
count = 0
while i < len(a_after):
    if a_before[i] == a_after[i]:
        count += 1
    i += 1

print(count)

