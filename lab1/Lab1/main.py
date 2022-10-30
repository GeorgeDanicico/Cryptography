import time
from method2 import method_two_gcd
from method1 import method_one_gcd
from method3 import method_three_gcd


def test_method_one(a, b):
    start_time = time.time()
    gcd = method_one_gcd(a, b)
    print(f"GCD of {a} and {b} is {gcd} and was computed in %s seconds ---" % (time.time() - start_time))


def test_method_two(a, b):
    start_time = time.time()
    gcd = method_two_gcd(a, b)
    print(f"GCD of {a} and {b} is {gcd} and was computed in %s seconds ---" % (time.time() - start_time))


def test_method_three(a, b):
    start_time = time.time()
    gcd = method_three_gcd(a, b)
    print(f"GCD of {a} and {b} is {gcd} and was computed in %s seconds ---" % (time.time() - start_time))


def main():
    print("-----------Test method 1-----------")
    test_method_one(15, 24)
    test_method_one(1591, 2414)
    test_method_one(141245, 2441213)
    test_method_one(15421223, 24909212)
    test_method_one(14413510027, 2412351233)
    print("------------------------------------ \n")

    print("-----------Test method 2-----------")
    test_method_two(15, 24)
    test_method_two(1591, 2414)
    test_method_two(141245, 2441213)
    test_method_two(15421223, 24909212)
    test_method_two(14413510027, 2412351233)
    print("------------------------------------ \n")

    print("-----------Test method 3-----------")
    test_method_three(15, 24)
    test_method_three(1591, 2414)
    test_method_three(141245, 2441213)
    test_method_three(15421223, 24909212)
    test_method_three(14413510027, 2412351233)
    print("------------------------------------ \n")


if __name__ == "__main__":
    main()




