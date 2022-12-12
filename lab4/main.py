import random


def is_prime(number):
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False

    i = 3
    while i * i <= number:
        if number % i == 0:
            return False
        i += 2

    return True


def gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r

    return a


def find_e(number):
    i = 3
    while i < number:
        if is_prime(i) and gcd(i, number) == 1:
            return i
        i += 2

    return 3


def get_numerical_equivalent(group):
    group_to_encrypt = reversed(group)
    power = 1
    s = 0
    for i in group_to_encrypt:
        if i == '_':
            ascii_code = 0
        else:
            ascii_code = ord(i) - ord('A') + 1
        s += ascii_code * power
        power *= 27

    return s


def convert_to_encrypted_group(number, group_size):
    string = ''

    while number:
        string = alphabet[number % 27] + string
        number //= 27

    return string.rjust(group_size, "_")


def split_message(message, split_group_size):
    _split = [message[i:i + split_group_size] for i in range(0, len(message), split_group_size)]

    if len(_split[-1]) < split_group_size:
        _split[-1] = _split[-1].ljust(split_group_size, '_')

    return _split


def rsa(message, split_group_size, power, n, encryption_group_size):
    _split_message = split_message(message, split_group_size)

    result = ''

    for i in range(len(_split_message)):
        m = get_numerical_equivalent(_split_message[i])
        encryption = pow(m, power, n)
        result = result + convert_to_encrypted_group(encryption, encryption_group_size)

    return result


prime_numbers = [ 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139,]
alphabet = ['_', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
index = random.randint(0, 20)

p = prime_numbers[index]
q = prime_numbers[index + 1]

n = p * q
phi = (p - 1) * (q - 1)
e = find_e(phi)
d = pow(e, -1, phi)
public_key = gcd(n, e)
private_key = d

k = 3
l = 2

print(str(pow(27, k)) + ", " + str(n) + ',' +str(pow(27, l)))

message = "ottawa".upper()
print("Message data = " + message)

encrypted_message = rsa(message, k, e, n, l)
print("Encrypted message = " + encrypted_message)
print("Decrypted message = " + rsa(encrypted_message, l, d, n, k).strip('_'))

