# Find the value of d_1 * d_10 * d_100 * d_1000 * d_10000 * d_100000 * d_1000000
# where d_i is the ith digit of the fractional part of Champernowne's constant

s = ''
for i in range(1,1000001):
	s += str(i)

ans = 1
for i in range(7):
	ans *= int(s[10**i - 1])
	
print(ans)

#ans = 210
