# Program to find the sum of all numbers which are equal to the sum of the factorial
# of their digits

import time

fact = [1]
for i in range(1,10):
	fact.append(i*fact[-1])

tot = 0

start = time.time()

for i in range(10, 7*fact[9]):
    total = 0
    for x in str(i):
        total += fact[int(x)]
    if total == i:
        tot += i

print(tot)
print(time.time()-start)

#answer: 40730
