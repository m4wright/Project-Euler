# Program to calculate the largest 1 to 9 pandigital number that can be formed as
# thhe concatenated product of an integer with (1,2,...,n) where n > 1

num = 0

def isPandigital(n):
    l = [int(x) for x in str(n)]
    l.sort()
    if l == [x for x in range(1, 10)]:
        return True
    else:
        return False

for i in range(9000, 10000):
    test = int(str(i) + str(i*2))
    if isPandigital(test):
        num = test

print(num)

#answer: 932718654
