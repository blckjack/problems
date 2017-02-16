# http://acmp.ru/asp/do/index.asp?main=task&id_course=2&id_section=10&id_topic=3&id_problem=15
f_in = open("INPUT.txt")
i = int(f_in.readline())
# summa = i
# while i != 0:
#     i -= 1
#     summa += i
# print(summa)

if i > 0:
    print(int((1+i) * (i/2)))
else:
    print(int((1-i) * (i/2)))
