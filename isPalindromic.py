# Program to determine if a number is palindromic

def isPalindromic(n):
    num = str(n)
    i = 0
    while i*2 < len(num):
        if num[i] != num[-i-1]:
            return False
        i += 1
    return True
