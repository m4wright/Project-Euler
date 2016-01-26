# Sum of all primes below two million

L = [x for x in range(2000000)]
L[1] = 0

for i in range(4,len(L), 2):
	L[i] = 0
	
x = 3
while x**2 <= len(L):
	if L[x] != 0:
		for i in range(2*x,len(L),x):
			L[i] = 0
	x += 2
	
print(sum(L))

# sum(L) = 142913828922
