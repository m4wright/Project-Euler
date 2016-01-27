def gcd(x, y):
    while y != 0:
        x, y = y, x%y

    return x
    
def reduce_fraction(a, b):
    gc = gcd(a, b)
    a /= gc
    b /= gc
    return (a, b)
