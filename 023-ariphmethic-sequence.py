# http://acmp.ru/asp/do/index.asp?main=task&id_course=1&id_section=7&id_iic=119&id_problem=736

f_in = open("INPUT.txt")
# a = [int(s) for s in f_in.readlines()]
# b = [int(s) for s in f_in.readline().split().strip()]


# handle a different input.txt
a = [193, 67, 13, 0, 46, 53, 22, 0, 13, 23, 123]


# def quickSort(l, r):

#     x = a[len(a)//2]
#     i = l
#     j = r

#     while i <= j:
#         while a[i] < x and a[j] > x:
#             if i <= j:
#                 tmp = a[i]
#                 a[i] = a[j]
#                 a[j] = tmp
#             j -= 1
#             i += 1
#         if j > l:
#             quickSort(l, j)
#         if r > i:
#             quickSort(i, r)
#     print(a)

# partion array


# sort array


def partition(list, start, end):
    pivot = list[end]
    j = start-1
    i = end

    done = 0
    while not done:

        while not done:
            j += 1

            if list[j] > pivot:
                list[i] = list[j]
                break

            if j == i:
                done = 1
                break
        
        while not done:
            i -= 1

            if list[i] < pivot:
                list[j] = list[i]
                break

            if i == j:
                done = 1
                break
    list[i] = pivot                          # Put the pivot in its place.
    return i                                 # Return the split point


def quicksort(list, start, end):
    if start < end:
        split = partition(list, start, end)
        quicksort(list, start, split-1)
        quicksort(list, split+1, end)
    else:
        return
    print(list)


quicksort(a, 0, (len(a)-1))
