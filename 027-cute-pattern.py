# http://acmp.ru/asp/do/index.asp?main=task&id_course=1&id_section=8&id_topic=121&id_problem=748
f_in = open("INPUT.txt")
pattern = []

i = 0
while i < 4:
    n = [str(s) for s in f_in.readline().strip()]
    pattern.append(n)
    i += 1


def cute(pattern):
    i = 0
    while i < 3:
        k = 0
        while k < 3:
            if pattern[i][k] == pattern[i+1][k] and pattern[i][k] == pattern[i][k+1] and pattern[i][k] == pattern[i+1][k+1]:
                return False
                break
            k += 1
        i += 1
    return True


def result():
    if cute(pattern):
        print("Yes")
    if not cute(pattern):
        print("No")

result()
