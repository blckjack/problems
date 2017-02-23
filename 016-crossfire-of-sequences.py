# http://acmp.ru/asp/do/index.asp?main=task&id_course=2&id_section=10&id_topic=4&id_problem=17
f_in = open("INPUT.txt")
N = [int(s) for s in f_in.readline().strip().split()]
first_sequence = [int(s) for s in f_in.readline().strip().split()]
second_sequence = [int(s) for s in f_in.readline().strip().split()]
final_sequence = []

i = 0
while i < len(first_sequence):
    k = 0
    while k < len(second_sequence):
        if first_sequence[i] == second_sequence[k]:
            if first_sequence[i] not in final_sequence:
                final_sequence.append(first_sequence[i])
                n = 0
                while n < len(final_sequence):
                    sp = n
                    minimal_value = 100000000
                    while sp < len(final_sequence):
                            if final_sequence[sp] < minimal_value:
                                minimal_value = final_sequence[sp]
                                minimal_value_index = sp
                            sp += 1
                    t = final_sequence[n]
                    final_sequence[n] = minimal_value
                    final_sequence[minimal_value_index] = t
                    n += 1
        k += 1
    i += 1
print(" ".join(map(str, final_sequence)))
