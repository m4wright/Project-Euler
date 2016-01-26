# number of letters used to write the numbers from 1 to 1000

zero = 0
one = 3
two = 3
three = 5
four = 4
five = 4
six = 3
seven = 5
eight = 5
nine = 4
ten = 3
eleven = 6
twelve = 6
thirteen = 8
fourteen = 8
fifteen = 7
sixteen = 7
seventeen = 9
eighteen = 8
nineteen = 8
twenty = 6
thirty = 6
fourty = 5
fifty = 5
sixty = 5
seventy = 7
eighty = 6
ninety = 6
hundred = 7

digits = []
digits.append(zero)
digits.append(one)
digits.append(two)
digits.append(three)
digits.append(four)
digits.append(five)
digits.append(six)
digits.append(seven)
digits.append(eight)
digits.append(nine)

teens = []
teens.append(ten)
teens.append(eleven)
teens.append(twelve)
teens.append(thirteen)
teens.append(fourteen)
teens.append(fifteen)
teens.append(sixteen)
teens.append(seventeen)
teens.append(eighteen)
teens.append(nineteen)

wholes = []
wholes.append(twenty)
wholes.append(thirty)
wholes.append(fourty)
wholes.append(fifty)
wholes.append(sixty)
wholes.append(seventy)
wholes.append(eighty)
wholes.append(ninety)

ands = 3



def num_letters(n):
    dig = []
    for i in str(n):
        dig.insert(0, int(i))
    total = 0
    if len(dig) == 1:
        total = digits[n]
        return total
    elif len(dig) == 2:
        if dig[1] == 1:
            total = teens[n-10]
            return total
        else:
            total = digits[dig[0]]
            total += wholes[dig[1]-2]
            return total
    elif len(dig) == 3:
        total = hundred
        if not(dig[0] == 0 and dig[1] == 0):
            total += ands
        total += digits[dig[2]]
        total += num_letters(n%100)
        return total
        


ans = 11

for i in range(1, 1000):
    ans += num_letters(i)

print(ans)

# ans = 21124
