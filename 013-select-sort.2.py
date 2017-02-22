# http://acmp.ru/asp/do/index.asp?main=task&id_problem=726
f_in = open("INPUT.txt")
N = [int(s) for s in f_in.readline().strip().split()]
AA = [int(s) for s in f_in.readline().strip().split()]

current_position = 0

while current_position < len(AA):
    scan_position = current_position
    minimal_value = 100000000

    while scan_position < len(AA):
        if AA[scan_position] < minimal_value:
            minimal_value = AA[scan_position]
            minimal_value_index = scan_position
        scan_position += 1
    # done with minimal value on a current row
    t = AA[current_position]
    AA[current_position] = minimal_value
    AA[minimal_value_index] = t

    current_position += 1
print(" ".join(map(str, AA)))
