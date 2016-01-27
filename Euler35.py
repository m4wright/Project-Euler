# Program to count the number of primes below one million such that
# all rotations of the number is also prime

import time

def isPrime(n):
	if n <= 1:
		return False
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

def getRotations(n):
    options = []
    number = []
    for digit in str(n):
        number.append(int(digit))
    x = 0
    while x < len(str(n)):
        number = [number[-1]] + number
        number.pop()
        options.append(int(''.join(map(str, number))))
        x += 1
    return options
    

def isCircularPrime(n):
    
    for number in getRotations(n):
        if isPrime(number) == False:
            return False
    return True


numCircPrimes = 13
start = time.time()
for i in range(100, 1000000):
    if isCircularPrime(i):
        numCircPrimes += 1

print(numCircPrimes)
print(time.time()-start)

# answer: 55
