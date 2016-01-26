# Program to find the largest prime factor of 600851475143

def largestPrimeFactor(n):
	while n % 2 == 0:
		n //= 2
	x = 3
	while x < n:
		if n % x == 0:
			n //= x
		else:
			x += 2
	return n
	
print(largestPrimeFactor(600851475143))

# anser = 6857
