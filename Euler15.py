# Program to find the number of routes from the top left corner down to the bottom right corner
# of a 20x20 grid

def fact(n):
	a = 1
	for i in range(1,n+1):
		a *= i
	return a
	
def binom(n,x):
	return fact(n)//(fact(x)*fact(n-x))
	
print(fact(40,20)

# answer: 137846528820
