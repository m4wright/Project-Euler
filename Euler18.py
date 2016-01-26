# program to find the maximum total from top to bottom of a triangle containing 15 lines
# the triangle is in the file p018.txt and can be found at: https://projecteuler.net/problem=18
# Note that this uses a brute force approach. A better solution to the same problem (but with more rows)
# Can be found in Euler67.py

file = open("p018.txt", "r")
r = []
for i in file:
    r.append([int(x) for x in i.split()])



def sums(row, col):
    if row == 0 and col == 0:
        return r[row][col]
    
    if col == 0:
        return sums(row-1, col)+r[row][col]

    if col == len(r[row])-1:
        return sums(row-1, col-1) + r[row][col]
    
    return r[row][col] + max(sums(row-1, col), sums(row-1, col-1))




numbers = [sums(len(r)-1, x) for x in range(len(r[-1]))]

print(max(numbers))
