#program to find the closest reduced, proper fraction to 3/7
#that has a denominator <= 1000000

from time import time

def gcd(a,b):
    while b != 0:
        a,b = b,a%b
    return a

def isLarger(a,b):
    a_num = a[0]*b[1]
    b_num = b[0]*a[1]
    return a_num > b_num

def isReduced(a):
    return gcd(a[0],a[1]) == 1

important = (3,7)
closest = (1,10)

start = time()

for d in range(2,1000001):
    for n in range((3*d)//7, d):
        if d == 7 and n == 3:
            break
        temp = (n,d)
        if isLarger(temp, important):
            break
        if isReduced(temp) and isLarger(temp,closest):
            closest = temp

stop = time()

print(closest[0], "/", closest[1])
print(stop-start)

#answer: 428570 / 999997
#running time: approx 13 seconds
