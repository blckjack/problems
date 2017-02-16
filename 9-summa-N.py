# http://acmp.ru/asp/do/index.asp?main=task&id_course=2&id_section=10&id_topic=3&id_problem=15
f_in = open("INPUT.txt")
i = int(f_in.readline())
# summa = i
# while i != 0:
#     i -= 1
#     summa += i
# print(summa)

if i > 0:
    print(((1+i) * i//2))
if i < 0:
    print(((-i+1) * i)//2+1)
if i == 0:
    print(1)
