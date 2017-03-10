# http://acmp.ru/asp/do/index.asp?main=task&id_course=1&id_section=7&id_topic=119&id_problem=736

f_in = open("INPUT.txt")
a = [int(x) for x in f_in.read().split()]


def quickSort(left, right):
    x = a[(left+right)//2]
    i = left
    j = right
    while i <= j:
        while a[i] < x:  # tried if, instead of while.
            i += 1
        while a[j] > x:
            j -= 1
        if i <= j:  # forgot about if.
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1
    if i < right:
        quickSort(i, right)
    if j > left:
        quickSort(left, j)


def progression(list):
    quickSort(0, (len(a) - 1))
    j = len(a) - 1
    i = j - 1
    while i > 0:
        if list[j] - list[i] != list[j-1] - list[i-1]:
            return False
        i -= 1
        j -= 1
    return True

if progression(a):
    print("Yes")
else:
    print("No")
