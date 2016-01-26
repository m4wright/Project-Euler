# Program to calculate the sum of the even fibonacci numbers that are less than 4 million.

fib = [1,1]
ans = 0

while fib[-1] < 4000000:
	fib.append(fib[-1] + fib[-2])
	if fib[-1] % 2 == 0:
		ans += fib[-1]

print(ans)

# ans = 4613732
