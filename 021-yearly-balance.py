# http://acmp.ru/asp/do/index.asp?main=task&id_course=1&id_section=7&id_topic=118&id_problem=732
# f_in = open("INPUT.txt")
# a = [s for s in str(f_in.readline().strip())]
# b = [s for s in str(f_in.readline().strip())]
a = ['1', '8']
b = ['-', '1', '0']

i = 0
while i < len(a):
    k = 0
    maximum = 0
    while k < len(a):
        if int(k) > maximum:
            maximum = int(a[k])
            maximum_index = k
        k += 1
    tmp = int(a[i])
    a[i] = maximum
    a[maximum_index] = tmp
    i += 1


i = 0
while i < len(b):
    k = 0
    maximum = 0
    while k < len(b):
        if int(k) > maximum:
            maximum = int(b[k])
            maximum_index = k
        k += 1
    tmp = int(b[i])
    b[i] = maximum
    b[maximum_index] = tmp
    i += 1

print(a, b)

# if a(+) b(+) a=big b=small
# -  - a=b b=s
# +  - a=b b=b
# -  + a=b b=b
