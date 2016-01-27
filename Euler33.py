# See https://projecteuler.net/problem=33 for question

import GCD
import time

tot_num = 1
tot_denom = 1
count = 0

start = time.time()

while count < 4:
    for num in range(11, 100):
        for denom in range(num+1, 100):
            #print(num, denom)
            denom_list = []
            num_list = []
            for i in str(num):
                num_list.append(int(i))
            for i in str(denom):
                denom_list.append(int(i))
            if str(num)[0] in str(denom) and str(num)[0] != '0':
                denom_list.remove(num_list[0])
                num_list.pop(0)
                if num_list[0] != 0 and denom_list[0] != 0:
                    if num/denom == num_list[0]/denom_list[0]:
                        tot_num *= num
                        tot_denom *= denom
                        count += 1
                        print(num, denom)
            elif str(num)[1] in str(denom) and str(num)[1] != '0':
                denom_list.remove(num_list[1])
                num_list.pop(1)
                if num_list[0] != 0 and denom_list[0] != 0:
                    if num/denom == num_list[0]/denom_list[0]:
                        tot_num *= num
                        tot_denom *= denom
                        print(num, denom)
                        count += 1

print(tot_num, tot_denom)
print(GCD.reduce_fraction(tot_num, tot_denom))
print(time.time()-start)
