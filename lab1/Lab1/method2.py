# Stein's Algorithm

def method_two_gcd(a, b):
    # if a == 0, then the gcd is b, or if b == 0, then the gcd is a.
    if a == 0:
        return b
    if b == 0:
        return a

    # find the greatest power of 2 that divides both a and b
    p2 = 0

    while (a | b) & 1 == 0:
        a = a >> 1
        b = b >> 1
        p2 += 1

    # divide a by 2 until it becomes odd
    while a & 1 == 0:
        a = a >> 1

    # at this point, a will be odd
    while b != 0:
        # if b is even, then divide it by 2 until we get an odd number
        while (b & 1) == 0:
            b = b >> 1

        r = a % b
        a = b
        b = r

    # multiply the result with the power of 2 we computed earlier.
    return a << p2


print(method_two_gcd(125412551, 124512553))


