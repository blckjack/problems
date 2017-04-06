# http://acmp.ru/asp/do/index.asp?main=task&id_course=1&id_section=9&id_topic=123&id_problem=765
f_in = open("INPUT.txt")
m = []
s = []
n = [str(s) for s in f_in.readline().strip().split()]
for i in n[0]:
    m.append(i)


def main():
    i = 0
    while i < len(m)-1:
        tmp = m[i]
        m[i] = m[i+1]
        m[i+1] = tmp
        s.append("".join(map(str, m)))
        i += 1
    if s[-1] != n[0]:
        main()

main()
for i in s:
    print(i)

