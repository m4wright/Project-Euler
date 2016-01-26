# Program to calculate the smallest number that is evenly divisible by all of the numbers from 1 to 20

def gcd(a,b):
	while b != 0:
		a,b = b,a%b
	return a
	
def lcm(a,b):
	g = gcd(a,b)
	return (a*b)//g
	
l = 1
for i in range(1,21):
	l = lcm(l,i)
	
print(l)
