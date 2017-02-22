# http://acmp.ru/asp/do/index.asp?main=task&id_course=2&id_section=10&id_topic=3&id_problem=14
f_in = open("INPUT.txt")
sp = [int(s) for s in f_in.readline().strip().split()]

S = sp[0]
P = sp[1]
x = 1
y = S//2
while x < S//2:
    while y < S:
        if P == x * y and S == x + y:
            if x > y:
                print(y, x)
                break
            if x <= y:
                print(x, y)
                break
        print(x,y)
    x += 1

# while y <= 1000:
#     if P == y * (S - y):
#         x = int(P/y)
#         if S == x + y:
#             if x > y:
#                 print(y, x)
#                 break
#             if x <= y:
#                 print(x, y)
#                 break
#     y += 1
