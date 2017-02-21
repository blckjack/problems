f_in = open("INPUT.txt")
A = [int(s) for s in f_in.readline().strip().split()]
B = [int(s) for s in f_in.readline().strip().split()]

k = 0
i = 0
a = []
while i <= len(A) - 1:
    while k <= len(B) - 1:
        z = int(str(A[i]) + str(B[k]))
        k += 1
        a.append(z)
    k = 0
    i += 1

print(" ".join(map(str, a)))
