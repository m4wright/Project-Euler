from Number_Theory import isPentagonal
from time import time

num1 = 0
num2 = 0
i = 0

pent = []
test = True

start = time()

while test:
    i += 1
    num1 = int((3*i - 1)*i/2)
    pent.append(num1)

    for x in pent[:-1]:
        if isPentagonal(num1+x) and isPentagonal(num1-x):
            num2 = x
            test = False
            break
    #if i % 100 == 0:
     #   print(i, num1)
    


print(num1, num2, num1-num2, time()-start)
