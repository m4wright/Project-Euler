# Program to find the difference between the sum of squares of the first 100 natural numbers
# and the square of the sum

ans = ((100*101)//2)**2 - sum([x**2 for x in range(1,101)])
print(ans)

#ans = 25164150
