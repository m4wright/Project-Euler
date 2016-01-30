# Program to find the next triangle number after 40755 that is also pentagonal and hexagonal

from Quadratic_formula import quad_formula
import time

def isHexagonal(n):
    soln = quad_formula(2, -1, -n)
    if soln[0] > 0 and soln[0] == int(soln[0]) or soln[1] > 0 and soln[1] == int(soln[1]):
        return True
    else:
        return False

def isTriangular(n):
    soln = quad_formula(1, 1, -2*n)
    if soln[0] > 0 and soln[0] == int(soln[0]) or soln[1] > 0 and soln[1] == int(soln[1]):
        return True
    else:
        return False

def isPentagonal(n):
    soln = quad_formula(3, -1, -2*n)
    if soln[0] > 0 and soln[0] == int(soln[0]) or soln[1] > 0 and soln[1] == int(soln[1]):
        return True
    else:
        return False

check = True

n = 144
start = time.time()

while check:
    total = n*(2*n - 1)
    if isPentagonal(total) and isTriangular(total):
        check = False
        print(total)
        print(time.time()-start)
        break
    n += 1
    
#answer: 1533776805
