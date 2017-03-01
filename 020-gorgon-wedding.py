# http://acmp.ru/asp/do/index.asp?main=task&id_course=1&id_section=7&id_topic=118&id_problem=731
f_in = open("INPUT.txt")
n = int(f_in.readline().strip())
bridegrooms_wealth = [int(s) for s in f_in.readline().strip().split()]
gorgons_wealth = int(f_in.readline().strip())

i = 0
while i < n:
    k = i
    poorest_wealth = 100000000
    while k < n:
        if bridegrooms_wealth[k] < poorest_wealth:
            poorest_wealth = bridegrooms_wealth[k]
            poorest_bridegroom = k
        k += 1
    tmp = bridegrooms_wealth[i]
    bridegrooms_wealth[i] = poorest_wealth
    bridegrooms_wealth[poorest_bridegroom] = tmp

    if gorgons_wealth < bridegrooms_wealth[i]:
        gorgons_wealth = (gorgons_wealth + bridegrooms_wealth[i]) / 2
    i += 1

print(format(gorgons_wealth, '.6f'))
