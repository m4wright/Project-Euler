# program to calculate the sum of all amicable numbers under 10000

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

total = 0

amicables = []

for i in range(1, 10000):
    sum_div = isAmicable.sum_proper_divisors(i)
    if isAmicable.isAmicable(i, sum_div) and i not in amicables:
        total += (i+sum_div)
        amicables.append(i)
        amicables.append(sum_div)

print(total)

# answer: 31626
