# Program to find the longest reccuring cycle in its decimal fraction for the fractions
# 1/d where 1 < d < 1000

def isRepeating(d):
    while d % 5 == 0:
        d //= 5
    while d % 2 == 0:
        d //= 2
    return d != 1

def recurringCycle(d):
    if not isRepeating(d):
        return 0
    r = 10
    r %= d
    remainder = []
    while r not in remainder:
        remainder.append(r)
        while r < d:
            r *= 10
        r  %= d
    return len(remainder)-remainder.index(r)

index = 0
maximum = 0

for i in range(2,1000):
    length = recurringCycle(i)
    if length > maximum:
        maximum = length
        index = i

print(index)

#answer: 983
