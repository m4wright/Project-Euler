# Program to find the number of ways that a 2 pounds can be made using any number of coins
# where you can use 1p, 2p, 5p, 10p, 20p, 50p, 1 pound and 2 pounds

ways = 0

for a in range(200, -1, -200):
    for b in range(a, -1, -100):
        for c in range(b, -1, -50):
            for d in range(c, -1, -20):
                for e in range(d, -1, -10):
                    for f in range(e, -1, -5):
                        for g in range(f, -1, -2):
                            ways += 1

print(ways)

# answer: 73682
