# euclid algorithm
def method_three_gcd(a, b):

    while b != 0:
        r = a % b
        a = b
        b = r

    return a

