# http://acmp.ru/asp/do/index.asp?main=task&id_problem=726
f_in = open("INPUT.txt")
N = [int(s) for s in f_in.readline().strip().split()]
AA = [int(s) for s in f_in.readline().strip().split()]

current_position = 0
while current_position < len(AA):

    scan_position = current_position
    mini = 100000000000

    while scan_position < len(AA):
        if mini > AA[scan_position]:
            mini = AA[scan_position]
            mini_index = scan_position
        scan_position += 1

    # now mini is minimum for AA[current_position:]
    # so swap it with first element
    t = AA[current_position]
    AA[current_position] = mini
    AA[mini_index] = t

    current_position += 1


print(" ".join(map(str, AA)))
