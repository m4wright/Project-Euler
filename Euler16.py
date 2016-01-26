# Sum of the digits of the number 2^1000

print(sum([int(x) for x in str(2**1000)]))

# using a less pythonic way:
L = [1]
for i in range(1000):
	for j in range(len(L)):
		L[j] *= 2
	l = len(L)
	for j in range(l):
		if L[j] > 9:
			if j == l-1:
				L.append(L[j]//10)
			else:
				L[j+1] += L[j]//10
			L[j] %= 10
	
	print(sum(L))

# answer: 1366
