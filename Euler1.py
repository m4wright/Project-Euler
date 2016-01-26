#Program to calculate the sum of all numbers from 1 t0 1000 (exclusive) that are divisible by 3 or 5.

def bad_version():
	ans = 0
	for i in range(1,1000):
		if i % 3 == 0 or i % 5 == 0:
			ans += i
	return ans
	
def good_version():
	ans = 3*(333*334)//2
	ans += 5*(199*200)//2
	ans -= 15*(66*67)//2
	return ans
	
	
#answer: 233168
