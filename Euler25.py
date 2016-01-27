# Program to find the index of the first term in the fibonacci sequence to contain 1000 digits

fib1, fib2 = 1, 1
i = 2
while len(str(fib2)) < 1000:
	fib1, fib2 = fib2, fib1 + fib2
	i += 1
	
print(i)

#answer: i = 4782
