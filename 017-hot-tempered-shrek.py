# http://acmp.ru/asp/do/index.asp?main=task&id_course=1&id_section=7&id_topic=118&id_problem=730
f_in = open("INPUT.txt")
n = [int(s) for s in f_in.readline().strip().split()]
arr = [int(s) for s in f_in.readline().strip().split()]

# sorting:
i = 0  # main iterator
while i < len(arr):
    k = i  # secondary iterator
    minimal_card = 10000000
    while k < len(arr):
        if arr[k] < minimal_card:
            minimal_card = arr[k]
            minimal_card_position = k
        k += 1
    tmp = arr[i]
    arr[i] = minimal_card
    arr[minimal_card_position] = tmp
    i += 1

# find the actual summ of the winning prize:
s = 0
summ_of_shrek = 0
summ_of_dealer = 0
while s < len(arr)//2:
    summ_of_shrek = summ_of_shrek + arr[n[0]//2 + s]
    summ_of_dealer = summ_of_dealer + arr[s]
    s += 1

summ_of_the_win = summ_of_shrek - summ_of_dealer

print(summ_of_the_win)
