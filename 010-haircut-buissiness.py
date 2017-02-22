#  http://acmp.ru/asp/do/index.asp?main=task&id_course=2&id_section=10&id_topic=4&id_problem=18
f_in = open("INPUT.txt")
N = [int(s) for s in f_in.readline().strip().split()]
AA = [int(s) for s in f_in.readline().strip().split()]

current_day = 0
wallet = 0
while current_day < len(AA):
    hair_length = 1
    i = current_day
    max_kurs = AA[i]
    max_kurs_position = i
    max_hair_length = hair_length
    while i < len(AA):
        if max_kurs < AA[i]:
            max_kurs = AA[i]
            max_kurs_position = i
            max_hair_length = hair_length
        hair_length += 1
        i += 1
    current_day = max_kurs_position
    wallet = wallet + max_hair_length * max_kurs
    current_day += 1
print(wallet)
