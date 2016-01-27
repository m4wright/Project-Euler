# For which value of p <= 1000 where p is the perimeter of a right angle triangle,
# is the number of integer solutions maximized?

import time

def num_soln(p):
    total = 0
    numbers = []
    for a in range(1, p):
        for b in range(1, p-a):
            c = p-a-b
            if a not in numbers and b not in numbers:
                if c**2 == a**2 + b**2 or c**2 == a**2 - b**2 or c**2 == b**2 - a**2:
                    total += 1
                    numbers.append(a)
                    numbers.append(b)
                    numbers.append(c)

    return total

max_num = 0
place = 0

start = time.time()

for i in range(1, 1001):
    soln = num_soln(i)
    if max_num < soln:
        max_num = soln
        place = i

print(max_num, place)
print(time.time()-start)

#brute force solution, takes approx 6 minutes
#answer: 840
