import random


def compute_power(a, t, n):
    """
    Computes the first element of the miller rabin sequence.
    :param a: the base
    :param t: t such that (2 ^ s) * t = n - 1
    :param n: the initial number
    :return: return pow(a, t) mod n
    """
    result = 1
    x = a

    """
    We will use the binary representation of t. For each bit that is equal to 1, we will multiple the result with 
    a ^ (2 ^ i) where i represents the position of the bit from right to left.
    """
    while t > 0:
        # if the rightmost bit is 1, then we add x to the result
        if t & 1:
            result = (result * x) % n

        # shift the bits with one position to the right
        t = t >> 1

        # increase the x. x is of shape a ^ (2 ^ i), so a ^ (2 ^ (i + 1)) = a ^ (2 ^ i) * a ^ (2 ^ i)
        x = (x * x) % n

    return result


def miller_rabin_test(n, s, t, used_bases):
    """
    Does the miller rabin test for an iteration.
    :param n: the number to be checked
    :param s: s such that (2 ^ s) * t = n - 1
    :param t: t such that (2 ^ s) * t = n - 1
    :param used_bases: the array of used bases
    :return: True if the number is probable prime, False otherwise
    """
    # choose a random between 2 and n - 1
    a = random.randint(2, n - 1)

    """
    Check if the random base has not been used.
    """
    if a in used_bases:
        while a in used_bases:
            a = random.randint(2, n - 1)

    used_bases.append(a)

    """
    Compute the first element of the sequence. a ^ t
    """
    val = compute_power(a, t, n)

    """
    if the first element of the sequence is 1 or if the first element is -1, since s is at least 1, it means that
    the next element of the sequence will be 1.
    """
    if val == 1 or val == n - 1:
        return True

    # Computes the elements of the sequence
    j = 1
    while j <= s:
        val = (val * val) % n

        # if we get a one, but there is no -1 before, there is an error
        if val == 1:
            return False
        # if we get a -1, and we haven't reached the end of the sequence, it means that the number might pe prime.
        if val == n - 1 and j < s:
            return True
        j += 1

    return False


def is_prime(n, k):
    """
    Checks if a number is probable prime or not using miller rabin test
    :param n: the number to be checked
    :param k: the number of iterations
    :return:
    """
    if n == 2:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    if n <= 3:
        return True

    """
    Find s and t such that (2^s) * t = n - 1 
    """
    s = 0
    t = n - 1
    while t % 2 == 0:
        s += 1
        t //= 2

    """
    For each iteration, a new base will be used for computations, which is generated randomly, and 
    we need to make sure that we use a certain base only once.
    """
    used_bases = []

    """
    If the number of iterations is greater than the n - 2, adjust the iterations.
    """
    if k > n - 2:
        k = n - 2

    for _ in range(k):
        if miller_rabin_test(n, s, t, used_bases) is False:
            return False

    return True


print("The prime numbers less than 1000 are:")
l = []
for i in range(1000):
    if is_prime(i, 4):
        l.append(i)

print(l)
