f_in = open("INPUT.txt")
n = [int(s) for s in f_in.readline().strip().split()]
'INPUT: 1 5 5 10'
i0, i1, k0, k1 = n

i = i0
while i <= i1:
    k = k0
    while k <= k1:
        print(str(i) + str(k))
        k += 1
    i += 1


# # build sequence A:
# A = []
# i = n[0]
# while i <= n[1]:
#     A.append(i)
#     i += 1
# # build sequence B:
# B = []
# k = n[2]
# while k <= n[3]:
#     B.append(k)
#     k += 1
# # build compared sequence z:
# ii = 0
# while ii < len(A):
#     kk = 0
#     while kk < len(B):
#         z = int(str(A[ii]) + str(B[kk]))
#         kk += 1
#         print(z,)
#     ii += 1

