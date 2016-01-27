# See https://projecteuler.net/problem=33 for question

from isPrime import isPrime
import time

def isTrunctPrime(n):
    number = []
    for i in str(n):
        number.append(int(i))
    test_num = number[:]
    while len(test_num) > 0:
        if isPrime(int(''.join(map(str, test_num)))) == False:
            return False
        else:
            test_num.pop()
    test_num = number[:]
    test_num.pop(0)
    while len(test_num) > 0:
        if not isPrime(int(''.join(map(str, test_num)))):
            return False
        else:
            test_num.pop(0)

    return True
            

num = 0
i = 10
total = 0
while num < 11:
    if isTrunctPrime(i):
        total += i
        num += 1
    i += 1

print(total)
