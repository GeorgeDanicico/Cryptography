def method_one_gcd(a, b):
    minim = a if a < b else b

    if a == 0:
        return b
    if b == 0:
        return a

    divisor = 1

    for i in range(2, minim // 2):
        if a % i == 0 and b % i == 0:
            divisor = i

    return divisor
