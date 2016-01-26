# Program to calculate a*b*c where a^2 + b^2 = c^2 and a+b+c = 1000

def ans():
	for a in range(1,999):
		for b in range(a+1,1000):
			c = 1000-a-b
			if a**2 + b**2 == c**2:
				return a*b*c
				
				
print(ans())

#ans = 31875000
