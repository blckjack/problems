# http://acmp.ru/asp/do/index.asp?main=task&id_problem=726
f_in = open("INPUT.txt")
N = [int(s) for s in f_in.readline().strip().split()]
AA = [int(s) for s in f_in.readline().strip().split()]
'12 7 92 5 18 4 32 48 11 74'
current_position = 0
scan_position = 0
tmp = 0
while current_position < len(AA):
    while scan_position < len(AA):
        if AA[current_position] > AA[scan_position]:
            tmp = AA[scan_position]
            AA[scan_position] = AA[current_position]
            AA[current_position] = tmp
        scan_position += 1
    current_position += 1
    scan_position = current_position
print(" ".join(map(str, AA)))
