# Program to find the index of the first term in the fibonacci sequence to contain 1000 digits

fibonacci = [1,1]
i = 2
while len(str(fib[-1])) < 1000:
	fib.append(fib[-1] + fib[-2])
	i += 1
	
print(i)

#answer: i = 4782
