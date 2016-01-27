# See https://projecteuler.net/problem=28 for question

f1 = lambda n: (2*n + 1)**2	       # formula to calculate the value at the top right corner

f_corners = lambda n: 4*f1(n) - 12*n  # formula to calculate the sum of the corners
ans = 1								  # we don't want to calculate the middle 4 times, so start with this
for i in range(1,501):				  # to make a 1001x1001 spiarl, we go 500x around
    ans += f_corners(i)

print(ans)

#ans =669171001
