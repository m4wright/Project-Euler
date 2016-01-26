# program to find the number under one million that produces the longest collatz chain

def collatz(n):
	count = 0
	while n != 1:
		count += 1
		if n % 2 == 0:
			n //= 2
		else:
			n = 3*n + 1
	return count
	
length = 0
for i in range(2,1000000):
	c = collatz(i)
	if c > length:
		length = c
		value = i
		
print(value)

# value = 837799
