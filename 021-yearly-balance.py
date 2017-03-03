# http://acmp.ru/asp/do/index.asp?main=task&id_course=1&id_section=7&id_topic=118&id_problem=732
f_in = open("INPUT.txt")
a = [int(s) for s in f_in.readline().strip().split()]
b = [int(s) for s in f_in.readline().strip().split()]


def modify_array(v):
    negative = 0
    v = [s for s in str(v[0])]
    if v[0] == '-':
        v.remove(v[0])
        negative += 1
    return v


def increase_value(v):
    i = 0
    negative = 0
    v = modify_array(v)
    while i < len(v):
        k = i
        maximum = -1000000000
        while k < len(v):
            if int(v[k]) > maximum:
                maximum = int(v[k])
                maximum_index = k
            k += 1
        tmp = int(v[i])
        v[i] = maximum
        v[maximum_index] = tmp
        i += 1
    v = "".join(str(x) for x in v)
    if negative == 1:
        v = v * -1
    return int(v)


def decrease_value(v):
    i = 0
    negative = 0
    modify_array(v)
    while i < len(v):
        k = i
        minimum = 1000000000
        while k < len(v):
            if int(v[k]) < minimum:
                minimum = int(v[k])
                minimum_index = k
            k += 1
        tmp = int(v[i])
        v[i] = minimum
        v[minimum_index] = tmp
        i += 1
    v = "".join(str(x) for x in v)
    if negative == 1:
        v = v * -1
    return int(v)

if a[0] > 0 and b[0] > 0:
    black_income = increase_value(a) - decrease_value(b)
if a[0] < 0 and b[0] < 0:
    black_income = decrease_value(a) - increase_value(b)
else:
    black_income = increase_value(a) - increase_value(b)

print(black_income)
