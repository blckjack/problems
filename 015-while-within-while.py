f_in = open("INPUT.txt")
A = [int(s) for s in f_in.readline().strip().split()]

B = []
C = [A[2], A[3]]
i = 0
b = 0
while b < len(A)//2:
    B.append(A[b])
    b += 1

print(B)


# A = [int(s) for s in f_in.readline().strip().split()]
# B = [int(s) for s in f_in.readline().strip().split()]

# k = 0
# i = 0
# while i <= len(A) - 1:
#     k = 0
#     while k <= len(B) - 1:
#         z = int(str(A[i]) + str(B[k]))
#         k += 1
#         print(z,)
#     i += 1
