# http://acmp.ru/asp/do/index.asp?main=task&id_course=1&id_section=9&id_topic=123&id_problem=767
f_in = open("INPUT.txt")
n = [int(s) for s in f_in.readline().strip().split()]
backpack =[[0]*(n[1]+1) for i in range(n[0])]
keep =[[0]*(n[1]+1) for i in range(n[0])]
profits = {}
weights = {}
bring_with_you = []

i = 0
while i < n[0]:
	m = [int(s) for s in f_in.readline().strip().split()]
	weights[i] = m[0]
	profits[i] = m[1]
	i += 1

i = 0
while i < n[0]:
	k = 0
	while k < n[1]+1:
		if k >= weights[i]:
			t1 = backpack[i-1][k]
			t2 = backpack[i-1][k-weights[i]] + profits[i]
			if t1 > t2:
				keep[i][k] = 0
				backpack[i][k] = t1
			else:
				keep[i][k] = 1
				backpack[i][k] = t2
		else:
			backpack[i][k] = backpack[i-1][k] 
			keep[i][k] = 0
		k += 1
	i += 1

empty_space = n[1]
for k in range(n[0]-1,-1,-1):
	if keep[k][empty_space] == 1:
		bring_with_you.append(k+1)
		empty_space = empty_space - weights[k]

temp = []
for i in bring_with_you:
	temp.append(profits[i-1])

print(len(bring_with_you), sum(temp))
print(*bring_with_you)
