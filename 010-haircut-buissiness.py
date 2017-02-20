f_in = open("INPUT.txt")
N = [int(s) for s in f_in.readline().strip().split()]
AA = [int(s) for s in f_in.readline().strip().split()]

length = 1
max_kurs = 1
day = 0
wallet = 0
while day < (len(AA) - 1):
    if AA[day] > max_kurs:
        max_kurs = AA[day]
        wallet = max_kurs * length + wallet
        max_kurs = 0
        length = 0
    if AA[day] < max_kurs:
        length += 1
    day += 1

print(len(AA) - 1 )
