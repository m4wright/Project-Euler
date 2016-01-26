# Program to find the largest palindrome made from the product of two 3-digit numbers

def isPalindrome(n):
	L = [int(x) for x in str(n)]
	return L == L[::-1]
	
largestPalindrome = 0
for i in range(100,1000):
	for j in range(i, 1000):
		temp = i*j
		if temp > largestPalindrome and isPalindrome(temp):
			largestPalindrome = temp
			
print(largestPalindrome)
