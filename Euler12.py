# Program to find the first triangular number that has over five hundred divisors

def primeFactors(n):

        if n > 0 and n < 2:
                return n
        if n < 0:
                print("Error!")
                return None

        primes = []
        i = 2
        c = n
        while i <= c:
                if c % i == 0:
                        primes.append(i)
                        c /= i
                        i = 2
                else:
                        i += 1
        return primes
        
def num_prime_factors(n):
        primes = primeFactors(n)
        new_primes = []

        for i in primes:
                if i not in new_primes:
                        new_primes.append(i)

        return len(new_primes)
        
        
t = 3
i = 3
while num_factors(t) <= 500:
	t += i
	i += 1
	
print(t)

#ans: t = 76576500
