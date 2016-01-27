def fact(n):
	a = 1
	for i in range(1,n+1):
		a *= i
	return a
	
print(sum([int(x) for x in str(fact(100))]))

# ans: 648
# For a less pythonic way of calculating this, see Euler20.java under BigInts
