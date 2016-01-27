# Program to find the sum of all numbers less than one million which are palindromic
# in base 10 and base 2

from isPalindromic import isPalindromic
import time

def toBin(n):
    return int(bin(n)[2:])

total = 0

start = time.time()

for i in range(1, 1000001):
    if isPalindromic(i) and isPalindromic(toBin(i)):
        total += i        

print(total)
print(time.time()-start)

#answer: 872187
