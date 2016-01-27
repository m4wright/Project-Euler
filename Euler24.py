# Program to find the millionth lexicographic permutation of the digits 0,1,2,3,4,5,6,7,8,9

from Sort import sort
import itertools

numbers = []


for i in itertools.permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]):
    numbers.append(int(''.join(map(str, i))))
    if len(numbers) == 1000000:
    	print(numbers[-1])
    	break


#ans = 2783915460
