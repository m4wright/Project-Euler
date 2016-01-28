"""
Number theory module
By: Mathew Wright
"""

def gcd(a, b):
    while b != 0:
        a, b = b, a%b
    return a

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

def largestPrimeFactor(n):
        return primeFactors(n)[-1]

def num_prime_factors(n):
        primes = primeFactors(n)
        new_primes = []

        for i in primes:
                if i not in new_primes:
                        new_primes.append(i)

        return len(new_primes)

def distinctPrimes(n):
        if n > 0 and n < 2:
                return n
        if n < 0:
                return "Error!"

        primes = []
        i = 2
        c = n
        while i <= c:
                if c % i == 0:
                        if i not in primes:
                                primes.append(i)
                        c /= i
                        i = 2
                else:
                        i += 1
        return primes

def totient(n):
    p = distinctPrimes(n)
    t = n
    for i in p:
        t *= (1 - 1/i)
    return int(round(t))

def linear_eq(a, b):
    return -b/a


def quad_formula(a, b, c):
    
    if (b**2 - 4*a*c) < 0:
        return False
    x1 = (-b + (b**2 - 4*a*c)**(0.5))/(2*a)
    x2 = (-b - (b**2 - 4*a*c)**(0.5))/(2*a)
    return (x1, x2)    


def factorial(n):
    if n == 0 or n == 1:
        return 1
    total = n
    for i in range(1, n):
        total *= i
    return total


def num_factors(n):
    primes = primeFactors(n)
    number = []
    while len(primes) > 0:
        number.append(primes.count(primes[0]))
        primes = list(filter(primes[0].__ne__, primes))

    number_of_factors = 1
    for i in number:
        number_of_factors *= (i+1)
    return number_of_factors



def factors(n):
    fact = []
    i = 1
    while i*2 <= n:
        if n % i == 0:
            fact.append(i)
        i += 1
    fact.append(n)
    return fact

def fib(n):
    num1 = 1
    num2 = 1
    for i in range(n-2):
        num2, num1 = num1+num2, num2
    return num2

def isFib(n):
    x1 = 5*n**2 + 4
    x2 = 5*n**2 - 4
    x1 **= 0.5
    x2 **= 0.5
    if x1 == int(x1) or x2 == int(x2):
        return True
    else:
        return False


def sum_proper_divisors(n):
    total = 0
    i = 1
    while i*2 <= n:
        if n % i == 0:
            total += i
        i += 1
    return total

def isAmicable(a, b):
    if a != b and sum_proper_divisors(a) == b and sum_proper_divisors(b) == a:
        return True
    else:
        return False

def isPalindromic(n):
    num = str(n)
    i = 0
    while i*2 < len(num):
        if num[i] != num[-i-1]:
            return False
        i += 1
    return True

def isPermutation(a, b):
    num1 = str(a)
    num2 = str(b)

    for i in num1:
        if i not in num2:
            return False
        else:
            num2 = num2.replace(i, "", 1)

    return True
    

def isPrime(n):
    if n == 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    i = 3
    
    while i**2 <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def isSquare(n):
    x = n // 2
    seen = set([x])
    while x*x != n:
        x = (x + (n // x)) // 2
        if x in seen:
            return False
        seen.add(x)
    return True

def isTriangular(t):
    facts = quad_formula(1, 1, -2*t)
    if facts[0] == int(facts[0]) and facts[0] > 0:
        return True
    if facts[1] == int(facts[1]) and facts[1] > 0:
        return True
    return False

def isPentagonal(p):
    facts = quad_formula(3, -1, -2*p)
    if facts[0] == int(facts[0]) and facts[0] > 0:
        return True
    if facts[1] == int(facts[1]) and facts[1] > 0:
        return True
    return False



