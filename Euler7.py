# Program to find the 10 0001'st prime number

def isPrime(n):
	if n <= 3:
		return True
	if n % 2 == 0:
		return False
	x = 3
	while x**2 <= n:
		if n % x == 0:
			return False
		x += 2
	return True
	
x = 1
count = 1

while count < 10001:
	x += 2
	if isPrime(x):
		count += 1
	
print(x)

# x = 104783
# takes 0.48 seconds
