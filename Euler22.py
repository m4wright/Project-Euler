# Program to find the total score of all names in a file (see https://projecteuler.net/problem=22 for file), where
# the score of a name is the sum of the numeric value for a character multiplied by its position when sorted, 
# where 'a' = 1, 'b' = 2, etc

import Sort

names = []

with open("p022_names.txt") as filestream:
    for line in filestream:
        currentline = line.split(",")
        for i in currentline:
            names.append(i)


sorted_names = Sort.sort(names)

all_names_total = 0

for name in sorted_names:
    total = 0
    number = [ord(char)-96 for char in name[1:-1].lower()]
    total = sum(number)
    all_names_total += total*(sorted_names.index(name)+1)

filestream.close()

print(all_names_total)

#answer = 871198282
