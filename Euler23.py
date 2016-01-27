# Program to find the sum of all numbers that cannot be expressed as the sum of two abundant numbers. An abundant number
# is a number where the sum of its proper factors is larger than the number itself.

def factors(n):
    fact = []
    i = 1
    while i*2 <= n:
        if n % i == 0:
            fact.append(i)
        i += 1
    return fact

def isAbundant(n):
    if sum(factors(n)) > n:
        return True




abundant = [x for x in range(12,28123-12+1) if isAbundant(x)]


sumsOfAbundant = [False for x in range(28123)]
for i in range(len(abundant)):
    for j in range(i, len(abundant)):
        a = abundant[i]+abundant[j]
        if a < len(sumsOfAbundant):
            sumsOfAbundant[a] = True

ans = 0

for i in range(len(sumsOfAbundant)):
    if not sumsOfAbundant[i]:
        ans += i
        
 
print(ans)

#ans = 4179871
